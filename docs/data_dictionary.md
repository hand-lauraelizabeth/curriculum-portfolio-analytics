# Data Dictionary

All data in this repository are synthetic and created solely for demonstration.

| Field | Type | Description |
| --- | --- | --- |
| product_id | string | Synthetic learning-product identifier. |
| title | string | Synthetic product title. |
| topic | string | High-level curriculum topic. |
| format | string | Learning-product format such as Micro, Burst, Half-Day, Full-Day, or Mastery. |
| delivery_mode | string | Virtual or In Person. |
| lifecycle_stage | string | Portfolio stage: Active, Pilot, or Refresh. |
| launch_date | date | Synthetic initial launch date. |
| registrations | integer | Synthetic registration count. |
| attendees | integer | Synthetic attendee count. |
| completion_rate | float | Synthetic completion rate from 0 to 1. |
| satisfaction_score | float | Synthetic learner satisfaction score on a 1 to 5 scale. |
| last_refresh_date | date | Synthetic most recent substantive refresh date. |

## Derived metrics

**Attendance rate**  
`attendees / registrations`

**Utilization score**  
A demonstration score that combines normalized registrations, attendance rate, completion rate, and satisfaction.

**Refresh age**  
Months between `last_refresh_date` and the analysis reference date.

**Refresh candidate**  
A demonstration flag for products already marked Refresh or products with weak utilization signals and an older refresh date.

## Interpretation

These fields are intentionally generalized. They demonstrate how a curriculum portfolio can be modeled for analysis without reproducing a real organization's proprietary product taxonomy, thresholds, or performance data.
