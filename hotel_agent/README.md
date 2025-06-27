## サンプルテーブル作成

```sql
CREATE TABLE IF NOT EXISTS
  `${your_dataset}.hotels` ( id INT64 NOT NULL,
    name STRING NOT NULL,
    location STRING NOT NULL,
    price_tier STRING NOT NULL,
    checkin_date DATE NOT NULL,
    checkout_date DATE NOT NULL,
    booked BOOLEAN NOT NULL );
INSERT INTO
  `${your_dataset}.hotels` (id,
    name,
    location,
    price_tier,
    checkin_date,
    checkout_date,
    booked)
VALUES
  (1, 'Hilton Basel', 'Basel', 'Luxury', '2024-04-20', '2024-04-22', FALSE),
  (2, 'Marriott Zurich', 'Zurich', 'Upscale', '2024-04-14', '2024-04-21', FALSE),
  (3, 'Hyatt Regency Basel', 'Basel', 'Upper Upscale', '2024-04-02', '2024-04-20', FALSE),
  (4, 'Radisson Blu Lucerne', 'Lucerne', 'Midscale', '2024-04-05', '2024-04-24', FALSE),
  (5, 'Best Western Bern', 'Bern', 'Upper Midscale', '2024-04-01', '2024-04-23', FALSE),
  (6, 'InterContinental Geneva', 'Geneva', 'Luxury', '2024-04-23', '2024-04-28', FALSE),
  (7, 'Sheraton Zurich', 'Zurich', 'Upper Upscale', '2024-04-02', '2024-04-27', FALSE),
  (8, 'Holiday Inn Basel', 'Basel', 'Upper Midscale', '2024-04-09', '2024-04-24', FALSE),
  (9, 'Courtyard Zurich', 'Zurich', 'Upscale', '2024-04-03', '2024-04-13', FALSE),
  (10, 'Comfort Inn Bern', 'Bern', 'Midscale', '2024-04-04', '2024-04-16', FALSE);
```

## Toolboxの設定ファイル

`tools.yml`

```yml
sources:
  my-bigquery-source:
    kind: bigquery
    project: ${your_project}
    location: asia-northeast1
toolsets:
  my-toolset:
    - search-hotels-by-name
    - search-hotels-by-location
tools:
  search-hotels-by-name:
    kind: bigquery-sql
    source: my-bigquery-source
    description: Search for hotels based on name.
    parameters:
      - name: name
        type: string
        description: The name of the hotel.
    statement: SELECT * FROM `${your_dataset}.hotels` WHERE LOWER(name) LIKE LOWER(CONCAT('%', @name, '%'));
  search-hotels-by-location:
    kind: bigquery-sql
    source: my-bigquery-source
    description: Search for hotels based on location.
    parameters:
      - name: location
        type: string
        description: The location of the hotel.
    statement: SELECT * FROM `${your_dataset}.hotels` WHERE LOWER(location) LIKE LOWER(CONCAT('%', @location, '%'));
```
