#!/usr/bin/env python3
from __future__ import annotations

import argparse
import os
import json
from typing import Optional

from huggingface_hub import HfApi, login


def upload_model(
    local_model_dir: str,
    repo_name: str,
    *,
    username: str = "yuntian-deng",
    token: Optional[str] = None,
    private: bool = False,
    commit_message: Optional[str] = None,
) -> str:
    """
    Upload a local model directory to HuggingFace Hub.
    
    Returns the full repo_id (username/repo_name).
    """
    if not os.path.isdir(local_model_dir):
        raise ValueError(f"Local model directory does not exist: {local_model_dir}")
    
    # Login to HF Hub
    if token:
        login(token=token)
    else:
        login()  # Uses HF_TOKEN env var or prompts for login
    
    api = HfApi()
    repo_id = f"{username}/{repo_name}"
    
    # Create repo if it doesn't exist
    try:
        api.create_repo(repo_id=repo_id, private=private, exist_ok=True)
    except Exception as e:
        print(f"Note: Could not create repo (may already exist): {e}")
    
    # Upload all files from the model directory
    api.upload_folder(
        folder_path=local_model_dir,
        repo_id=repo_id,
        commit_message=commit_message or f"Upload model from {local_model_dir}",
    )
    
    print(f"Successfully uploaded {local_model_dir} to https://huggingface.co/{repo_id}")
    return repo_id


def main() -> None:
    parser = argparse.ArgumentParser(description="Upload trained models to HuggingFace Hub")
    parser.add_argument("model_type", choices=["compiler", "interpreter"], 
                       help="Type of model to upload")
    parser.add_argument("--checkpoint-dir", default="outputs/prefix_kv/checkpoint",
                       help="Checkpoint directory containing compiler/ and interpreter/ subdirs")
    parser.add_argument("--repo-name", help="HF repo name (defaults to paw-{model_type})")
    parser.add_argument("--username", default="yuntian-deng", help="HF username")
    parser.add_argument("--token", help="HF token (or set HF_TOKEN env var)")
    parser.add_argument("--private", action="store_true", help="Create private repo")
    parser.add_argument("--commit-message", help="Custom commit message")
    
    args = parser.parse_args()
    
    # Default repo names
    if not args.repo_name:
        args.repo_name = f"paw-{args.model_type}"
    
    local_dir = os.path.join(args.checkpoint_dir, args.model_type)
    if not os.path.isdir(local_dir):
        raise ValueError(f"Model directory not found: {local_dir}")
    
    repo_id = upload_model(
        local_model_dir=local_dir,
        repo_name=args.repo_name,
        username=args.username,
        token=args.token,
        private=args.private,
        commit_message=args.commit_message,
    )
    
    print(f"\nTo use in eval.py:")
    if args.model_type == "compiler":
        print(f"  # Note: compiler is used automatically during paw.compile()")
        print(f"  # No changes needed for eval.py")
    else:
        print(f"  python eval.py --model-name {repo_id} ...")


if __name__ == "__main__":
    main() 