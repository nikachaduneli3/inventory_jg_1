## Models

1. BaseModel
   - create_date : Datetime : auto_now_add 
   - write_date : Datetime : auto_now
   - archived : Boolean : default False
2. Item
    - name : CharField
    - description : TextField
    - price : FloatField
    - stock_qty : PositiveInteger
    - height : PositiveInteger : nullable
    - width : PositiveInteger : nullable
    - weight : PositiveInteger : nullable
    - barcode : Char (11 digit symbol auto generated) unique
    - expiration_date : DateField
    - category m2o -> Category

3. Category
   - name : CharField


## Endpoints

- 'items/' GET
- 'items/' POST
- 'items/<int:id>' GET
- 'items/<int:id>' PUT
- 'items/<int:id>' PATCH
- 'items/<int:id>' DELETE
- 'categories/' GET
- 'categories/' POST
- 'categories/<int:pk>' GET
- 'categories/<int:pk>' PUT
- 'categories/<int:pk>' PATCH
- 'categories/<int:pk>' DELETE

