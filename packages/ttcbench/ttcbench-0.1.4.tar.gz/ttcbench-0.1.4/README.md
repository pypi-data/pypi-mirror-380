# ttc_bench

Benchmark for OpenAI/vLLM `/v1/chat/completions` endpoints with optional local GPU telemetry.

## Install

```bash
pip install ttc_bench


# env (optional)
echo 'MODEL_BASE_URL=http://host:3000/v1' > .env
echo 'MODEL_API_KEY=' >> .env
echo 'DEFAULT_MODEL=Qwen2.5-72B-Instruct-GPTQ-Int4' >> .env

# run
ttc_bench run --task textgen --steps 10 --batch 2 --seq-out 128 \
  --base-url "http://host:3000/v1" --model "Qwen2.5-72B-Instruct-GPTQ-Int4"
