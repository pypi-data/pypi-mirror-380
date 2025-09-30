<p align="center">
  <img src="builder-ui/public/logo.png" alt="Polymo" width="220">
</p>

Polymo makes it easy to read REST APIs into Spark DataFrames. 
Just a config file and read it with Spark.

## Quick start

1. Define a config file:

   ```yaml
   version: 0.1
   source:
     type: rest
     base_url: https://jsonplaceholder.typicode.com
   stream:
     path: /posts
     params:
       _limit: 20
     infer_schema: true
   ```

2. Register the source and read data:

   ```python
   from pyspark.sql import SparkSession
   from polymo import ApiReader 

   spark = SparkSession.builder.getOrCreate()
   spark.dataSource.register(ApiReader)

   df = (
       spark.read.format("polymo")
       .option("config_path", "./config.yml")
       .option("token", "<YOUR_BEARER_TOKEN>")  
       .load()
   )
   ```

## Builder UI

Want a friendly way to craft configs? Launch the local builder:

```bash
polymo builder --port 9000
```

# Installation
Base version without spark and builder:

`pip install polymo`

For builder UI:

`pip install 'polymo[builder]'` 

- Incremental cursors, partitioning, and advanced pagination strategies are on the roadmap.

Contributions and early feedback welcome!
