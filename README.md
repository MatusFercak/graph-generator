# 📈 Python Graph genration Function

Generate a graph using only the specified URL and parameters.

## 🧰 Usage

### GET /graph.png

**URL Parameters**

| Name      | Description           | Location     | Type   | Sample Value                |
| --------- | --------------------- | ------------ | ------ | --------------------------- |
| `x`       | Values of x-axis.     | Query string | csv    | `1,2,3,4,5,6,7,8`           |
| `y`       | Values of y-axis.     | Query string | csv    | `1,2,3.5,4,2.1,1.2,2.5,3.2` |
| `x_type`  | Type of values in `x` | Query string | String | `num`                       |
| `y_type`  | Type of values in `y` | Query string | String | `num`                       |
| `x_label` | Label for x-axis      | Query string | String | `X_label`                   |
| `y_label` | Label for y-axis      | Query string | String | `Y_label`                   |
| `title`   | Graph title           | Query string | String | `X_label`                   |

You can use the function with parameters provided in the request body, except for the change in the `x` and `y` attributes, where we insert arrays ( lists ).

**Sample URL:**
`https://65196d46cc349ea4b149.appwrite.global/graph.png?x=1,2,3,4,5,6,7,8&y=1,2,3.5,4,2.1,1.2,2.5,3.2&x_type=num&y_type=num&x_label=X_label&y_label=Y_Label&title=Graph_titl`

**Sample `200` Response.**

![Graph](https://65196d46cc349ea4b149.appwrite.global/graph.png?x=1,2,3,4,5,6,7,8&y=1,2,3.5,4,2.1,1.2,2.5,3.2&x_type=num&y_type=num&x_label=X_label&y_label=Y_Label&title=Graph_title)

**Sample `400` Response.**

```json
	{
		"ok":  False,
		"error":  "ErrorMessage: --//--"
	}
```

**Sample `405` Response.**
Response when the request method was POST, PUT, PATCH, DELETE

```json
	{
		"ok":  False,
		"message":  "Try GET method and follow instruction -> https://github.com/MatusFercak/graf-generator"
	}
```

## ⚙️ Configuration

| Setting           | Value                             |
| ----------------- | --------------------------------- |
| Runtime           | Python (3.9)                      |
| Entrypoint        | `src/main.py`                     |
| Build Commands    | `pip install -r requirements.txt` |
| Permissions       | `any`                             |
| Timeout (Seconds) | 15                                |

## 🔒 Environment Variables

No environment variables required.
