# MetPro Adapt — Locked V1 Rules

## Scope
- Standalone Streamlit prototype; prior MetPro app remains untouched.
- One primary Adaptive Intake screen plus a one-time profile/setup screen.
- No automated cutting/revving cycle logic in V1. Users self-select intake level and micro-adjustments.

## Visual / UX anchor
- Premium Apple-clean white interface.
- Navy typography; blue protein, red carbs, orange fat.
- Small animated MetPro intelligence avatar.
- Compact Weight / Body Comp / Protein tiles.
- Label: **Adaptive Intake Level**.
- Phase 3 is the visual/default middle and Balanced is the recommended protein setting.

## Profile
- First-use Complete Profile prompt collects age, sex, height, and weight.
- Once saved, the prompt disappears from the main screen.
- Tap the MetPro avatar to edit profile later.
- Weight remains directly editable from the main Weight tile.

## Body composition
Program categories (not medical diagnoses):
- Lower = 100% of body weight participates in protein calculation.
- Moderate = 95%.
- Higher = 85%.

If optional body-fat percentage is supplied, prototype category thresholds are:
- Male: Lower <20%; Moderate 20–29.9%; Higher ≥30%.
- Female: Lower <30%; Moderate 30–41.9%; Higher ≥42%.

## Protein
Demand settings:
- Moderate = 0.5 g/lb.
- Balanced = 0.7 g/lb (Recommended).
- Performance = 0.9 g/lb.

Calculation:
1. Adjusted weight = body weight × body-comp factor.
2. Protein calculation weight = min(adjusted weight, 300 lb).
3. Phase-3 target = calculation weight × selected protein factor.
4. Round to nearest 5g.

Phase protein:
- Moderate: P1=P2=P3=target; P4=target+10g; P5=target+15g.
- Balanced/Performance: P1=P2=target−5g; P3=target; P4=target+10g; P5=target+15g.
- Never allow protein below the rounded 0.5 g/lb algorithmic floor.
- Absolute protein ceiling: 290g/day.

Micro adjustment:
- Protein ±15g, one step either direction from the selected level baseline.
- Controls gray out when the lower floor or 290g ceiling would be violated.

## Carbohydrate
Base phase carbs:
- P1 120g
- P2 145g
- P3 160g
- P4 220g
- P5 300g

Body-weight modifier:
- ≤140 lb: +0g.
- 140–200 lb: +0.5g per lb above 140.
- >200 lb: +30g plus +0.25g per lb above 200.
- Round final carb target to nearest 5g.

Micro adjustment:
- Carbs ±15g, one step either direction from the phase baseline.

## Fat
Base phase fat:
- P1 55g
- P2 55g
- P3 60g
- P4 65g
- P5 70g

Micro adjustment:
- Fat ±5g, one step either direction.
- Hard operating corridor: 50–75g.

## Phase behavior
- User can tap 1–5 or use the large − / + controls.
- Changing phase resets all macro micro-adjustments to zero.
- Macro bars are visual only.
- Calories, macro ratio, and total macro grams update live.

## Low-weight-for-height protection
- No universal 100-lb minimum.
- Height and age are collected in profile so low-weight-for-height can be recognized at any body weight.
- Adults 20+:
  - BMI 17.0–18.49: Phase 3 is the lowest available phase; P1/P2 locked; all macro − controls disabled.
  - BMI <17.0: Phase 4 is the lowest available phase; P1/P2/P3 locked; all macro − controls disabled.
- Ages 18–19: use sex-specific CDC BMI-for-age underweight screening; when triggered, use the stronger protection state (Phase 4 floor and all macro − controls disabled).
- Protection is self-contained; there is no coach/clinician escalation workflow in the prototype.
- + adjustments remain available subject to the normal macro guardrails.
