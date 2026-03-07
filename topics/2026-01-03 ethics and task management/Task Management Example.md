# Example project -- make dan coffee

tasks:

|done? | name      |  length| depends on              |
|:----:|-----------|-------:|-------------------------|
| [ ]  |Dry beans  |      2d|                         |
| [ ]  |Roast beans|     30m|Dry beans                |
| [ ]  |Grind beans|      1m|Roast beans              |
| [ ]  |Boil water |      1m|                         |
| [ ]  |Strain     |      1m|Grind beans + Boil water |

- This works best if we start boiling water at the same time we start grinding beans.
- At best, we get coffee in 2d, 32m.
