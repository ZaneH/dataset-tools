## Dataset Tools

[Blog post](https://www.zaaane.com/blog/fine-tuning-llama3-on-1-rtx-3060#preparing-the-dataset)

I use this collection of scripts for creating new datasets to train LLM models.

- **stage1**: Store raw CSV file. Cleanup the base data manually
- **stage2**: Create a JSONL file from each CSV file
- **stage3**: Combin all JSONL files into one

### Example Usage:

- **Required:** Be sure to install the dependency in `requirements.txt`

```bash
$ python ./data/stage2/create-jsonl.py
usage: create-jsonl.py [-h] input_file output_dir output_file
create-jsonl.py: error: the following arguments are required: input_file, output_dir, output_file

$ python ./data/stage3/combine-jsonl.py
usage: combine-jsonl.py [-h] directory_path output_file
combine-jsonl.py: error: the following arguments are required: directory_path, output_file
```

```bash
$ python ./data/stage2/create-jsonl.py ./data/stage1/scrape-results1.csv ./data/stage2 scrape-results1.jsonl
2024-05-21 03:33:50 [info     ] CSV processing complete        output_file=data/stage2/scrape-results1.jsonl

$ python ./data/stage3/combine-jsonl.py ./data/stage2 ./data/stage3/final.jsonl
2024-05-21 03:36:42 [info     ] Merged JSONL files             output_file=./data/stage3/final.jsonl
```
