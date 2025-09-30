import argparse
import json
import logging
import multiprocessing.dummy as mt
import time
from typing import Any, Dict, List


def get_parquet_datasets_info_from_txt(
    dataset_txt_files: List[str],
    output_file_path: str,
    file_system_config: Dict[str, Any] | None = None,
    workers: int = 180,
):
    """
    Read datasets from a list of flat text files (one text file per dataset),
    where each text file contains parquet file paths (one per line).
    Compute dataset-level sub_ds_info and write a raw list to output JSON.

    Any exception during processing will cause the function to fail and no output file
    will be written.

    Args:
        dataset_txt_files: list of text files, each contains parquet paths for a dataset
        output_file_path: path where to save the result as JSON (raw list of lists)
        file_system_config: file system configuration dict (for S3 support)
        workers: number of parallel workers for processing (default: 180)

    """
    try:
        from tqdm import tqdm  # type: ignore
    except Exception:
        tqdm = None

    print(dataset_txt_files)
    from .parquet_dataset import ParquetConcateDataset, create_pyarrow_s3fs

    # Build datasets_filepaths (2-layer list) by reading each flat text file
    datasets_filepaths: List[List[str]] = []
    for txt_path in dataset_txt_files:
        with open(txt_path, "r") as f:
            files = [line.strip() for line in f if line.strip()]
        datasets_filepaths.append(files)

    if not datasets_filepaths or not any(datasets_filepaths):
        raise ValueError("No datasets or file paths found from provided text files")

    # Flatten all file paths for parallel processing
    all_filepaths: List[str] = []
    file_to_dataset_map: Dict[int, tuple[int, int]] = {}
    for dataset_idx, dataset_files in enumerate(datasets_filepaths):
        for file_idx_in_dataset, filepath in enumerate(dataset_files):
            file_to_dataset_map[len(all_filepaths)] = (dataset_idx, file_idx_in_dataset)
            all_filepaths.append(filepath)

    if not all_filepaths:
        raise ValueError("No valid file paths found in datasets")

    # Setup file system
    file_system = None
    if file_system_config and file_system_config.get("type") == "pyarrow_s3":
        file_system = create_pyarrow_s3fs(file_system_config)

    total = len(all_filepaths)
    print(f"Starting processing with {workers} workers (total files: {total:,})...")
    start_time = time.time()

    def _get_sub_ds_length(args: tuple[str, int]):
        path, file_idx = args
        row, row_groups = ParquetConcateDataset._get_sub_ds_length(
            path, file_system=file_system
        )
        return file_idx, row, row_groups

    # Create arguments with file index so we can restore order
    file_args = [(filepath, i) for i, filepath in enumerate(all_filepaths)]

    # Prepare result container
    all_files_sub_ds_info: List[list[int | list[int]] | None] = [None] * total

    # Run with imap_unordered for fast completion updates
    with mt.Pool(workers) as p:
        iterator = p.imap_unordered(_get_sub_ds_length, file_args)
        progress = (
            tqdm(total=total, mininterval=1.0, smoothing=0)
            if tqdm is not None
            else None
        )
        try:
            for file_idx, row, row_groups in iterator:
                all_files_sub_ds_info[file_idx] = [row, row_groups]
                if progress is not None:
                    progress.update(1)
        except Exception:
            if progress is not None:
                progress.close()
            raise
        finally:
            if progress is not None and progress.n < progress.total:
                progress.close()

    # Verify there were no failures
    if any(info is None for info in all_files_sub_ds_info):
        failed = sum(1 for info in all_files_sub_ds_info if info is None)
        raise RuntimeError(
            f"Failed to process {failed} files out of {total}. Aborting without writing output."
        )

    # Group results back into datasets
    datasets_sub_ds_info: List[List[list[int | list[int]]]] = [
        [] for _ in datasets_filepaths
    ]
    for file_idx, file_info in enumerate(all_files_sub_ds_info):
        # type: ignore[unreachable]
        dataset_idx, _ = file_to_dataset_map[file_idx]
        datasets_sub_ds_info[dataset_idx].append(file_info)  # type: ignore[arg-type]

    # Write result to output file as JSON (raw list of datasets_sub_ds_info)
    with open(output_file_path, "w") as f:
        json.dump(datasets_sub_ds_info, f, indent=2)

    # Summary
    total_datasets = len(datasets_sub_ds_info)
    total_files_done = sum(len(dataset_info) for dataset_info in datasets_sub_ds_info)
    total_rows = sum(
        sum(info[0] for info in dataset_info)  # type: ignore[index]
        for dataset_info in datasets_sub_ds_info
    )
    elapsed = time.time() - start_time
    rate = total_files_done / elapsed if elapsed > 0 else 0.0

    logging.info(
        f"Processed {total_datasets} datasets with {total_files_done}/{total} files"
        f"in {elapsed:.1f}s (~{rate:.1f} files/s)"
    )
    logging.info(f"Total rows: {total_rows:,}")
    logging.info(f"Result saved to {output_file_path}")

    return datasets_sub_ds_info


def _build_s3_config_from_args(args: Any) -> Dict[str, Any] | None:
    """
    Build an s3_config dict from CLI args if any S3-related fields are provided.
    Returns None if no S3-related args are given.
    """
    has_any = any(
        [
            getattr(args, "s3_type", None),
            getattr(args, "s3_access_key", None),
            getattr(args, "s3_secret_key", None),
            getattr(args, "s3_endpoint_override", None),
        ]
    )
    if not has_any:
        return None

    cfg: Dict[str, Any] = {}
    if args.s3_type:
        cfg["type"] = args.s3_type
    if args.s3_access_key:
        cfg["access_key"] = args.s3_access_key
    if args.s3_secret_key:
        cfg["secret_key"] = args.s3_secret_key
    if args.s3_endpoint_override:
        cfg["endpoint_override"] = args.s3_endpoint_override
    return cfg


def _parse_args() -> Any:
    parser = argparse.ArgumentParser(
        description=(
            "Compute dataset-level parquet file info from text file lists and save as JSON."
        )
    )

    parser.add_argument(
        "--dataset-txt-files",
        dest="dataset_txt_files",
        nargs="+",
        required=True,
        help="One or more text files; each contains parquet paths (one per line) for a dataset. cannot be nested txts.",
    )

    parser.add_argument(
        "--output-file-path",
        dest="output_file_path",
        required=True,
        help="Path to save the resulting JSON list (datasets_sub_ds_info).",
    )

    parser.add_argument(
        "--workers",
        type=int,
        default=180,
        help="Number of parallel workers (default: 180).",
    )

    # Optional S3 configuration
    parser.add_argument(
        "--s3-type",
        dest="s3_type",
        default=None,
        help='S3 filesystem type (e.g., "pyarrow_s3"). If provided, enables S3 access.',
    )
    parser.add_argument(
        "--s3-access-key",
        dest="s3_access_key",
        default=None,
        help="S3 access key.",
    )
    parser.add_argument(
        "--s3-secret-key",
        dest="s3_secret_key",
        default=None,
        help="S3 secret key.",
    )
    parser.add_argument(
        "--s3-endpoint-override",
        dest="s3_endpoint_override",
        default=None,
        help="S3 endpoint override URL, e.g. https://s3.example.com.",
    )

    return parser.parse_args()


"""
python -m anc_data.parquet_tools \
  --dataset-txt-files /path/ds_a.txt /path/ds_b.txt \
  --output-json /tmp/datasets_sub_ds_info.json \
  --workers 200 \
  --s3-type pyarrow_s3 \
  --s3-access-key "$AWS_ACCESS_KEY_ID" \
  --s3-secret-key "$AWS_SECRET_ACCESS_KEY" \
  --s3-endpoint-override https://s3.example.com
"""
if __name__ == "__main__":
    args = _parse_args()
    get_parquet_datasets_info_from_txt(
        dataset_txt_files=args.dataset_txt_files,
        output_file_path=args.output_file_path,
        file_system_config=_build_s3_config_from_args(args),
        workers=args.workers,
    )
