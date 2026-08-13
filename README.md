# MetPro Adapt — Functional V1 Prototype

A standalone Streamlit prototype for the single-page MetPro Adapt intake interface.

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Streamlit Community Cloud

Create a new app pointing to `app.py` in this folder/repository. This prototype is intentionally separate from any previous MetPro Streamlit app.

## Prototype behavior

- One-time profile setup; saved in browser `localStorage` for the prototype.
- Profile remains editable by tapping the MetPro avatar after setup.
- Editable Weight / Body Comp / Protein tiles.
- Adaptive Intake Levels 1–5.
- Protein and carbs: one ±15g micro-adjustment from the selected level baseline.
- Fat: one ±5g micro-adjustment, with 50–75g guardrails.
- Phase changes reset all micro-adjustments.
- Personalized protein and carbohydrate calculations based on the agreed MetPro Adapt rules.
- Low-weight-for-height protection silently restricts lower phases and minus adjustments.

## Note

This is a product prototype, not medical software. The body-composition categories and calibration rules are MetPro wellness-program logic.
