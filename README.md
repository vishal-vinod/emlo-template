# Lightning Template

```
silver_train --help
```

## Development

Install in dev mode

```
pip install -e .
```

### Run
```
silver_train data.num_workers=16
```
The latest checkpoint is saved as `./save.ckpt`

### Eval
```
silver_eval data.num_workers=16 ckpt_path="./save.ckpt"
```