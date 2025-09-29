### union

Combine two geometries into their union.

- Tool: `union`
- Geometry format: WKT

Parameters

- geometry1 (string)
- geometry2 (string)

Returns

- geometry (string, WKT)
- status (string), message (string)

Example

```json
{
  "tool": "union",
  "params": {
    "geometry1": "POLYGON((0 0,10 0,10 10,0 10,0 0))",
    "geometry2": "POLYGON((5 5,15 5,15 15,5 15,5 5))"
  }
}
```
