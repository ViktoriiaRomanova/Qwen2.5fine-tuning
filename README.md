 
# Fine-tuning Qwen2.5-VL for Visual Watermark & Content Extraction

This project fine-tunes the **Qwen2.5-VL** vision-language model to process images and extract structured information in **JSON format**.  
The model is trained to detect and describe:  

- **Watermarks** (count)  
- **Text** (OCR-like extraction)  
- **Main object** (primary entity in the image)  
- **Style** (artistic or visual style)  

---

## 🚀 Model Input / Output

### Input
- **Image** (`.png`, `.jpg`, `.jpeg`)  

### Output (JSON)
```json
{
  "watermarks": "int",
  "text": "str",
  "main object": "str",
  "style": "str"
}
```

Example:
```json
{
  "watermarks": 2,
  "text": "Confidential",
  "main object": "laptop",
  "style": "minimalist"
}
```

---

## 📊 Training Results

The fine-tuned model achieved the following metrics:

| Metric                          | Value   |
|---------------------------------|---------|
| **Watermarks Accuracy**         | 0.901   |
| **Watermarks MAE**              | 0.101   |
| **Text Levenshtein Distance**   | 2.297   |
| **Main Object BERTScore**       | 0.874   |
| **Style BERTScore**             | 0.918   |

## Framework versions

- PEFT 0.17.1
- TRL: 0.24.0.dev0
- Transformers: 4.56.2
- Pytorch: 2.8.0
- Datasets: 4.1.1
- Tokenizers: 0.22.1