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

### To train with TIMM
```
silver_train model="timm.yaml" 
```
The latest checkpoint is saved as `./save.ckpt`

### To evaluate with TIMM
```
silver_eval model="timm.yaml" ckpt_path="./save.ckpt"
```