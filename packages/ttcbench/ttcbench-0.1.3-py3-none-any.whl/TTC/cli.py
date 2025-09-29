import argparse, json, sys, os
from dotenv import load_dotenv
load_dotenv()

from .utils_nvml import list_gpus
from .config import BenchConfig
from .storage import write_jsonl, stamp

def main():
    parser = argparse.ArgumentParser("ttc_bench")
    sub = parser.add_subparsers(dest="cmd")
    sub.add_parser("gpus")

    p_run = sub.add_parser("run")
    p_run.add_argument("--task", required=True, choices=["textgen"])
    p_run.add_argument("--backend", default="openai", choices=["openai"])
    p_run.add_argument("--model", help="Model name or id as in /v1/models")
    p_run.add_argument("--batch", type=int, default=1)
    p_run.add_argument("--seq-in", type=int, default=0)
    p_run.add_argument("--seq-out", "--max-tokens", dest="seq_out", type=int, default=128)
    p_run.add_argument("--steps", type=int, default=30)
    p_run.add_argument("--warmup", type=int, default=5)
    p_run.add_argument("--out", default="runs/results.jsonl")
    p_run.add_argument("--base-url", default=os.getenv("MODEL_BASE_URL"))
    p_run.add_argument("--api-key",  default=os.getenv("MODEL_API_KEY"))
    p_run.add_argument("--timeout", type=int, default=120)
    p_run.add_argument("--endpoint", help="Explicit endpoint path, e.g. /v1/chat/completions")

    # generation params (optional)
    p_run.add_argument("--temperature", type=float)
    p_run.add_argument("--top-p", dest="top_p", type=float)
    p_run.add_argument("--stream", action="store_true")
    p_run.add_argument("--stop", help="Comma-separated stop strings")
    p_run.add_argument("--json", dest="json_mode", action="store_true", help="response_format=json_object")
    p_run.add_argument("--system", help="system prompt")

    args = parser.parse_args()

    if args.cmd == "gpus":
        print(json.dumps(list_gpus(), indent=2, ensure_ascii=False))
        return

    if args.cmd == "run":
        from .runner_textgen_openai import OpenAITextGenRunner

        stop_list = [s for s in (args.stop or "").split(",") if s] if args.stop else None

        cfg = BenchConfig(
            task=args.task,
            backend=args.backend,
            model_id=args.model or os.getenv("DEFAULT_MODEL",""),
            batch_size=args.batch,
            seq_in=args.seq_in,
            seq_out=args.seq_out,
            steps=args.steps,
            warmup_steps=args.warmup,
            base_url=args.base_url,
            api_key=args.api_key,
            timeout_s=args.timeout,
            endpoint=args.endpoint,
            # optional gen params
            temperature=args.temperature,
            top_p=args.top_p,
            stream=args.stream,
            stop=stop_list,
            json_mode=args.json_mode,
            system=args.system,
        )

        runner = OpenAITextGenRunner(cfg)
        res = runner.run()
        res["ts"] = stamp()
        print(json.dumps(res, indent=2, ensure_ascii=False))
        write_jsonl(args.out, res)
        return

    parser.print_help(sys.stderr)

if __name__ == "__main__":
    main()
