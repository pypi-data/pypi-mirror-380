# Workflow

``` mermaid
flowchart TD
    A[TCX File] -->|Instantiate| B(TCX2GPX)
    B --> C[Read File]
    C --> D[Extract Track Points]
    D --> E[Create GPX]
    E --> G(Extract Track Name)
    G --> H(Extract Activity)
    H --> I(Append GPX Trackpoints)
    I --> F
    E -...- F[Write GPX]

```
