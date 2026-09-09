# Global Common Parameters

**Global Header Parameters**

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| No parameters |

**Global Query Parameters**

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| No parameters |

**Global Body Parameters**

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| No parameters |

**Global Authentication Method**

> No authentication required

# Status Code Description

| Status Code | Description |
| --- | ---- |
| No parameters |

# Public Infomation

> Created by: Timesup

> Updated by: Timesup

> Created at: 2024-06-27 05:13:01

> Updated at: 2024-08-20 05:32:48

## Server URL：

**All APIs need to be prefixed with server URL： https://shine-api.felicitysolar.com,For example：
    API Refresh Token，URI is '/openApi/sec/refreshToken' , When calling this API, the complete URL is 'https://shine-api.felicitysolar.com/openApi/sec/refreshToken'**

**Query**

# User-related

> Created by: chh

> Updated by: typhoon

> Created at: 2024-06-20 04:26:41

> Updated at: 2024-06-27 03:43:43

```text
No description
```

**Directory Header Parameters**

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| No parameters |

**Directory Query Parameters**

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| No parameters |

**Directory Body Parameters**

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| No parameters |

**Directory Authentication Info**

> Inherit from parent

**Query**

## Refresh Token

> Created by: chh

> Updated by: chh

> Created at: 2024-06-20 04:26:45

> Updated at: 2024-08-20 08:54:43

**This endpoint allows you to refresh the authentication token by passing the refresh token obtained from the login endpoint as a parameter.,If the refresh token expires, you need to log in again.,error code**

| code | [object Object] |
| ---- | -- |
| 999 | You need to log in again. |
| 1002001 | Account not activated; please contact the administrator. |

**Interface Status**

> Completed

**Interface URL**

> /openApi/sec/refreshToken

**Request Method**

> POST

**Content-Type**

> json

**Request Body Parameters**

```javascript
{
	"refreshToken": "Bearer_eyJhbGciOiJIUzI1NiJ9.eyJpZCI6OTAyMTE1NDA0NDk4ODg5NiwiaWF0IjoxNzE4ODYzODM0fQ._dSC4TGSdeBrK7fbpHcijo23GohZcOK4SMUirToHP9811"
}
```

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| refreshToken | - | string | Yes | Refresh Token |

**Authentication Method**

> Inherit from parent

**Response Example**

* Success(200)

```javascript
{
	"code": 200,
	"message": "Success",
	"data": {
		"token": "Bearer_eyJhbGciOiJIUzI1NiJ9.eyJkZW1vVXNlciI6ZmFsc2UsInN1YiI6Iui-o-akkiIsImF1ZCI6Ik9UQXlNVEUxTkRBME5EazRPRGc1Tmc9PSIsIm5iZiI6MTcxODg2NDIxOSwiaXNzIjoiRkxTLVNPTEFSLVNFUlZFUiIsImlkIjo5MDIxMTU0MDQ0OTg4ODk2LCJleHAiOjE3MjE0NTYyMTksImlhdCI6MTcxODg2NDIxOX0.T_uFdGuJJm2bssgTiHTRuzpRv17q7_sgYkOraAFdXBk",
		"tokenExpireTime": "1721456219000",
		"refreshToken": "Bearer_eyJhbGciOiJIUzI1NiJ9.eyJpZCI6OTAyMTE1NDA0NDk4ODg5NiwiaWF0IjoxNzE4ODYzODM0fQ._dSC4TGSdeBrK7fbpHcijo23GohZcOK4SMUirToHP98",
		"refTokenExpireTime": "1724047834012"
	}
}
```

| Parameter Name | Example Value | Parameter Type | Description |
| --- | --- | ---- | ---- |
| code | 200 | number | Response code |
| message | Success | string | Response message body |
| data | - | object | Returned data |
| data.token | Bearer_eyJhbGciOiJIUzI1NiJ9.eyJkZW1vVXNlciI6ZmFsc2UsInN1YiI6Iui-o-akkiIsImF1ZCI6Ik9UQXlNVEUxTkRBME5EazRPRGc1Tmc9PSIsIm5iZiI6MTcxODg2NDIxOSwiaXNzIjoiRkxTLVNPTEFSLVNFUlZFUiIsImlkIjo5MDIxMTU0MDQ0OTg4ODk2LCJleHAiOjE3MjE0NTYyMTksImlhdCI6MTcxODg2NDIxOX0.T_uFdGuJJm2bssgTiHTRuzpRv17q7_sgYkOraAFdXBk | string | Authentication token |
| data.tokenExpireTime | 1721456219000 | string | Authentication token expiration time (timestamp) |
| data.refreshToken | Bearer_eyJhbGciOiJIUzI1NiJ9.eyJpZCI6OTAyMTE1NDA0NDk4ODg5NiwiaWF0IjoxNzE4ODYzODM0fQ._dSC4TGSdeBrK7fbpHcijo23GohZcOK4SMUirToHP98 | string | Refresh token |
| data.refTokenExpireTime | 1724047834012 | string | Refresh token expiration time |

* Fail(201)

```javascript
{
	"code": 998,
	"message": "The token has expired, please log in again",
	"data": "The token has expired, please log in again"
}
```

| Parameter Name | Example Value | Parameter Type | Description |
| --- | --- | ---- | ---- |
| code | 998 | number | Response Code |
| message | The token has expired, please log in again | string | Response Message Body |
| data | The token has expired, please log in again | string | Returned Data |

**Query**

## login

> Created by: chh

> Updated by: Timesup

> Created at: 2024-06-20 04:08:40

> Updated at: 2025-03-03 13:07:45

**1.First, We need to encrypt the password for transmission using the RSA algorithm.The steps are as follows：,1.1 Use the plaintext password (account password) and the public Key provided by fSolar to compute the encrypted password using the RSA algorithm.
1.2 Use the encrypted password to fill the password field in the login interface, and provide the correct username. Request the login interface to obtain the token.
1.3 When accessing other interfaces, fill in the parameters according to the interface documentation and include the required token. This will allow you to access the interfaces.,Public key
MFwwDQYJKoZIhvcNAQEBBQADSwAwSAJBAK0GDivaRzIKeTmQnAxAYh2LChuHWDp0yHZ0zIvm+Eoi7J+rx7phqR7EtkBDO3HWqAXVkNDeeQaU32P5w1Q4FVUCAwEAAQ==**

```
MFwwDQYJKoZIhvcNAQEBBQADSwAwSAJBAK0GDivaRzIKeTmQnAxAYh2LChuHWDp0yHZ0zIvm+Eoi7J+rx7phqR7EtkBDO3HWqAXVkNDeeQaU32P5w1Q4FVUCAwEAAQ==
```

**Java encryption example**

```java
public static void main(String[] args) throws Exception {
        String password = "8888888";
        //public key
        String publicKeyStr = "MFwwDQYJKoZIhvcNAQEBBQADSwAwSAJBAK0GDivaRzIKeTmQnAxAYh2LChuHWDp0yHZ0zIvm+Eoi7J+rx7phqR7EtkBDO3HWqAXVkNDeeQaU32P5w1Q4FVUCAwEAAQ==";

        PublicKey publicKey = KeyFactory.getInstance("RSA")
                .generatePublic(new X509EncodedKeySpec(Base64.getDecoder().decode(publicKeyStr)));

        // encrypt data using a public key
        Cipher encryptCipher = Cipher.getInstance("RSA");
        encryptCipher.init(Cipher.ENCRYPT_MODE, publicKey);
        byte[] encryptedBytes = encryptCipher.doFinal(password.getBytes());
        System.out.println("encrypted data: " + Base64.getEncoder().encodeToString(encryptedBytes));
    }
```

**error code**

| code | [object Object] |
| ---- | -- |
| 1002006 | Wrong password |

**Interface Status**

> Completed

**Interface URL**

> /openApi/sec/login

**Request Method**

> POST

**Content-Type**

> json

**Request Body Parameters**

```javascript
{
	"password": "KnihfiVSe7WGt43EtmMGfkbPorIPLitSo5Ue3PkoxO1CP1GOusglHRLmvHKnNXTLIhrV1n3o2nfrBfJSKizNkg==",
	"userName": "11@qq.com"
}
```

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| password | - | string | Yes | password |
| userName | - | string | Yes | username:ps:The account is provided by our company |

**Authentication Method**

> Inherit from parent

**Response Example**

* Success(200)

```javascript
{
	"code": 200,
	"message": "Success",
	"data": {
		"token": "Bearer_eyJhbGciOiJIUzI1NiJ9.eyJkZW1vVXNlciI6ZmFsc2UsInN1YiI6Iui-o-akkiIsImF1ZCI6Ik9UQXlNVEUxTkRBME5EazRPRGc1Tmc9PSIsIm5iZiI6MTcxODg2NDIxOSwiaXNzIjoiRkxTLVNPTEFSLVNFUlZFUiIsImlkIjo5MDIxMTU0MDQ0OTg4ODk2LCJleHAiOjE3MjE0NTYyMTksImlhdCI6MTcxODg2NDIxOX0.T_uFdGuJJm2bssgTiHTRuzpRv17q7_sgYkOraAFdXBk",
		"tokenExpireTime": "1721456219000",
		"refreshToken": "Bearer_eyJhbGciOiJIUzI1NiJ9.eyJpZCI6OTAyMTE1NDA0NDk4ODg5NiwiaWF0IjoxNzE4ODYzODM0fQ._dSC4TGSdeBrK7fbpHcijo23GohZcOK4SMUirToHP98",
		"refTokenExpireTime": "1724047834008"
	}
}
```

| Parameter Name | Example Value | Parameter Type | Description |
| --- | --- | ---- | ---- |
| code | 200 | number | code |
| message | Success | string | message |
| data | - | object | data |
| data.token | Bearer_eyJhbGciOiJIUzI1NiJ9.eyJkZW1vVXNlciI6ZmFsc2UsInN1YiI6Iui-o-akkiIsImF1ZCI6Ik9UQXlNVEUxTkRBME5EazRPRGc1Tmc9PSIsIm5iZiI6MTcxODg2NDIxOSwiaXNzIjoiRkxTLVNPTEFSLVNFUlZFUiIsImlkIjo5MDIxMTU0MDQ0OTg4ODk2LCJleHAiOjE3MjE0NTYyMTksImlhdCI6MTcxODg2NDIxOX0.T_uFdGuJJm2bssgTiHTRuzpRv17q7_sgYkOraAFdXBk | string | Authentication token |
| data.tokenExpireTime | 1721456219000 | TimeStamp | Authentication token expiration time |
| data.refreshToken | Bearer_eyJhbGciOiJIUzI1NiJ9.eyJpZCI6OTAyMTE1NDA0NDk4ODg5NiwiaWF0IjoxNzE4ODYzODM0fQ._dSC4TGSdeBrK7fbpHcijo23GohZcOK4SMUirToHP98 | string | Refresh authentication token |
| data.refTokenExpireTime | 1724047834008 | TimeStamp | Refresh authentication token expiration time |

* Fail(201)

```javascript
{
  "code": 1002006,
  "message": "Wrong password",
  "data": "Wrong password"
}
```

| Parameter Name | Example Value | Parameter Type | Description |
| --- | --- | ---- | ---- |
| code | 1002006 | number | code |
| message | Wrong password | string | message |
| data | Wrong password | string | data |

**Query**

# Device Data

> Created by: chh

> Updated by: Timesup

> Created at: 2024-06-20 08:31:59

> Updated at: 2024-06-26 15:38:24

```text
No description
```

**Directory Header Parameters**

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| No parameters |

**Directory Query Parameters**

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| No parameters |

**Directory Body Parameters**

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| No parameters |

**Directory Authentication Info**

> Inherit from parent

**Query**

## Energy data query for year, month, day

> Created by: chh

> Updated by: Timesup

> Created at: 2024-06-20 08:32:45

> Updated at: 2024-06-27 05:07:38

**This endpoint adjusts the response data based on the timeDimension parameter. Depending on whether it's set to day, month, year, or total, the data values in the response vary accordingly.**

**Interface Status**

> Completed

**Interface URL**

> /openApi/data/deviceDataEnergy

**Request Method**

> GET

**Content-Type**

> form-data

**Request Header Parameters**

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| Authorization | Bearer_eyJhbGciOiJIUzI1NiJ9.eyJkZW1vVXNlciI6ZmFsc2UsInN1YiI6Iui-o-akkiIsImF1ZCI6Ik9UQXlNVEUxTkRBME5EazRPRGc1Tmc9PSIsIm5iZiI6MTcxODg2NDIxOSwiaXNzIjoiRkxTLVNPTEFSLVNFUlZFUiIsImlkIjo5MDIxMTU0MDQ0OTg4ODk2LCJleHAiOjE3MjE0NTYyMTksImlhdCI6MTcxODg2NDIxOX0.T_uFdGuJJm2bssgTiHTRuzpRv17q7_sgYkOraAFdXBk | string | Yes | authentication token |

**Request Body Parameters**

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| deviceSn | 020505004822242582 | string | Yes | device Sn |
| timeDimension | day | string | Yes | Query dimension :day month year total |
| dateStr | - | string | No | Query time: (yyyy-MM-dd HH:mm:ss) |
| pageNum | 1 | number | Yes | Page number (default 1) |
| pageSize | 10 | number | Yes | PageSize，The maximum value is 300 |

**Authentication Method**

> Inherit from parent

**Response Example**

* Success(200)

```javascript
{
	"code": 200,
	"message": "Success",
	"data": {
		"records": [
			{
				"deviceSn": "020505004822242582",
				"dataTime": "2023-04-03",
				"timeStamp": 1680451200000,
				"gridInput": null,
				"feedOutput": null,
				"generateEnergy": null,
				"inversionEnergy": null,
				"batCharEnergy": null,
				"bat2ChartEnergy": null,
				"batDisEnergy": null,
				"batDis2Energy": null,
				"pv1Energy": null,
				"pv2Energy": null,
				"pv3Energy": null,
				"pv4Energy": null,
				"genEnergy": null,
				"smartLoadEnergy": null,
				"offGridEnergy": null,
				"gridTiedEnergy": null,
				"offGridTiedEnergy": null
			},
			{
				"deviceSn": "020505004822242582",
				"dataTime": "2023-04-04",
				"timeStamp": 1680537600000,
				"gridInput": "0.26",
				"feedOutput": "0.22",
				"generateEnergy": "0.29",
				"inversionEnergy": null,
				"batCharEnergy": "0.39",
				"bat2ChartEnergy": null,
				"batDisEnergy": "0.25",
				"batDis2Energy": null,
				"pv1Energy": null,
				"pv2Energy": null,
				"pv3Energy": null,
				"pv4Energy": null,
				"genEnergy": null,
				"smartLoadEnergy": null,
				"offGridEnergy": "0.29",
				"gridTiedEnergy": null,
				"offGridTiedEnergy": "0.29"
			},
			{
				"deviceSn": "020505004822242582",
				"dataTime": "2023-04-06",
				"timeStamp": 1680710400000,
				"gridInput": "0.26",
				"feedOutput": "0.22",
				"generateEnergy": "0.29",
				"inversionEnergy": null,
				"batCharEnergy": "0.39",
				"bat2ChartEnergy": null,
				"batDisEnergy": "0.25",
				"batDis2Energy": null,
				"pv1Energy": null,
				"pv2Energy": null,
				"pv3Energy": null,
				"pv4Energy": null,
				"genEnergy": null,
				"smartLoadEnergy": null,
				"offGridEnergy": "0.29",
				"gridTiedEnergy": null,
				"offGridTiedEnergy": "0.29"
			},
			{
				"deviceSn": "020505004822242582",
				"dataTime": "2023-04-07",
				"timeStamp": 1680796800000,
				"gridInput": "0.26",
				"feedOutput": "0.22",
				"generateEnergy": "0.29",
				"inversionEnergy": null,
				"batCharEnergy": "0.39",
				"bat2ChartEnergy": null,
				"batDisEnergy": "0.25",
				"batDis2Energy": null,
				"pv1Energy": null,
				"pv2Energy": null,
				"pv3Energy": null,
				"pv4Energy": null,
				"genEnergy": null,
				"smartLoadEnergy": null,
				"offGridEnergy": "0.29",
				"gridTiedEnergy": null,
				"offGridTiedEnergy": "0.29"
			},
			{
				"deviceSn": "020505004822242582",
				"dataTime": "2023-04-14",
				"timeStamp": 1681401600000,
				"gridInput": "0",
				"feedOutput": "0",
				"generateEnergy": "0",
				"inversionEnergy": null,
				"batCharEnergy": "0",
				"bat2ChartEnergy": null,
				"batDisEnergy": "0",
				"batDis2Energy": null,
				"pv1Energy": null,
				"pv2Energy": null,
				"pv3Energy": null,
				"pv4Energy": null,
				"genEnergy": null,
				"smartLoadEnergy": null,
				"offGridEnergy": "0",
				"gridTiedEnergy": null,
				"offGridTiedEnergy": "0"
			},
			{
				"deviceSn": "020505004822242582",
				"dataTime": "2023-04-15",
				"timeStamp": 1681488000000,
				"gridInput": "0",
				"feedOutput": "0",
				"generateEnergy": "0",
				"inversionEnergy": null,
				"batCharEnergy": "0",
				"bat2ChartEnergy": null,
				"batDisEnergy": "0",
				"batDis2Energy": null,
				"pv1Energy": null,
				"pv2Energy": null,
				"pv3Energy": null,
				"pv4Energy": null,
				"genEnergy": null,
				"smartLoadEnergy": null,
				"offGridEnergy": "0",
				"gridTiedEnergy": null,
				"offGridTiedEnergy": "0"
			},
			{
				"deviceSn": "020505004822242582",
				"dataTime": "2023-04-17",
				"timeStamp": 1681660800000,
				"gridInput": "0",
				"feedOutput": "0",
				"generateEnergy": "0",
				"inversionEnergy": null,
				"batCharEnergy": "0",
				"bat2ChartEnergy": null,
				"batDisEnergy": "0",
				"batDis2Energy": null,
				"pv1Energy": null,
				"pv2Energy": null,
				"pv3Energy": null,
				"pv4Energy": null,
				"genEnergy": null,
				"smartLoadEnergy": null,
				"offGridEnergy": "0",
				"gridTiedEnergy": null,
				"offGridTiedEnergy": "0"
			},
			{
				"deviceSn": "020505004822242582",
				"dataTime": "2023-04-18",
				"timeStamp": 1681747200000,
				"gridInput": "0",
				"feedOutput": "0",
				"generateEnergy": "0",
				"inversionEnergy": null,
				"batCharEnergy": "0",
				"bat2ChartEnergy": null,
				"batDisEnergy": "0",
				"batDis2Energy": null,
				"pv1Energy": null,
				"pv2Energy": null,
				"pv3Energy": null,
				"pv4Energy": null,
				"genEnergy": null,
				"smartLoadEnergy": null,
				"offGridEnergy": "0",
				"gridTiedEnergy": null,
				"offGridTiedEnergy": "0"
			},
			{
				"deviceSn": "020505004822242582",
				"dataTime": "2023-04-19",
				"timeStamp": 1681833600000,
				"gridInput": "0",
				"feedOutput": "0",
				"generateEnergy": "0",
				"inversionEnergy": null,
				"batCharEnergy": "0",
				"bat2ChartEnergy": null,
				"batDisEnergy": "0",
				"batDis2Energy": null,
				"pv1Energy": null,
				"pv2Energy": null,
				"pv3Energy": null,
				"pv4Energy": null,
				"genEnergy": null,
				"smartLoadEnergy": null,
				"offGridEnergy": "0",
				"gridTiedEnergy": null,
				"offGridTiedEnergy": "0"
			},
			{
				"deviceSn": "020505004822242582",
				"dataTime": "2023-04-20",
				"timeStamp": 1681920000000,
				"gridInput": "0",
				"feedOutput": "0",
				"generateEnergy": "0",
				"inversionEnergy": null,
				"batCharEnergy": "0",
				"bat2ChartEnergy": null,
				"batDisEnergy": "0",
				"batDis2Energy": null,
				"pv1Energy": null,
				"pv2Energy": null,
				"pv3Energy": null,
				"pv4Energy": null,
				"genEnergy": null,
				"smartLoadEnergy": null,
				"offGridEnergy": "0",
				"gridTiedEnergy": null,
				"offGridTiedEnergy": "0"
			}
		],
		"total": 110,
		"size": 10,
		"current": 1,
		"orders": [],
		"optimizeCountSql": true,
		"hitCount": false,
		"searchCount": true,
		"pages": 11
	}
}
```

| Parameter Name | Example Value | Parameter Type | Description |
| --- | --- | ---- | ---- |
| code | 200 | number | Code |
| message | Success | string | Message |
| data | - | object | Return Data |
| data.records | - | object | records |
| data.records.deviceSn | 020505004822242582 | string | Device serial number |
| data.records.dataTime | 2023-04-03 | string | Data time |
| data.records.timeStamp | 1680451200000 | number | Device time (timestamp) converted based on UTC+8 time zone |
| data.records.gridInput | - | Double | Grid input Energy (kWh) |
| data.records.feedOutput | - | Double | Grid feed Energy (kWh) |
| data.records.generateEnergy | - | Double | Power generation |
| data.records.inversionEnergy | - | Double | Inversion Energy |
| data.records.batCharEnergy | - | Double | Battery charge energy(kWh) |
| data.records.bat2ChartEnergy | - | Double | Battery2 charge energy(kWh) |
| data.records.batDisEnergy | - | Double | Battery discharge energy(kWh) |
| data.records.batDis2Energy | - | Double | Battery2 discharge energy(kWh) |
| data.records.pv1Energy | - | Double | pv1 Energy |
| data.records.pv2Energy | - | Double | pv2 Energy |
| data.records.pv3Energy | - | Double | pv3 Energy |
| data.records.pv4Energy | - | Double | pv4 Energy |
| data.records.genEnergy | - | Double | generator Energy |
| data.records.smartLoadEnergy | - | Double | Smart Load Energy |
| data.records.offGridEnergy | - | Double | Back up load Energy |
| data.records.gridTiedEnergy | - | Double | Home load Energy |
| data.total | 110 | number | Total page |
| data.size | 10 | number | Page size |
| data.current | 1 | number | Current page |
| data.orders | {} | object | - |
| data.optimizeCountSql | true | string | - |
| data.hitCount | false | string | - |
| data.searchCount | true | string | - |
| data.pages | 11 | number | - |

* Fail(201)

```javascript
No data
```

**Request Header Parameters**

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| Authorization | Bearer_eyJhbGciOiJIUzI1NiJ9.eyJkZW1vVXNlciI6ZmFsc2UsInN1YiI6Iui-o-akkiIsImF1ZCI6Ik9UQXlNVEUxTkRBME5EazRPRGc1Tmc9PSIsIm5iZiI6MTcxODg2NDIxOSwiaXNzIjoiRkxTLVNPTEFSLVNFUlZFUiIsImlkIjo5MDIxMTU0MDQ0OTg4ODk2LCJleHAiOjE3MjE0NTYyMTksImlhdCI6MTcxODg2NDIxOX0.T_uFdGuJJm2bssgTiHTRuzpRv17q7_sgYkOraAFdXBk | string | Yes | authentication token |

**Query**

## Device Basic Data Query

> Created by: Timesup

> Updated by: Timesup

> Created at: 2024-06-22 04:19:50

> Updated at: 2024-06-27 03:10:36

**The application server can call this interface to query device basic information through the Fsolar platform.**

**Interface Status**

> Completed

**Interface URL**

> /openApi/data/deviceDataBasic/{deviceSn}

**Request Method**

> GET

**Content-Type**

> form-data

**Request Header Parameters**

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| Content-Type | application/x-www-form-urlencoded | string | Yes | - |
| Authorization | Bearer_eyJhbGciOiJIUzI1NiJ9.eyJkZW1vVXNlciI6ZmFsc2UsInN1YiI6IueuoeeQhuWRmCIsImF1ZCI6Ik56TTNORFF4TkRrd01UVTFPREUwTkE9PSIsIm5iZiI6MTcxMTY3NjY4NiwiaXNzIjoiRkxTLVNPTEFSLVNFUlZFUiIsImlkIjo3Mzc0NDE0OTAxNTU4MTQ0LCJleHAiOjE3MTQyNjg2ODYsImlhdCI6MTcxMTY3NjY4Nn0._l5VIYevtyv2Xc66S9w6fqmkECBFvLZPJYqjU07pObE | string | Yes | User token, which can be obtained from authentication and refreshing tokens. |
| Lang | en_US | string | Yes | Language, currently supports English en_US. |

**Path Variables**

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| deviceSn | 1 | string | Yes | Device serial number |

**Request Body Parameters**

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| deviceSn | - | string | Yes | Device serial number |

**Authentication Method**

> Inherit from parent

**Response Example**

* OK(200)

```javascript
{
	"code": 0,
	"message": "",
	"data": {
		"collectorSn": "",
		"controlVersion": "",
		"controlVersion2": "",
		"deviceModel": "",
		"deviceSn": "",
		"deviceType": "",
		"displayVersion": "",
		"firmwareVersion": "",
		"iapVersion": "",
		"moduleVersion": "",
		"ratedPower": "",
		"status": "",
		"subType": "",
		"type": ""
	}
}
```

| Parameter Name | Example Value | Parameter Type | Description |
| --- | --- | ---- | ---- |
| code | - | integer | Code |
| message | - | string | Message |
| data.collectorSn | - | string | Collector serial number |
| data.controlVersion | - | string | Control version number |
| data.controlVersion2 | - | string | Slave control version number |
| data.deviceModel | - | string | Device Model |
| data.deviceSn | - | string | Device serial number |
| data.deviceType | - | string | Device type: inverter: INV, battery pack: BP, others: Other |
| data.displayVersion | - | string | Display Version number |
| data.firmwareVersion | - | string | Firmware Version number |
| data.iapVersion | - | string | IAP Version number |
| data.moduleVersion | - | string | Collector Version number |
| data.ratedPower | - | number | Rated power |
| data.status | - | string | Device status: normal, alarm, offline, inventory |
| data.subType | - | string | Device Sub Type |
| data.type | - | string | Device Type |
| data | - | object | - |

* Unauthorized(401)

```javascript
No data
```

* Forbidden(403)

```javascript
No data
```

* Not Found(404)

```javascript
No data
```

**Request Header Parameters**

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| Content-Type | application/x-www-form-urlencoded | string | Yes | - |
| Authorization | Bearer_eyJhbGciOiJIUzI1NiJ9.eyJkZW1vVXNlciI6ZmFsc2UsInN1YiI6IueuoeeQhuWRmCIsImF1ZCI6Ik56TTNORFF4TkRrd01UVTFPREUwTkE9PSIsIm5iZiI6MTcxMTY3NjY4NiwiaXNzIjoiRkxTLVNPTEFSLVNFUlZFUiIsImlkIjo3Mzc0NDE0OTAxNTU4MTQ0LCJleHAiOjE3MTQyNjg2ODYsImlhdCI6MTcxMTY3NjY4Nn0._l5VIYevtyv2Xc66S9w6fqmkECBFvLZPJYqjU07pObE | string | Yes | User token, which can be obtained from authentication and refreshing tokens. |
| Lang | en_US | string | Yes | Language, currently supports English en_US. |

**Query**

## Historical real-time data query (single device)

> Created by: Timesup

> Updated by: chh

> Created at: 2024-06-22 04:19:50

> Updated at: 2024-08-14 11:48:16

**The application server can call this interface to query historical real-time data of a single device on the Fsolar platform.,For detailed explanation of response parameters, please refer to the following link
https://doc.apipost.net/docs/detail/2c65f6449c64000?target_id=81e8862bde00f**

**Interface Status**

> Completed

**Interface URL**

> /openApi/data/deviceDataHistory/{deviceSn}?dateStr=&pageNum=&pageSize=

**Request Method**

> GET

**Content-Type**

> form-data

**Request Header Parameters**

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| Authorization | - | string | Yes | Authorization token |

**Request Query Parameters**

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| dateStr | - | string | Yes | Date string, format: yyyy MM dd HH: mm: ss |
| pageNum | - | string | Yes | Page number (default 1) |
| pageSize | - | string | Yes | PageSize，The maximum value is 300 |

**Path Variables**

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| deviceSn | - | string | Yes | DeviceSN |

**Request Body Parameters**

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| dateStr | - | string | Yes | Date string, format: yyyy MM dd HH: mm: ss |
| deviceSn | - | string | Yes | Device serial number |
| pageNum | - | string | Yes | Page number (default 1) |
| pageSize | - | string | Yes | PageSize，The maximum value is 300 |

**Authentication Method**

> Inherit from parent

**Response Example**

* OK(200)

```javascript
Could you provide the link or specify what you're referring to：https://doc.apipost.net/docs/detail/2c65f6449c64000?target_id=81e8862bde00f
```

| Parameter Name | Example Value | Parameter Type | Description |
| --- | --- | ---- | ---- |
| data | - | object | Data |
| total | - | integer | Total number of records |
| totalPage | - | integer | Total Page |
| currentPage | - | integer | Current Page |
| pageSize | - | integer | Page Size |
| dataList.acRInCurr | - | number | Grid L1 Current |
| dataList.acRInFreq | - | number | Grid L1 Frequency |
| dataList.acRInPower | - | number | Grid L1 Power |
| dataList.acRInVolt | - | number | Grid L1 Voltage |
| dataList.acROutCurr | - | number | Backup Load L1 Current |
| dataList.acROutFreq | - | number | Backup Load L1 Frequency |
| dataList.acROutPower | - | number | Backup Load L1 Power |
| dataList.acROutVolt | - | number | Backup Load L1 Voltage |
| dataList.acSInCurr | - | number | Grid L2 Current |
| dataList.acSInFreq | - | number | Grid L2 Frequency |
| dataList.acSInPower | - | number | Grid L2 Power |
| dataList.acSInVolt | - | number | Grid L2 Voltage |
| dataList.acSOutCurr | - | number | Backup Load L2 Current |
| dataList.acSOutFreq | - | number | Backup Load L2 Frequency |
| dataList.acSOutPower | - | number | Backup Load L2 Power |
| dataList.acSOutVolt | - | number | Backup Load L2 Voltage |
| dataList.acTInCurr | - | number | Grid L3 Current |
| dataList.acTInFreq | - | number | Grid L3 Frequency |
| dataList.acTInPower | - | number | Grid L3 Power |
| dataList.acTInVolt | - | number | Grid L3 Voltage |
| dataList.acTOutCurr | - | number | Backup Load L3 Current |
| dataList.acTOutFreq | - | number | Backup Load L3 Frequency |
| dataList.acTOutPower | - | number | Backup Load L3 Power |
| dataList.acTOutVolt | - | number | Backup Load L3 Voltage |
| dataList.acTotalOutActPower | - | number | Total Backup Load Active Power |
| dataList.acTotalOutAppaPower | - | number | Total Backup Load Apparent Power(VA) |
| dataList.acTtlInpower | - | number | Total Grid Power(Negative value is the feeding power) |
| dataList.bmsFlag | - | boolean | Battery pack communication status |
| dataList.ctPower | - | number | External CT Power |
| dataList.devTempMax | - | number | Inverter Max Temp |
| dataList.devTempMin | - | number | Inverter Min Temp |
| dataList.deviceDataTime | - | string | Device data time string, format: yyyy-MM-dd HH:mm:ss |
| dataList.deviceSn | - | string | Device serial number |
| dataList.ebatCharTotal | - | number | Total battery charging(kWh) |
| dataList.ebatDischarTotal | - | number | Total battery discharge (kWh) |
| dataList.emsCurrent | - | number | Battery current (EMS) |
| dataList.emsPower | - | number | EMS power |
| dataList.emsSoc | - | number | EMS Soc |
| dataList.emsVoltage | - | number | Battery voltage (EMS) |
| dataList.epvToday | - | number | PV Power Today |
| dataList.meterPower | - | number | Home load power |
| dataList.pv2InCurr | - | number | PV2 Current |
| dataList.pv2Power | - | number | PV2 Power |
| dataList.pv2Volt | - | number | PV2 Voltage |
| dataList.pv3InCurr | - | number | PV3 current |
| dataList.pv3Power | - | number | PV3 power |
| dataList.pv3Volt | - | number | PV3 voltage |
| dataList.pvInCurr | - | number | PV1 Current |
| dataList.pvPower | - | number | PV1 Power |
| dataList.pvTotalPower | - | number | Total PV Power（pv1+pv2+pv3+pv4） |
| dataList.pvVolt | - | number | PV1 Voltage |
| dataList.tempMax | - | number | Maximum temperature of battery pack |
| dataList.tempMin | - | number | Minimum temperature of battery pack |
| dataList.timeZone | - | string | time zone |
| dataList.totalConsumPower | - | number | Total electricity consumption（backup load + home load） |
| dataList.totalEnergy | - | number | Total power generation |
| dataList.totalEnergyUnit | - | string | Total power generation unit |
| dataList.workMode | - | string | Work Model |

* Unauthorized(401)

```javascript
No data
```

* Forbidden(403)

```javascript
No data
```

* Not Found(404)

```javascript
No data
```

**Request Header Parameters**

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| Authorization | - | string | Yes | Authorization token |

**Query**

## Historical real-time data query (batch device)

> Created by: Timesup

> Updated by: chh

> Created at: 2024-06-22 04:19:50

> Updated at: 2024-08-14 11:48:25

**The application server can call this interface to query (batch devices) historical real-time data on the Fsolar platform.,For detailed explanation of response parameters, please refer to the following link.
https://doc.apipost.net/docs/detail/2c65f6449c64000?target_id=81e8862bde00f**

**Interface Status**

> Completed

**Interface URL**

> /openApi/data/devicesDataHistory?deviceSnList=100202000624170143,123123&endTime=&pageNum=&pageSize=&queryType=&startTime=

**Request Method**

> GET

**Content-Type**

> none

**Request Header Parameters**

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| Authorization | - | string | Yes | Authorization token |

**Request Query Parameters**

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| deviceSnList | 100202000624170143,123123 | string | Yes | Device serial number list, up to 50 |
| endTime | - | string | No | End time string, format: yyyy-MM-dd HH:mm:ss, required when queryType=1 |
| pageNum | - | string | No | Page number, starting from 1, mandatory when queryType=1 |
| pageSize | - | string | No | Number of entries per page, maximum value is 300, mandatory when queryType=1 |
| queryType | - | string | Yes | Query type, 0: Latest entry, 1: Page within half an hour |
| startTime | - | string | No | Starting time string, format: yyyy-MM-dd HH:mm:ss, required when queryType=1 |

**Authentication Method**

> Inherit from parent

**Response Example**

* OK(200)

```javascript
Could you provide the link or specify what you're referring to：https://doc.apipost.net/docs/detail/2c65f6449c64000?target_id=81e8862bde00f
```

| Parameter Name | Example Value | Parameter Type | Description |
| --- | --- | ---- | ---- |
| data | - | object | Data |
| total | - | integer | Total number of records |
| totalPage | - | integer | Total Page |
| currentPage | - | integer | Current Page |
| pageSize | - | integer | Page Size |
| dataList.acRInCurr | - | number | Grid L1 Current |
| dataList.acRInFreq | - | number | Grid L1 Frequency |
| dataList.acRInPower | - | number | Grid L1 Power |
| dataList.acRInVolt | - | number | Grid L1 Voltage |
| dataList.acROutCurr | - | number | Backup Load L1 Current |
| dataList.acROutFreq | - | number | Backup Load L1 Frequency |
| dataList.acROutPower | - | number | Backup Load L1 Power |
| dataList.acROutVolt | - | number | Backup Load L1 Voltage |
| dataList.acSInCurr | - | number | Grid L2 Current |
| dataList.acSInFreq | - | number | Grid L2 Frequency |
| dataList.acSInPower | - | number | Grid L2 Power |
| dataList.acSInVolt | - | number | Grid L2 Voltage |
| dataList.acSOutCurr | - | number | Backup Load L2 Current |
| dataList.acSOutFreq | - | number | Backup Load L2 Frequency |
| dataList.acSOutPower | - | number | Backup Load L2 Power |
| dataList.acSOutVolt | - | number | Backup Load L2 Voltage |
| dataList.acTInCurr | - | number | Grid L3 Current |
| dataList.acTInFreq | - | number | Grid L3 Frequency |
| dataList.acTInPower | - | number | Grid L3 Power |
| dataList.acTInVolt | - | number | Grid L3 Voltage |
| dataList.acTOutCurr | - | number | Backup Load L3 Current |
| dataList.acTOutFreq | - | number | Backup Load L3 Frequency |
| dataList.acTOutPower | - | number | Backup Load L3 Power |
| dataList.acTOutVolt | - | number | Backup Load L3 Voltage |
| dataList.acTotalOutActPower | - | number | Total Backup Load Active Power |
| dataList.acTotalOutAppaPower | - | number | Total Backup Load Apparent Power(VA) |
| dataList.acTtlInpower | - | number | Total Grid Power(Negative value is the feeding power) |
| dataList.bmsFlag | - | boolean | Battery pack communication status |
| dataList.ctPower | - | number | External CT Power |
| dataList.devTempMax | - | number | Inverter Max Temp |
| dataList.devTempMin | - | number | Inverter Min Temp |
| dataList.deviceDataTime | - | string | Device data time string, format: yyyy-MM-dd HH:mm:ss |
| dataList.deviceSn | - | string | Device serial number |
| dataList.ebatCharTotal | - | number | Total battery charging(kWh) |
| dataList.ebatDischarTotal | - | number | Total battery discharge (kWh) |
| dataList.emsCurrent | - | number | Battery current (EMS) |
| dataList.emsPower | - | number | EMS power |
| dataList.emsSoc | - | number | EMS Soc |
| dataList.emsVoltage | - | number | Battery voltage (EMS) |
| dataList.epvToday | - | number | PV Power Today |
| dataList.meterPower | - | number | Home load power |
| dataList.pv2InCurr | - | number | PV2 Current |
| dataList.pv2Power | - | number | PV2 Power |
| dataList.pv2Volt | - | number | PV2 Voltage |
| dataList.pv3InCurr | - | number | PV3 current |
| dataList.pv3Power | - | number | PV3 power |
| dataList.pv3Volt | - | number | PV3 voltage |
| dataList.pvInCurr | - | number | PV1 Current |
| dataList.pvPower | - | number | PV1 Power |
| dataList.pvTotalPower | - | number | Total PV Power（pv1+pv2+pv3+pv4） |
| dataList.pvVolt | - | number | PV1 Voltage |
| dataList.tempMax | - | number | Maximum temperature of battery pack |
| dataList.tempMin | - | number | Minimum temperature of battery pack |
| dataList.timeZone | - | string | time zone |
| dataList.totalConsumPower | - | number | Total electricity consumption（backup load + home load） |
| dataList.totalEnergy | - | number | Total power generation |
| dataList.totalEnergyUnit | - | string | Total power generation unit |
| dataList.workMode | - | string | Work Model |

* Unauthorized(401)

```javascript
No data
```

* Forbidden(403)

```javascript
No data
```

* Not Found(404)

```javascript
No data
```

**Request Header Parameters**

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| Authorization | - | string | Yes | Authorization token |

**Query**

## Event Query (alarms and faults)

> Created by: Timesup

> Updated by: chh

> Created at: 2024-06-22 04:19:50

> Updated at: 2024-08-20 11:57:29

**The application server can call this interface to Query Events (alarms and faults) on the Fsolar platform.,If startTime and endTime are not provided, the default is to query alarm data from the past seven days.**

**Interface Status**

> Completed

**Interface URL**

> /openApi/data/deviceDataWarn/{deviceSn}

**Request Method**

> GET

**Content-Type**

> form-data

**Request Header Parameters**

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| Authorization | - | string | Yes | Authorization token |

**Path Variables**

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| deviceSn | - | string | Yes | Device serial number |

**Request Body Parameters**

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| startTime | - | string | No | with the specified format is "Start Time" or "Beginning Time," formatted as "yyyy-MM-dd HH:mm:ss |
| endTime | - | string | No | with the specified format is "End Time," formatted as "yyyy-MM-dd HH:mm:ss |
| state | - | string | No | with the specified statuses is
 0: Unprocessed
1: Processed
2: Expired
3: In Progress |

**Authentication Method**

> Inherit from parent

**Response Example**

* OK(200)

```javascript
{
  "code": 200,
  "message": "Erfolg",
  "data": [
    {
      "deviceSn": "100202000624170143",
      "warringName": "PV2 Low voltage",
      "warringType": "W",
      "warnCode": "4",
      "dataTimeStr": "2024-06-20 09:08",
      "timeZone": "UTC+8"
    },
    {
      "deviceSn": "100202000624170143",
      "warringName": "Meter comm fail",
      "warringType": "W",
      "warnCode": "42",
      "dataTimeStr": "2024-06-20 09:08",
      "timeZone": "UTC+8"
    },
    {
      "deviceSn": "100202000624170143",
      "warringName": "Meter comm fail",
      "warringType": "W",
      "warnCode": "42",
      "dataTimeStr": "2024-06-19 09:41",
      "timeZone": "UTC+8"
    },
    {
      "deviceSn": "100202000624170143",
      "warringName": "Meter comm fail",
      "warringType": "W",
      "warnCode": "42",
      "dataTimeStr": "2024-06-18 19:50",
      "timeZone": "UTC+8"
    },
    {
      "deviceSn": "100202000624170143",
      "warringName": "PV2 Low voltage",
      "warringType": "W",
      "warnCode": "4",
      "dataTimeStr": "2024-06-18 17:16",
      "timeZone": "UTC+8"
    },
    {
      "deviceSn": "100202000624170143",
      "warringName": "Meter comm fail",
      "warringType": "W",
      "warnCode": "42",
      "dataTimeStr": "2024-06-18 17:08",
      "timeZone": "UTC+8"
    },
    {
      "deviceSn": "100202000624170143",
      "warringName": "PV2 Low voltage",
      "warringType": "W",
      "warnCode": "4",
      "dataTimeStr": "2024-06-18 17:08",
      "timeZone": "UTC+8"
    },
    {
      "deviceSn": "100202000624170143",
      "warringName": "Meter comm fail",
      "warringType": "W",
      "warnCode": "42",
      "dataTimeStr": "2024-06-18 09:31",
      "timeZone": "UTC+8"
    },
    {
      "deviceSn": "100202000624170143",
      "warringName": "Meter comm fail",
      "warringType": "W",
      "warnCode": "42",
      "dataTimeStr": "2024-06-18 08:58",
      "timeZone": "UTC+8"
    },
    {
      "deviceSn": "100202000624170143",
      "warringName": "PV2 Low voltage",
      "warringType": "W",
      "warnCode": "4",
      "dataTimeStr": "2024-06-18 08:58",
      "timeZone": "UTC+8"
    }
  ]
}
```

| Parameter Name | Example Value | Parameter Type | Description |
| --- | --- | ---- | ---- |
| code | - | integer | Code |
| message | - | string | Return Message |
| data.dataTimeStr | - | string | Event time |
| data.deviceSn | - | string | Device serial number |
| data.timeZone | - | string | Time Zone |
| data.warnCode | - | string | Event Code |
| data.warringName | - | string | Event Name |
| data.warringType | - | string | Event Type(F:fault, W:alarm) |

* Unauthorized(401)

```javascript
No data
```

* Forbidden(403)

```javascript
No data
```

* Not Found(404)

```javascript
No data
```

**Request Header Parameters**

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| Authorization | - | string | Yes | Authorization token |

**Query**

## The document provides an explanation of the differences in historical data for devices.

> Created by: chh

> Updated by: chh

> Created at: 2024-08-14 09:53:43

> Updated at: 2024-08-14 11:48:59

**The document provides an explanation of the differences in device response parameters for the following interfaces.,/openApi/data/deviceDataHistory/  (Historical real-time data query (single device)),/openApi/data/devicesDataHistory/ (Historical real-time data query (batch device))**

**Directory Header Parameters**

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| No parameters |

**Directory Query Parameters**

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| No parameters |

**Directory Body Parameters**

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| No parameters |

**Directory Authentication Info**

> Inherit from parent

**Query**

### T-REX

> Created by: chh

> Updated by: chh

> Created at: 2024-08-14 09:55:19

> Updated at: 2024-08-15 07:54:33

****T-REX General parameters for all types
****

| Field name | Field type | Field description | Unit | Description |
| ---------- | ---------- | ----------------- | ---- | ----------- |
| deviceSn | String | SN | - |  |
| deviceDataTime | String | data Time | - |  |
| timeZone | String | time zone | - |  |
| pvVolt | Double | PV1 Voltage | V |  |
| pv2Volt | Double | PV2 Voltage | V |  |
| pv3Volt | Double | PV3 Voltage | V |  |
| pv4Volt | Double | PV4 Voltage | V |  |
| pvInCurr | Double | PV1 Current | A |  |
| pv2InCurr | Double | PV2 Current | A |  |
| pv3InCurr | Double | PV3 Current | A |  |
| pv4InCurr | Double | PV4 Current | A |  |
| pvPower | Double | PV1 Power | kW |  |
| pv2Power | Double | PV2 Power | kW |  |
| pv3Power | Double | PV3 Power | kW |  |
| pv4Power | Double | PV4 Power | kW |  |
| pvTotalPower | Double | Total PV Power | kW |  |
| acRInVolt | Double | Grid L1 Voltage | V |  |
| acSInVolt | Double | Grid L2 Voltage | V |  |
| acTInVolt | Double | Grid L3 Voltage | V |  |
| acRInCurr | Double | Grid L1 Current | A |  |
| acSInCurr | Double | Grid L2 Current | A |  |
| acTInCurr | Double | Grid L3 Current | A |  |
| acRInFreq | Double | Grid L1 Frequency | Hz |  |
| acSInFreq | Double | Grid L2 Frequency | Hz |  |
| acTInFreq | Double | Grid L3 Frequency | Hz |  |
| acRInPower | Double | Grid L1 Power | kW |  |
| acSInPower | Double | Grid L2 Power | kW |  |
| acTInPower | Double | Grid L3 Power | kW |  |
| acTtlInpower | Double | Total Grid Power | kW |  |
| ctPower | Double | External CT Power | kW |  |
| acROutVolt | Double | Backup Load L1 Voltage | V |  |
| acSOutVolt | Double | Backup Load L2 Voltage | V |  |
| acTOutVolt | Double | Backup Load L3 Voltage | V |  |
| acROutCurr | Double | Backup Load L1 Current | A |  |
| acSOutCurr | Double | Backup Load L2 Current | A |  |
| acTOutCurr | Double | Backup Load L3 Current | A |  |
| acROutFreq | Double | Backup Load L1 Frequency | Hz |  |
| acSOutFreq | Double | Backup Load L2 Frequency | Hz |  |
| acTOutFreq | Double | Backup Load L3 Frequency | Hz |  |
| acROutPower | Double | Backup Load L1 Power | kW |  |
| acSOutPower | Double | Backup Load L1 Power | kW |  |
| acTOutPower | Double | Backup Load L1 Power | kW |  |
| acTotalOutActPower | Double | "Total Backup Load Active Power | kW |  |
| acTotalOutAppaPower | Double | "Total Backup Load Apparent Power | kVA |  |
| meterPower | Double | Home Load | kW |  |
| emsVoltage | Double | Battery Voltage | V |  |
| emsVoltage2 | Double | Battery2 Voltage | V |  |
| emsCurrent | Double | Battery Current | A |  |
| emsCurrent2 | Double | Battery2 Current | A |  |
| emsPower | Double | Battery Power | kW |  |
| emsPower2 | Double | Battery2 Power | kW |  |
| emsSoc | Double | SOC | % |  |
| emsSoc2 | Double | SOC2 | % |  |
| genVoltage | Double | Gen L1 Voltage | V |  |
| genVoltage2 | Double | Gen L2 Voltage | V |  |
| genVoltage3 | Double | Gen L3 Voltage | V |  |
| genCurrent | Double | Gen L1 Current | A |  |
| genCurrent2 | Double | Gen L2 Current | A |  |
| genCurrent3 | Double | Gen L3 Current | A |  |
| genFrequency | Double | Gen L1 Frequency | Hz |  |
| genPower | Double | Gen L1 Power | kW |  |
| genPower2 | Double | Gen L2 Power | kW |  |
| genPower3 | Double | Gen L3 Power | kW |  |
| genTotalPower | Double | Gen Total Power | kW |  |
| workMode | Double | Work Model | - | 0:Power On Mode,1:Standby Mode,2:Bypass Mode,3:Off-Grid Mode,4:Fault Mode,5:Line Mode,6:PV Charge Mode,7:Gen Mode,8:TurnOff |
| devTempMax | Double | Inverter Max Temp | ℃ |  |
| devTempMin | Double | Inverter Min Temp | ℃ |  |

**Response Example.**

```json
{
        "acTInFreq": "6",
        "genPower2": null,
        "genPower3": null,
        "pv3InCurr": "36.3",
        "acTotalOutAppaPower": "2.1",
        "timeZone": "UTC+8",
        "acTInPower": "21",
        "pvPower": "0",
        "acRInPower": "21",
        "emsSoc": "100",
        "acTInCurr": "75",
        "workMode": "1",
        "emsPower": "0.2",
        "emsPower2": "54.1",
        "pv3Power": "34.5",
        "genFrequency": null,
        "acSInFreq": "6",
        "acSOutPower": "0.2",
        "pv2InCurr": "26.3",
        "createTime": "2024-08-14T21:25:03",
        "acROutVolt": "139.3",
        "dataTimeStr": "21:25:00",
        "ctPower": null,
        "emsCurrent": "0.5",
        "devTempMax": "310",
        "acTOutCurr": "39",
        "acSOutFreq": "25.1",
        "meterPower": null,
        "pv4InCurr": "46.3",
        "genVoltage3": null,
        "genVoltage2": null,
        "pvVolt": "274",
        "emsVoltage2": "54.1",
        "acTOutVolt": "339.3",
        "acRInCurr": "75",
        "pv4Volt": "444.4",
        "genPower": null,
        "acTOutPower": "0.3",
        "acSOutVolt": "239.3",
        "emsVoltage": "54.1",
        "deviceSn": "013548202500021000",
        "pv4Power": "44.5",
        "acRInFreq": "6",
        "acSInPower": "21",
        "acSOutCurr": "29",
        "acTOutFreq": "35.1",
        "pv3Volt": "333.3",
        "acTInVolt": "389.3",
        "genTotalPower": null,
        "devTempMin": "180",
        "acTtlInpower": "50.1",
        "emsCurrent2": "5410",
        "emsSoc2": null,
        "acTotalOutActPower": "1.1",
        "acSInCurr": "75",
        "acROutCurr": "19",
        "genCurrent": null,
        "genCurrent3": null,
        "genCurrent2": null,
        "pvTotalPower": "103.5",
        "genVoltage": null,
        "acROutPower": "0.1",
        "acRInVolt": "389.3",
        "acSInVolt": "389.3",
        "pv2Power": "24.5",
        "deviceDataTime": "2024-08-14 21:25:03",
        "pv2Volt": "222.2",
        "acROutFreq": "15.1",
        "pvInCurr": "16.3"
      }
```

**Query**

### IVGM

> Created by: chh

> Updated by: chh

> Created at: 2024-08-14 09:54:44

> Updated at: 2024-08-16 08:07:22

****IVGM General parameters for all types
****

| Field name | Field type | Field description | Unit | Description |
| ---------- | ---------- | ----------------- | ---- | ----------- |
| deviceSn | String | SN | - |  |
| deviceDataTime | String | data Time | - |  |
| timeZone | String | time zone | - |  |
| pvVolt | Double | PV1 Voltage | V |  |
| pv2Volt | Double | PV2 Voltage | V |  |
| pvInCurr | Double | PV1 Current | A |  |
| pv2InCurr | Double | PV2 Current | A |  |
| pvPower | Double | PV1 Power | W |  |
| pv2Power | Double | PV2 Power | W |  |
| pvTotalPower | Double | Total PV Power | W |  |
| acRInVolt | Double | Grid L1 Voltage | V |  |
| acRInCurr | Double | Grid L1 Current | A |  |
| acRInFreq | Double | Grid L1 Frequency | Hz |  |
| acRInPower | Double | Grid L1 Power | W |  |
| acTtlInpower | Double | Total Grid Power | W |  |
| ctPower | Double | External CT Power | W |  |
| acROutVolt | Double | Backup Load L1 Voltage | V |  |
| acROutCurr | Double | Backup Load L1 Current | A |  |
| acROutFreq | Double | Backup Load L1 Frequency | Hz |  |
| acROutPower | Double | Backup Load L1 Power | W |  |
| acTotalOutActPower | Double | "Total Backup Load Active Power | W |  |
| acTotalOutAppaPower | Double | "Total Backup Load Apparent Power | VA |  |
| meterPower | Double | Home Load | W |  |
| emsVoltage | Double | Battery Voltage | V |  |
| emsCurrent | Double | Battery Current | A |  |
| emsPower | Double | Battery Power | W |  |
| emsSoc | Double | SOC | % |  |
| workMode | Double | Work Model | - | 0:Power On Mode",1:Standby Mode,2:Bypass Mode,3:Off-Grid Mode,4:Fault Mode,5:Line Mode,6:PV Charge Mode |
| devTempMax | Double | Inverter Max Temp | ℃ |  |
| devTempMin | Double | Inverter Min Temp | ℃ |  |

**Response Example.**

```json
{
        "acTotalOutAppaPower": "5484",
        "timeZone": "UTC+8",
        "pvPower": "100",
        "acRInPower": "1464",
        "emsSoc": "2",
        "workMode": "5",
        "emsPower": "-227",
        "pv2InCurr": "6.6",
        "createTime": "2024-08-14T21:25:03",
        "acROutVolt": "238.8",
        "dataTimeStr": "21:25:00",
        "ctPower": "4260",
        "emsCurrent": "3.2",
        "devTempMax": "53.9",
        "meterPower": null,
        "pvVolt": "2",
        "acRInCurr": "6.1",
        "emsVoltage": "53.6",
        "deviceSn": "020505004822240016",
        "acRInFreq": "49.99",
        "devTempMin": "41.7",
        "acTtlInpower": "4260",
        "acTotalOutActPower": "4293",
        "acROutCurr": "7.9",
        "pvTotalPower": "467",
        "acROutPower": "1477",
        "acRInVolt": "238.8",
        "pv2Power": "367",
        "deviceDataTime": "2024-08-14 21:25:03",
        "pv2Volt": "1.8",
        "acROutFreq": "49.97",
        "pvInCurr": "6.3"
      }
```

**Query**

# Device Interface

> Created by: chh

> Updated by: chh

> Created at: 2024-06-20 08:41:44

> Updated at: 2024-06-25 13:31:30

```text
No description
```

**Directory Header Parameters**

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| No parameters |

**Directory Query Parameters**

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| No parameters |

**Directory Body Parameters**

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| No parameters |

**Directory Authentication Info**

> Inherit from parent

**Query**

## Deleting devices in bulk

> Created by: chh

> Updated by: Timesup

> Created at: 2024-06-20 08:48:41

> Updated at: 2024-06-27 05:07:56

```text
No description
```

**Interface Status**

> Completed

**Interface URL**

> /openApi/devices/del

**Request Method**

> POST

**Content-Type**

> json

**Request Header Parameters**

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| Authorization | Bearer_eyJhbGciOiJIUzI1NiJ9.eyJkZW1vVXNlciI6ZmFsc2UsInN1YiI6Iui-o-akkiIsImF1ZCI6Ik9UQXlNVEUxTkRBME5EazRPRGc1Tmc9PSIsIm5iZiI6MTcxODg2NDIxOSwiaXNzIjoiRkxTLVNPTEFSLVNFUlZFUiIsImlkIjo5MDIxMTU0MDQ0OTg4ODk2LCJleHAiOjE3MjE0NTYyMTksImlhdCI6MTcxODg2NDIxOX0.T_uFdGuJJm2bssgTiHTRuzpRv17q7_sgYkOraAFdXBk | Text | Yes | User token, which can be obtained from authentication and refreshing tokens. |

**Request Body Parameters**

```javascript
{
	"deviceSns": [
        "020505004823490001"
        ]
}
```

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| deviceSns | 020505004823490001 | array | Yes | Device SN collection |

**Authentication Method**

> Inherit from parent

**Response Example**

* Success(200)

```javascript
{
	"code": 200,
	"message": "Success",
	"data": {}
}
```

* Fail(201)

```javascript
{
	"code": 1006002,
	"message": "Device does not exist",
	"data": "Device does not exist"
}
```

**Request Header Parameters**

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| Authorization | Bearer_eyJhbGciOiJIUzI1NiJ9.eyJkZW1vVXNlciI6ZmFsc2UsInN1YiI6Iui-o-akkiIsImF1ZCI6Ik9UQXlNVEUxTkRBME5EazRPRGc1Tmc9PSIsIm5iZiI6MTcxODg2NDIxOSwiaXNzIjoiRkxTLVNPTEFSLVNFUlZFUiIsImlkIjo5MDIxMTU0MDQ0OTg4ODk2LCJleHAiOjE3MjE0NTYyMTksImlhdCI6MTcxODg2NDIxOX0.T_uFdGuJJm2bssgTiHTRuzpRv17q7_sgYkOraAFdXBk | Text | Yes | User token, which can be obtained from authentication and refreshing tokens. |

**Query**

## Device list

> Created by: chh

> Updated by: Timesup

> Created at: 2024-06-20 08:52:31

> Updated at: 2024-06-27 05:08:03

```text
No description
```

**Interface Status**

> Completed

**Interface URL**

> /openApi/devices/list

**Request Method**

> GET

**Content-Type**

> form-data

**Request Header Parameters**

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| Authorization | Bearer_eyJhbGciOiJIUzI1NiJ9.eyJkZW1vVXNlciI6ZmFsc2UsInN1YiI6Iui-o-akkiIsImF1ZCI6Ik9UQXlNVEUxTkRBME5EazRPRGc1Tmc9PSIsIm5iZiI6MTcxODg2NDIxOSwiaXNzIjoiRkxTLVNPTEFSLVNFUlZFUiIsImlkIjo5MDIxMTU0MDQ0OTg4ODk2LCJleHAiOjE3MjE0NTYyMTksImlhdCI6MTcxODg2NDIxOX0.T_uFdGuJJm2bssgTiHTRuzpRv17q7_sgYkOraAFdXBk | Text | Yes | User token, which can be obtained from authentication and refreshing tokens. |

**Request Body Parameters**

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| deviceSn | - | string | Yes | Device Sn |
| pageNum | 1 | number | Yes | Page number, starting from 1, mandatory. |
| pageSize | 10 | number | Yes | Number of items per page, maximum value is 300, required. |

**Authentication Method**

> Inherit from parent

**Response Example**

* Success(200)

```javascript
{
	"code": 200,
	"message": "Success",
	"data": {
		"dataList": [
			{
				"deviceSn": "020505004822240024",
				"masterVersion": null,
				"slaveVersion": null,
				"commVersion": null,
				"hardwareVersion": null,
				"bpMasterVersion": null,
				"bpIpaVersion": null,
				"bpSubVersion": null
			},
			{
				"deviceSn": "020505004822240016",
				"masterVersion": "424",
				"slaveVersion": null,
				"commVersion": null,
				"hardwareVersion": null,
				"bpMasterVersion": null,
				"bpIpaVersion": null,
				"bpSubVersion": null
			},
			{
				"deviceSn": "020505004823490001",
				"masterVersion": null,
				"slaveVersion": null,
				"commVersion": null,
				"hardwareVersion": null,
				"bpMasterVersion": null,
				"bpIpaVersion": null,
				"bpSubVersion": null
			},
			{
				"deviceSn": "020505004822240010",
				"masterVersion": null,
				"slaveVersion": null,
				"commVersion": null,
				"hardwareVersion": null,
				"bpMasterVersion": null,
				"bpIpaVersion": null,
				"bpSubVersion": null
			},
			{
				"deviceSn": "020505004822242583",
				"masterVersion": null,
				"slaveVersion": null,
				"commVersion": null,
				"hardwareVersion": null,
				"bpMasterVersion": null,
				"bpIpaVersion": null,
				"bpSubVersion": null
			},
			{
				"deviceSn": "020505004822242582",
				"masterVersion": null,
				"slaveVersion": null,
				"commVersion": null,
				"hardwareVersion": null,
				"bpMasterVersion": null,
				"bpIpaVersion": null,
				"bpSubVersion": null
			}
		],
		"total": "6",
		"totalPage": "1",
		"pageSize": "10",
		"currentPage": "1",
		"data": null
	}
}
```

| Parameter Name | Example Value | Parameter Type | Description |
| --- | --- | ---- | ---- |
| code | 200 | number | code, 200 successful response |
| message | Success | string | message |
| data | - | object | data |
| data.dataList | - | object | - |
| data.dataList.deviceSn | 020505004822240024 | string | Device serial number |
| data.dataList.masterVersion | - | object | Inverter - Control version, ps: This field only has numerical values for inverters |
| data.dataList.slaveVersion | - | object | Inverter - From Control Version |
| data.dataList.commVersion | - | object | Inverter - Communication version, ps: This field only has numerical values for inverters |
| data.dataList.hardwareVersion | - | object | Inverter - Hardware version, ps: This field only has numerical values for inverters |
| data.dataList.bpMasterVersion | - | object | Battery Pack - Control Version, ps: This field only has a numerical value for the battery pack |
| data.dataList.bpIpaVersion | - | object | Battery pack IPA version, ps: This field only has a numerical value for the battery pack |
| data.dataList.bpSubVersion | - | object | Battery Pack - Auxiliary Version, ps: This field only has a numerical value for the battery pack |
| data.total | 6 | string | total page |
| data.totalPage | 1 | string | - |
| data.pageSize | 10 | string | The maximum number of entries per page is 300, which is required |
| data.currentPage | 1 | string | - |
| data.data | - | object | Additional data |

* Fail(201)

```javascript
No data
```

**Request Header Parameters**

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| Authorization | Bearer_eyJhbGciOiJIUzI1NiJ9.eyJkZW1vVXNlciI6ZmFsc2UsInN1YiI6Iui-o-akkiIsImF1ZCI6Ik9UQXlNVEUxTkRBME5EazRPRGc1Tmc9PSIsIm5iZiI6MTcxODg2NDIxOSwiaXNzIjoiRkxTLVNPTEFSLVNFUlZFUiIsImlkIjo5MDIxMTU0MDQ0OTg4ODk2LCJleHAiOjE3MjE0NTYyMTksImlhdCI6MTcxODg2NDIxOX0.T_uFdGuJJm2bssgTiHTRuzpRv17q7_sgYkOraAFdXBk | Text | Yes | User token, which can be obtained from authentication and refreshing tokens. |

**Query**

## Bulk device addition

> Created by: chh

> Updated by: Timesup

> Created at: 2024-06-20 08:42:52

> Updated at: 2024-06-27 05:08:10

```text
No description
```

**Interface Status**

> Completed

**Interface URL**

> /openApi/devices/reg

**Request Method**

> POST

**Content-Type**

> json

**Request Header Parameters**

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| Authorization | Bearer_eyJhbGciOiJIUzI1NiJ9.eyJkZW1vVXNlciI6ZmFsc2UsInN1YiI6Iui-o-akkiIsImF1ZCI6Ik9UQXlNVEUxTkRBME5EazRPRGc1Tmc9PSIsIm5iZiI6MTcxODg2NDIxOSwiaXNzIjoiRkxTLVNPTEFSLVNFUlZFUiIsImlkIjo5MDIxMTU0MDQ0OTg4ODk2LCJleHAiOjE3MjE0NTYyMTksImlhdCI6MTcxODg2NDIxOX0.T_uFdGuJJm2bssgTiHTRuzpRv17q7_sgYkOraAFdXBk | Text | Yes | User token, which can be obtained from authentication and refreshing tokens. |

**Request Body Parameters**

```javascript
{
	"deviceSaveInfoList": [
		{
			"checkCode": "0000",
			"deviceSn": "020505004823490001"
		}
	]
}
```

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| deviceSaveInfoList | - | object | Yes | - |
| deviceSaveInfoList.checkCode | 0000 | string | Yes | Verification code, located at the device's barcode. |
| deviceSaveInfoList.deviceSn | 020505004823490001 | string | Yes | Device Sn |

**Authentication Method**

> Inherit from parent

**Response Example**

* Success(200)

```javascript
{
	"code": 200,
	"message": "Success",
	"data": {}
}
```

* Fail(201)

```javascript
{
	"code": 1006001,
	"message": "Device already exists:020505004823490001",
	"data": "Device already exists:020505004823490001"
}
```

**Request Header Parameters**

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| Authorization | Bearer_eyJhbGciOiJIUzI1NiJ9.eyJkZW1vVXNlciI6ZmFsc2UsInN1YiI6Iui-o-akkiIsImF1ZCI6Ik9UQXlNVEUxTkRBME5EazRPRGc1Tmc9PSIsIm5iZiI6MTcxODg2NDIxOSwiaXNzIjoiRkxTLVNPTEFSLVNFUlZFUiIsImlkIjo5MDIxMTU0MDQ0OTg4ODk2LCJleHAiOjE3MjE0NTYyMTksImlhdCI6MTcxODg2NDIxOX0.T_uFdGuJJm2bssgTiHTRuzpRv17q7_sgYkOraAFdXBk | Text | Yes | User token, which can be obtained from authentication and refreshing tokens. |

**Query**

# Remote Control

> Created by: Timesup

> Updated by: Timesup

> Created at: 2024-06-22 04:19:50

> Updated at: 2024-06-26 13:46:41

**The application server can remotely control devices (inverters, etc.).**

**Directory Header Parameters**

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| No parameters |

**Directory Query Parameters**

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| No parameters |

**Directory Body Parameters**

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| No parameters |

**Directory Authentication Info**

> Inherit from parent

**Query**

## Remote Control Setting

> Created by: Timesup

> Updated by: Timesup

> Created at: 2024-06-22 04:19:50

> Updated at: 2025-03-13 14:18:17

**The application server can call this interface to set parameters for devices (inverters, etc.) through the Fsolar platform. Pay attention to the range of parameters, otherwise the parameters may not be set successfully.
Default support T-REX-6KLP1G01、T-REX-10KHP3G01、T-REX-5KLP1G01、T-REX-10KLP3G01. 
More device support see: Remote Control Setting Attachment**

**Interface Status**

> Completed

**Interface URL**

> /openApi/cmd/deviceSetting

**Request Method**

> POST

**Content-Type**

> json

**Request Header Parameters**

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| Content-Type | application/json | string | Yes | - |
| Authorization | Bearer_eyJhbGciOiJIUzI1NiJ9.eyJkZW1vVXNlciI6ZmFsc2UsInN1YiI6IueuoeeQhuWRmCIsImF1ZCI6Ik56TTNORFF4TkRrd01UVTFPREUwTkE9PSIsIm5iZiI6MTcxMTY3NjY4NiwiaXNzIjoiRkxTLVNPTEFSLVNFUlZFUiIsImlkIjo3Mzc0NDE0OTAxNTU4MTQ0LCJleHAiOjE3MTQyNjg2ODYsImlhdCI6MTcxMTY3NjY4Nn0._l5VIYevtyv2Xc66S9w6fqmkECBFvLZPJYqjU07pObE | string | Yes | User token, which can be obtained from authentication and refreshing tokens. |
| Lang | en_US | string | Yes | Language, currently supports English en_US. |

**Request Body Parameters**

```javascript
{
	"content": {
		"acOutputRatedFrequency": 0,
		"acOutputRatedVoltage": "",
		"antiIslandingDetectionEnable": 0,
		"batteryChargedVoltage": "",
		"batteryFloatingChargedVoltage": "",
		"batteryMaxChargedCurrent": "",
		"batteryMaxDischargeCurrent": "",
		"batteryModel": 0,
		"batteryModules": 0,
		"batteryOffGridDischargeDepthSoc": 0,
		"batteryOffGridRecoveryDepthSoc": 0,
		"batteryOnGridDischargeDepthSoc": 0,
		"buzzerEnable": 0,
		"commOffLineEnable": 0,
		"deratingByVoltageEnable": 0,
		"ecoRule1": {
			"daysOfEffectiveWeek": [
				""
			],
			"power": 0,
			"ruleMode": 0,
			"soc": 0,
			"startDay": "",
			"startTime": "",
			"stopDay": "",
			"stopTime": "",
			"voltage": ""
		},
		"ecoRule2": {
			"daysOfEffectiveWeek": [
				""
			],
			"power": 0,
			"ruleMode": 0,
			"soc": 0,
			"startDay": "",
			"startTime": "",
			"stopDay": "",
			"stopTime": "",
			"voltage": ""
		},
		"ecoRule3": {
			"daysOfEffectiveWeek": [
				""
			],
			"power": 0,
			"ruleMode": 0,
			"soc": 0,
			"startDay": "",
			"startTime": "",
			"stopDay": "",
			"stopTime": "",
			"voltage": ""
		},
		"ecoRule4": {
			"daysOfEffectiveWeek": [
				""
			],
			"power": 0,
			"ruleMode": 0,
			"soc": 0,
			"startDay": "",
			"startTime": "",
			"stopDay": "",
			"stopTime": "",
			"voltage": ""
		},
		"eventLogFunctionEnable": 0,
		"faultLogFunctionEnable": 0,
		"fixQPencent": "",
		"fpChargeCurveFunctionEnable": 0,
		"fpCurveFunctionEnable": 0,
		"fpCurveOverFrequencyLowerLimit": "",
		"fpOverFrequencyPowerSlope": "",
		"fpOverFrequencyUpperLimit": "",
		"fpRecoveryPowerSlope": "",
		"fpRestoreFrequencyLowerLimit": "",
		"fpRestoreFrequencyPowerSlope": 0,
		"fpRestoreFrequencyUperLimit": "",
		"fpRestoreFrequencyWaitingTime": 0,
		"fpUnderFrequencyLowerLimit": "",
		"fpUnderFrequencyPowerSlope": "",
		"fpUnderFrequencyPowerSlopeForCharge": "",
		"fpUnderFrequencyUpperLimit": "",
		"gridPowerUnbalanceEnable": 0,
		"gridStandardCode": 0,
		"gridWaveformDetectionMode": 0,
		"highVoltageCrossingTripThreshold": "",
		"highVoltageEndPointTripTime": "",
		"highVoltageEndPointTripValue": "",
		"highVoltageRideThroughFunctionEnable": 0,
		"highVoltageStartPointTripTime": "",
		"highVoltageStartPointTripValue": "",
		"isoDetectionEnable": 0,
		"lcdBacklightEnable": 0,
		"lowVoltageCrossingTripThreshold": "",
		"lowVoltageEndPointTripTime": "",
		"lowVoltageEndPointTripValue": "",
		"lowVoltageRideThroughFunctionEnable": 0,
		"lowVoltageStartPointTripTime": "",
		"lowVoltageStartPointTripValue": "",
		"noBmsOffGridBatteryCutOffVoltage": "",
		"noBmsOffGridBatteryRestartVoltage": "",
		"noBmsOnGridBatteryCutOffVoltage": "",
		"onGridObservationTime": 0,
		"onGridPowerLimit": "",
		"onGridPowerSlope": 0,
		"operatedMode": 0,
		"overFrequencyStage1TripTime": "",
		"overFrequencyStage1TripValue": "",
		"overFrequencyStage2TripTime": "",
		"overFrequencyStage2TripValue": "",
		"overLoadProtectionResetEnable": 0,
		"overVoltage10mTriggerValue": "",
		"overVoltageStage1TripTime": "",
		"overVoltageStage1TripValue": "",
		"overVoltageStage2TripTime": "",
		"overVoltageStage2TripValue": "",
		"pfPowerCurveFunctionEnable": 0,
		"pfPowerCurveLockinVoltage": "",
		"pfPowerCurveLockoutPower": "",
		"pfPowerCurveLockoutVoltage": "",
		"pfPowerCurvePointAPower": "",
		"pfPowerCurvePointAPowerFactor": "",
		"pfPowerCurvePointBPower": "",
		"pfPowerCurvePointBPowerFactor": "",
		"pfPowerCurvePointCPower": "",
		"pfPowerCurvePointCPowerFactor": "",
		"powerFactor": "",
		"puCurveFunctionEnable": 0,
		"puCurvePointAActivePower": "",
		"puCurvePointAVoltage": "",
		"puCurvePointBActivePower": "",
		"puCurvePointBVoltage": "",
		"puCurvePointCActivePower": "",
		"puCurvePointCVoltage": "",
		"puCurvePointDActivePower": "",
		"puCurvePointDVoltage": "",
		"pvParallelSetting": 0,
		"quCurveFunctionEnable": 0,
		"quCurveLockInPower": "",
		"quCurveLockOutPower": "",
		"quCurvePointAReactivePower": "",
		"quCurvePointAVoltage": "",
		"quCurvePointBReactivePower": "",
		"quCurvePointBVoltage": "",
		"quCurvePointCReactivePower": "",
		"quCurvePointCVoltage": "",
		"quCurvePointDReactivePower": "",
		"quCurvePointDVoltage": "",
		"remoteOnOffEnable": 0,
		"remoteOutputOnOffControl": 0,
		"underFrequencyStage1TripTime": "",
		"underFrequencyStage1TripValue": "",
		"underFrequencyStage2TripTime": "",
		"underFrequencyStage2TripValue": "",
		"underVoltageStage1TripTime": "",
		"underVoltageStage1TripValue": "",
		"underVoltageStage2TripTime": "",
		"underVoltageStage2TripValue": "",
		"zeroExportAdjustmentPower": 0,
		"zeroExportFunction": 0
	},
	"deviceSn": ""
}
```

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| content.acOutputRatedFrequency | 1 | integer | No | AC Output Rated Frequency，0：50Hz, 1：60Hz |
| content.acOutputRatedVoltage | - | number | No | AC Output Rated Voltage，Cannot be set |
| content.antiIslandingDetectionEnable | 1 | integer | No | Anti-Islanding Detection，0：Disable， 1：Enable |
| content.batteryChargedVoltage | 51.3 | number | No | Battery Charged Voltage，It is related to the "Battery Model",Each Model The range of values is 48~60V |
| content.batteryFloatingChargedVoltage | 52.5 | number | No | Battery Floating Charged Voltage，It is related to the "Battery Model",Each Model The range of values is 48~60V |
| content.batteryMaxChargedCurrent | 160 | number | No | Battery Max Charged Current，The range of values is 1~200A |
| content.batteryMaxDischargeCurrent | 110 | number | No | Battery Max Discharge Current，The range of values is 5~200A |
| content.batteryModel | 1 | integer | No | Battery Model，0：User defined，1：Lithium battery(default)，2：FelicitySolar(LPBF series)，3：FelicitySolar(LPBA series) |
| content.batteryModules | 1 | integer | No | Battery Modules，It is related to the "Battery Model", and can be set when the battery type is "User defined" |
| content.batteryOffGridDischargeDepthSoc | 40 | integer | No | Battery Off Grid Discharge Depth Soc，The range of values is 0~100% |
| content.batteryOffGridRecoveryDepthSoc | 60 | integer | No | Battery Off Grid Recovery Depth Soc，The range of values is 0~100% |
| content.batteryOnGridDischargeDepthSoc | 50 | integer | No | Battery On Grid Discharge DepthSoc，The range of values is 10~100% |
| content.buzzerEnable | 1 | integer | No | Buzzer Enable，0：Disable， 1：Enable |
| content.commOffLineEnable | 0 | integer | No | Comm Off Line Enable，0：Disable， 1：Enable |
| content.deratingByVoltageEnable | 0 | integer | No | 110%u Derating By Voltage Enable |
| content.ecoRule1.daysOfEffectiveWeek.0 | ["MONDAY", "TUESDAY"] | array | No | ECO Mode Rule 1，Days Of Effective Week,Valuable：MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY，Multiple Choice |
| content.ecoRule1.power | 100 | integer | No | ECO Mode Rule 1，Battery charging or discharging power,Unit：W，The range of values is 0~ inverter rated power |
| content.ecoRule1.ruleMode | 1 | integer | No | ECO Mode Rule 1，0：disable, 1: enable charge 2: enable discharge |
| content.ecoRule1.soc | 50 | integer | No | ECO Mode Rule 1，Battery charging or discharging soc，Unit：%，The range of values is 0~100% |
| content.ecoRule1.startDay | 01:01 | string | No | ECO Mode Rule 1，Starting date, Format: mm:dd |
| content.ecoRule1.startTime | 14:20 | string | No | ECO Mode Rule 1，Starting time, Format: HH:ss |
| content.ecoRule1.stopDay | 12:12 | string | No | ECO Mode Rule 1，Stop date, Format: mm:dd |
| content.ecoRule1.stopTime | 23:59 | string | No | ECO Mode Rule 1，Stop time, Format: HH:ss |
| content.ecoRule1.voltage | 50 | number | No | ECO Mode Rule 1，Battery charging or discharging voltage，Unit：V，It is related to the "Battery Model",Each Model The range of values is 48~60V |
| content.ecoRule1 | - | object | No | Economic Model Rule 1 Object |
| content.ecoRule2.daysOfEffectiveWeek.0 | ["MONDAY", "TUESDAY"] | array | No | ECO Mode Rule 2，Days Of Effective Week,Valuable：MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY，Multiple Choice |
| content.ecoRule2.power | 50 | integer | No | ECO Mode Rule 2，Battery charging or discharging power,Unit：W，The range of values is 0~ inverter rated power |
| content.ecoRule2.ruleMode | 2 | integer | No | ECO Mode Rule 2，0：disable, 1: enable charge 2: enable discharge |
| content.ecoRule2.soc | 60 | integer | No | ECO Mode Rule 2，Battery charging or discharging soc，Unit：%，The range of values is 0~100% |
| content.ecoRule2.startDay | 01:01 | string | No | ECO Mode Rule 2，Starting date, Format: mm:dd |
| content.ecoRule2.startTime | 14:20 | string | No | ECO Mode Rule 2，Starting time, Format: HH:ss |
| content.ecoRule2.stopDay | 12:12 | string | No | ECO Mode Rule 2，Stop date, Format: mm:dd |
| content.ecoRule2.stopTime | 23:59 | string | No | ECO Mode Rule 2，Stop time, Format: HH:ss |
| content.ecoRule2.voltage | 51 | number | No | ECO Mode Rule 2，Battery charging or discharging voltage，Unit：V，It is related to the "Battery Model",Each Model The range of values is 48~60V |
| content.ecoRule2 | - | object | No | Economic Model Rule 2 Object |
| content.ecoRule3.daysOfEffectiveWeek.0 | ["MONDAY", "TUESDAY"] | array | No | ECO Mode Rule 3，Days Of Effective Week,Valuable：MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY，Multiple Choice |
| content.ecoRule3.power | 40 | integer | No | ECO Mode Rule 3，Battery charging or discharging power,Unit：W，The range of values is 0~inverter rated power |
| content.ecoRule3.ruleMode | 1 | integer | No | ECO Mode Rule 3，0：disable, 1: enable charge 2: enable discharge |
| content.ecoRule3.soc | 50 | integer | No | ECO Mode Rule 3，Battery charging or discharging soc，Unit：%，The range of values is 0~100% |
| content.ecoRule3.startDay | 01:01 | string | No | ECO Mode Rule 3，Starting date, Format: mm:dd |
| content.ecoRule3.startTime | 14:20 | string | No | ECO Mode Rule 3，Starting time, Format: HH:ss |
| content.ecoRule3.stopDay | 12:12 | string | No | ECO Mode Rule 3，Stop date, Format: mm:dd |
| content.ecoRule3.stopTime | 23:59 | string | No | ECO Mode Rule 3，Stop time, Format: HH:ss |
| content.ecoRule3.voltage | 60 | number | No | ECO Mode Rule 3，Battery charging or discharging voltage，Unit：V，It is related to the "Battery Model",Each Model The range of values is 48~60V |
| content.ecoRule3 | - | object | No | Economic Model Rule 3 Object |
| content.ecoRule4.daysOfEffectiveWeek.0 | ["MONDAY", "TUESDAY"] | array | No | ECO Mode Rule 4，Days Of Effective Week,Valuable：MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY，Multiple Choice |
| content.ecoRule4.power | 40 | integer | No | ECO Mode Rule 4，Battery charging or discharging power,Unit：W，The range of values is 0~inverter rated power |
| content.ecoRule4.ruleMode | 2 | integer | No | ECO Mode Rule 4，0：disable, 1: enable charge 2: enable discharge |
| content.ecoRule4.soc | 60 | integer | No | ECO Mode Rule 4，Battery charging or discharging soc，Unit：%，The range of values is 0~100% |
| content.ecoRule4.startDay | 01:01 | string | No | ECO Mode Rule 4，Starting date, Format: mm:dd |
| content.ecoRule4.startTime | 14:20 | string | No | ECO Mode Rule 4，Starting time, Format: HH:ss |
| content.ecoRule4.stopDay | 12:12 | string | No | ECO Mode Rule 4，Stop date, Format: mm:dd |
| content.ecoRule4.stopTime | 23:59 | string | No | ECO Mode Rule 4，Stop time, Format: HH:ss |
| content.ecoRule4.voltage | 35 | number | No | ECO Mode Rule 4，Battery charging or discharging voltage，Unit：V，It is related to the "Battery Model",Each Model The range of values is 48~60V |
| content.ecoRule4 | - | object | No | Economic Mode Rule 4 Object |
| content.eventLogFunctionEnable | - | integer | No | Event Log Function，Cannot be set |
| content.faultLogFunctionEnable | - | integer | No | Fault Log Function，Cannot be set |
| content.fixQPencent | - | number | No | FixQ Pencent, unit：% |
| content.fpChargeCurveFunctionEnable | - | integer | No | Frequency-PoweryCharge Curve Function，0：Disable， 1：Enable |
| content.fpCurveFunctionEnable | - | integer | No | Frequency-Power Curve Function，0：Disable， 1：Enable |
| content.fpCurveOverFrequencyLowerLimit | - | number | No | Over Frequency Start Point |
| content.fpOverFrequencyPowerSlope | - | number | No | Over Frequency Power Slope |
| content.fpOverFrequencyUpperLimit | - | number | No | Over Frequency End Point |
| content.fpRecoveryPowerSlope | - | number | No | Recovery Power Slope |
| content.fpRestoreFrequencyLowerLimit | - | number | No | F(Stop) Lower |
| content.fpRestoreFrequencyPowerSlope | - | integer | No | Reconnection Power Slope |
| content.fpRestoreFrequencyUperLimit | - | number | No | F(Stop) Upper |
| content.fpRestoreFrequencyWaitingTime | - | integer | No | Restore Waiting Time |
| content.fpUnderFrequencyLowerLimit | - | number | No | Under Frequency Start Point |
| content.fpUnderFrequencyPowerSlope | - | number | No | Under Frequency Power Slope |
| content.fpUnderFrequencyPowerSlopeForCharge | - | number | No | Under Frequency Power Slope For Charge |
| content.fpUnderFrequencyUpperLimit | - | number | No | Under Frequency End Point |
| content.gridPowerUnbalanceEnable | - | integer | No | Grid Power Unbalance |
| content.gridStandardCode | - | integer | No | Standard |
| content.gridWaveformDetectionMode | - | integer | No | Detection Mode |
| content.highVoltageCrossingTripThreshold | - | number | No | High Voltage Limit Of Ride Through |
| content.highVoltageEndPointTripTime | - | number | No | End Point Of Protection Time |
| content.highVoltageEndPointTripValue | - | number | No | End Point Of Ride Through |
| content.highVoltageRideThroughFunctionEnable | - | integer | No | High Voltage Ride Through Function |
| content.highVoltageStartPointTripTime | - | number | No | Start Point Of Protection Time |
| content.highVoltageStartPointTripValue | - | number | No | Start Point Of Ride Through |
| content.isoDetectionEnable | - | integer | No | ISO Detection |
| content.lcdBacklightEnable | - | integer | No | LCD Backlight, 0：Disable， 1：Enable |
| content.lowVoltageCrossingTripThreshold | - | number | No | Low Voltage Limit Of Ride Through |
| content.lowVoltageEndPointTripTime | - | number | No | End Point Of Protection Time |
| content.lowVoltageEndPointTripValue | - | number | No | End Point Of Ride Through |
| content.lowVoltageRideThroughFunctionEnable | - | integer | No | Low Voltage Ride Through |
| content.lowVoltageStartPointTripTime | - | number | No | Start Point Of Protection Time |
| content.lowVoltageStartPointTripValue | - | number | No | Start Point Of Ride Through |
| content.noBmsOffGridBatteryCutOffVoltage | - | number | No | Battery Cut-Off Voltage(Off-Grid, No Bms) |
| content.noBmsOffGridBatteryRestartVoltage | - | number | No | Battery Restart Voltage(Off-Grid, No Bms) |
| content.noBmsOnGridBatteryCutOffVoltage | - | number | No | Battery Cut-Off Voltage(On-Grid, No Bms) |
| content.onGridObservationTime | - | integer | No | Observation Time |
| content.onGridPowerLimit | - | number | No | Grid Power Limit |
| content.onGridPowerSlope | - | integer | No | Grid Power Slope |
| content.operatedMode | - | integer | No | Operated Mode, 0:General Mode, 1:Backup Mode, 2:Eco Mode |
| content.overFrequencyStage1TripTime | - | number | No | OF Stage1 Trip Time |
| content.overFrequencyStage1TripValue | - | number | No | OF Stage1 Trip Value |
| content.overFrequencyStage2TripTime | - | number | No | OF Stage2 Trip Time |
| content.overFrequencyStage2TripValue | - | number | No | OF Stage2 Trip Value |
| content.overLoadProtectionResetEnable | - | integer | No | Over Load Protection Reset, 0：Disable， 1：Enable |
| content.overVoltage10mTriggerValue | - | number | No | OV 10Min Mean Value |
| content.overVoltageStage1TripTime | - | number | No | OV Stage1 Trip Time |
| content.overVoltageStage1TripValue | - | number | No | OV Stage1 Trip Value |
| content.overVoltageStage2TripTime | - | number | No | OV Stage2 Trip Time |
| content.overVoltageStage2TripValue | - | number | No | OV Stage2 Trip Value |
| content.pfPowerCurveFunctionEnable | - | integer | No | PF-Power Curve Function |
| content.pfPowerCurveLockinVoltage | - | number | No | Lockin Voltage |
| content.pfPowerCurveLockoutPower | - | number | No | Lockout Power |
| content.pfPowerCurveLockoutVoltage | - | number | No | Lockout Voltage |
| content.pfPowerCurvePointAPower | - | number | No | Point A Power |
| content.pfPowerCurvePointAPowerFactor | - | number | No | Point A Power Factor |
| content.pfPowerCurvePointBPower | - | number | No | Point B Power |
| content.pfPowerCurvePointBPowerFactor | - | number | No | Point B Power Factor |
| content.pfPowerCurvePointCPower | - | number | No | Point C Power |
| content.pfPowerCurvePointCPowerFactor | - | number | No | Point C Power Factor |
| content.powerFactor | - | number | No | Power Factor |
| content.puCurveFunctionEnable | - | integer | No | P(U) Curve Function |
| content.puCurvePointAActivePower | - | number | No | Point A Active Power |
| content.puCurvePointAVoltage | - | number | No | Point A Voltage |
| content.puCurvePointBActivePower | - | number | No | Point B Active Power |
| content.puCurvePointBVoltage | - | number | No | Point B Voltage |
| content.puCurvePointCActivePower | - | number | No | Point C Active Power |
| content.puCurvePointCVoltage | - | number | No | Point C Voltage |
| content.puCurvePointDActivePower | - | number | No | Point D Active Power |
| content.puCurvePointDVoltage | - | number | No | Point D Voltage |
| content.pvParallelSetting | - | integer | No | PV Parallel Set |
| content.quCurveFunctionEnable | - | integer | No | Q(U) Curve Function |
| content.quCurveLockInPower | - | number | No | Lock In Power |
| content.quCurveLockOutPower | - | number | No | Lock Out Power |
| content.quCurvePointAReactivePower | - | number | No | Point A Reactive Power |
| content.quCurvePointAVoltage | - | number | No | Point A Voltage |
| content.quCurvePointBReactivePower | - | number | No | Point B Reactive Power |
| content.quCurvePointBVoltage | - | number | No | Point B Voltage |
| content.quCurvePointCReactivePower | - | number | No | Point C Reactive Power |
| content.quCurvePointCVoltage | - | number | No | Point C Voltage |
| content.quCurvePointDReactivePower | - | number | No | Point D Reactive Power |
| content.quCurvePointDVoltage | - | number | No | Point D Voltage |
| content.remoteOnOffEnable | - | integer | No | Remote ON/OFF, 0：Disable， 1：Enable |
| content.remoteOutputOnOffControl | - | integer | No | AC Output ON/OFF, 0：off, 1: on |
| content.underFrequencyStage1TripTime | - | number | No | UF Stage1 Trip Time |
| content.underFrequencyStage1TripValue | - | number | No | UF Stage1 Trip Value |
| content.underFrequencyStage2TripTime | - | number | No | UF Stage2 Trip Time |
| content.underFrequencyStage2TripValue | - | number | No | UF Stage2 Trip Value |
| content.underVoltageStage1TripTime | - | number | No | UV Stage1 Trip Time |
| content.underVoltageStage1TripValue | - | number | No | UV Stage1 Trip Value |
| content.underVoltageStage2TripTime | - | number | No | UV Stage2 Trip Time |
| content.underVoltageStage2TripValue | - | number | No | UV Stage2 Trip Value |
| content.zeroExportAdjustmentPower | - | integer | No | Zero Export Power |
| content.zeroExportFunction | - | integer | No | Zero Export Mode，1: To load, 2: To CT |
| content | - | object | Yes | setting content |
| deviceSn | - | string | Yes | Device serial number |
| content.ecoRule5 | - | object | Yes | Economic Mode Rule 5 Object, refer to content.ecoRule (Economic Mode Rule 1 Object) |
| content.ecoRule6 | - | object | Yes | Economic Mode Rule 6 Object, refer to content.ecoRule (Economic Mode Rule 1 Object) |
| content.ecoRule7 | - | object | Yes | Economic Mode Rule 7 Object, refer to content.ecoRule (Economic Mode Rule 1 Object) |
| content.ecoRule8 | - | object | Yes | Economic Mode Rule 8 Object, refer to content.ecoRule (Economic Mode Rule 1 Object) |
| content.ecoRule9 | - | object | Yes | Economic Mode Rule 9 Object, refer to content.ecoRule (Economic Mode Rule 1 Object) |
| content.ecoRule10 | - | object | Yes | Economic Mode Rule 10 Object, refer to content.ecoRule (Economic Mode Rule 1 Object) |

**Authentication Method**

> Inherit from parent

**Response Example**

* OK(200)

```javascript
{
  "code": 200,
  "message": "Success",
  "data": {
    "id": "9797479076789696",
    "deviceSn": "020505004822242582"
  }
}
```

| Parameter Name | Example Value | Parameter Type | Description |
| --- | --- | ---- | ---- |
| code | - | integer | code |
| message | - | string | message |
| data.deviceSn | - | string | Device serial number |
| data.id | - | integer | setting command id |
| data | - | object | - |

* token expired(200)

```javascript
{
  "code": 998,
  "message": "The token has expired, please log in again",
  "data": {}
}
```

| Parameter Name | Example Value | Parameter Type | Description |
| --- | --- | ---- | ---- |
| code | 998 | string | - |
| message | The token has expired, please log in again | string | - |
| data | {} | string | - |

* Permission Denied(200)

```javascript
{
  "code": 2001528,
  "message": "Insufficient permissions",
  "data": "Insufficient permissions"
}
```

* Failed(200)

```javascript
{
  "code": 1006051,
  "message": "Failed to send command.",
  "data": "Failed to send command."
}
```

**Request Header Parameters**

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| Content-Type | application/json | string | Yes | - |
| Authorization | Bearer_eyJhbGciOiJIUzI1NiJ9.eyJkZW1vVXNlciI6ZmFsc2UsInN1YiI6IueuoeeQhuWRmCIsImF1ZCI6Ik56TTNORFF4TkRrd01UVTFPREUwTkE9PSIsIm5iZiI6MTcxMTY3NjY4NiwiaXNzIjoiRkxTLVNPTEFSLVNFUlZFUiIsImlkIjo3Mzc0NDE0OTAxNTU4MTQ0LCJleHAiOjE3MTQyNjg2ODYsImlhdCI6MTcxMTY3NjY4Nn0._l5VIYevtyv2Xc66S9w6fqmkECBFvLZPJYqjU07pObE | string | Yes | User token, which can be obtained from authentication and refreshing tokens. |
| Lang | en_US | string | Yes | Language, currently supports English en_US. |

**Query**

## Remote Control Setting Attachment

> Created by: Timesup

> Updated by: Timesup

> Created at: 2024-08-16 08:12:28

> Updated at: 2025-03-13 14:27:46

### T-REX

**for T-REX-15KLP1G01、T-REX-8KLP1G01、T-REX-50KHP3G01, the request parameters as follows：**

| Key | Name | Range | unit | Required | Type | Description |
| --- | ---- | ----- | ---- | -------- | ---- | ----------- |
| batteryMode | Bat Mode | 0:Lithium1:Use Batt V  2:No bat |  | No | Number |  |
| batteryCapacity | Bat Capacity | 0~500 | AH | No | Number |  |
| batteryMaxChargedCurrent | Max A Charge | 0~55 | A | No | Number | Max battery charg current. Parallel bat1&bat2:if the inverter battery wiring ports are connect to one battery bank, please enable this function. |
| batteryMaxDischargeCurrent | Max A Discharge | 0~55 | A | No | Number | Max battery discharge current. Parallel bat1&bat2:if the inverter battery wiring ports are connect to one battery bank, please enable this function. |
| batteryParallelEnable | Parallel bat1&bat2 | 0:Stand Alone 1:Parallel |  | No | Number | Parallel bat1&bat2:if the inverter battery wiring ports are connect to one battery bank, please enable this function. |
| genAutoStartChargeSoc | GEN Auto Start Charge | 0~100 | % | No | Number | generator Auto Start Charge Soc |
| genAutoExitChargeSoc | GEN Exit Charge | 5~100 | % | No | Number | generator Auto Exit Charge Soc |
| gridChargeCurrent | Grid Charge Current | 0~55 | A | No | Number | grid Charge Current |
| genChargeCurrent | GEN Charge Current | 0~55 | A | No | Number | generator Charge Current |
| genStartSignalEnable | GEN Start Signal | 0:Disable  1:Enable |  | No | Number | generator Start Signal Enable,0: Disable, 1: Enable |
| genChargeEnable | Grid Charge Enable | 0:Disable  1:Enable |  | No | Number | It's allowed to use power fed from the grid port, which includes grid or generator connected to the grid port, to charge the battery. |
| gridChargeEnable | GEN Charge Enable | 0:Disable  1:Enable |  | No | Number | Use the power of generator to charge the battery. |
| gridAutoStartChargeVoltage | Grid Auto Start Charge Voltage | 150~800 | V | No | Number |  |
| gridAutoExitChargeVoltage | Grid Exit Charge Voltage | 150~800 | V | No | Number |  |
| genAutoStartChargeVoltage | GEN Auto Start Charge Voltage | 150~800 | V | No | Number | generator Auto Start Charge Voltage |
| genAutoExitChargeVoltage | GEN Exit Charge Voltage | 150~800 | V | No | Number | generator Auto Exit Charge Voltage |
| genMaxRunTime | GEN Max Run Time | 0~24 | hours | No | Number | generator Max Run Time |
| lithiumProtocol | Lithium Protocol | 0~20 |  | No | Number |  |
| batteryFloatingChargedVoltage | Bat float voltage | 150~800 | V | No | Number | Battery full charge voltage. |
| batteryRestartOutputVoltage | Bat Restart | 150~800 | V | No | Number | battery Restart Output Voltage |
| batteryLowVoltageAlarmVoltage | Bat Low Alarm | 150~800 | V | No | Number | battery Low Voltage Alarm Voltage |
| batteryShutdownVoltage | Bat Shutdown | 150~800 | V | No | Number | battery Shutdown Voltage |
| batteryRestartOutputSoc | Bat Restart | 0~100 | % | No | Number | battery Restart Output Soc |
| batteryLowVoltageAlarmSoc | Bat Low Alarm SOC | 0~100 | % | No | Number | battery Low Voltage Alarm Soc |
| batteryShutdownSoc | Bat Shutdown SOC | 0~100 | % | No | Number | battery Shutdown Soc |
| operatedMode | System Mode | 0:Selling Mode   1:Zero Export To Load   2:Zero Export To CT   3:Scheduling Mode |  | No | Number | Selling First: This Mode allows hybrid inverter to sell back any excess power produced by the solar panels to the grid. If Time Of Use is active, the battery energy also can be sold into grid.  The PV energy will be used to power the load and charge the battery and then excess energy will flow to grid.  Power source priority for the load is as follows:  1. Solar Panels.  2. Grid. when Energy Pattern tick Batt First.  Battery (until programable SOC discharge is reached). when Energy Pattern tick Load First and disable Grid charge.  Zero Export To Load: Hybrid inverter will only provide power to the backup load connected. The hybrid inverter will neither provide power to the home load nor sell power to grid. The built-in CT will detect power flowing back to the grid and will reduce the power of the inverter only to supply the backup load and charge the battery.  Zero Export To CT: Hybrid inverter will not only provide power to the backup load connected but also give power to the home load connected. If PV power and battery power is insufficient, it will take grid energy as supplement. The hybrid inverter will not sell power to grid. In this mode, a CT is needed. Please refer to manual CT connection for the installation method of CT. The external CT will detect power flowing back to the grid and will reduce the power of the inverter only to supply the backup load, charge battery and home load.  Scheduling mode: Based on system requirements and operating conditions, adjust the working status of the inverter and its coordinated operation with other devices through power allocation. Scheduling mode: Based on system requirements and operating conditions, adjust the working status of the inverter and its coordinated operation with other devices through power allocation" |
| zeroExportToLoadEnable | Solar Sell(to Load) | 0:Disable   1:Enable |  | No | Number | “Solar sell” is supplement for Zero Export To Load or Zero Export To CT: when this item is active, the surplus PV energy can be sold back to grid too. When it is active, PV Power source priority usage is as follows: load consumption and charge battery and feed into grid. |
| zeroExportToCtEnable | Solar Sell(to CT) | 0:Disable   1:Enable" |  | No | Number | “Solar sell” is supplement for Zero Export To Load or Zero Export To CT: when this item is active, the surplus PV energy can be sold back to grid too. When it is active, PV Power source priority usage is as follows: load consumption and charge battery and feed into grid. |
| dispatchActivePowerGiven | Active Power | -55~55 | KW | No | Number | "The charge power(Active Power greater than 0) or discharge power(Active Power less than 0) in the Scheduling mode.Reactive power can be set at Gird Setting/Connect" |
| maxSellingPower | Max. Sell power | 0~550 | KW | No | Number | max Selling Power |
| zeroExportHysteresisPower | Zero-export Power | -5000~5000 | W | No | Number | "For Zero Export To Load or Zero Export To CT, and the “Solar sell” is not active.   It tells the grid output power threshold to ensure the hybrid inverter won' t feed power to grid." |
| energyPriority | Energy Priority | 0:Bat First   1:Load First |  | No | Number | "Energy Pattern:Priority of PV power usage.   Batt First: PV power is firstly used to charge the battery and then used to power the load. If PV power is insufficient, grid will make supplement for battery and load simultaneously.  Load First: PV power is firstly used to power the load and then used to charge the battery. If PV power is insufficient, Grid will provide power to load, but neither the battery power to load nor the Grid charge to battery." |
| gridPeakShavingEnable | Grid Peak Shaving Enable | 0:Disable   1:Enable |  | No | Number | "Grid Peak Shaving:  1. To use Peak-Shaving on a generator, the equipment MUST be connected to the “GRID” terminal of the inverter.  2. Peak-Shaving helps reduce grid consumption during peak demand by utilizing battery backup power. It can also be used to prevent generator overload above a specified power threshold.  3. Install the CT sensors on grid / generator lines L1, L2. The arrows on the CTs MUST point toward  the GRID.  4. The T-REX INVERTER supplies power from the batteries whenever the “Power” threshold is met.  5. This mode will automatically adjust the ""Grid Charge” amperage (A) to avoid generator overloads during battery charging.  6. Grid Peak-Shaving will automatically enable “Time of Use” and MUST be configured." |
| gridPeakShavingPower | Grid Peak Shaving Power | 0~550 | KW | No | Number | grid Peak Shaving Power |
| timeOfUseEnable | Time Of Use | 0:Disable   1:Enable |  | No | Number | "Time Of Use: it is used to program when to use grid or generator to charge the battery, and when to discharge the battery to power the load. Only tick ""Time Of Use"" then the follow items (Grid, charge, time, power etc.) will take effect.  Note: when tick Selling First and click Time Of Use, the battery power can be sold into grid.   Charge Source: select grid or generator to charge the battery." |
| ecoRule1.gridChangingEnable | Grid Changing | 0:Disable  1:Enable |  | No | Number | Grid Changing1: Time Of Use Rule 1, grid Changing Enable, 0: Disable, 1: Enable |
| ecoRule1.genChangingEnable | Gen Changing | 0:Disable  1:Enable |  | No | Number | Gen Changing1: Time Of Use Rule 1, gen Changing Enable, 0: Disable, 1: Enable |
| ecoRule1.startTime | Start Time | HH:023  mm:059 |  | No | String | Start Time1: Time Of Use Rule 1, Starting time, Format: HH:mm |
| ecoRule1.stopTime | End Time | HH:023  mm:059 |  | No | String | End Time1: Time Of Use Rule 1, Stop time, Format: HH:mm |
| ecoRule1.voltage | Target Voltage | 150~750 | V | No | Number | Target Voltage 1: Time Of Use Rule 1，Battery charging or discharging voltage，Unit：V，It is related to the "Battery Model",Each Model The range of values is 48~60V |
| ecoRule1.soc | Target SOC | 0~100 | % | No | Number | Target SOC 1: Time Of Use Rule 1，Battery charging or discharging soc，Unit：%，The range of values is 0~100% |
| ecoRule1.power | INV Power | 0~50 | KW | No | Number | INV Power 1: Time Of Use Rule 1，Battery charging or discharging power,Unit：kW，The range of values is 0~ inverter rated power |
| ecoRule2.gridChangingEnable | Grid Changing | 0:Disable  1:Enable |  | No | Number | Grid Changing2: Time Of Use Rule 2, grid Changing Enable, 0: Disable, 1: Enable |
| ecoRule2.genChangingEnable | Gen Changing | 0:Disable   1:Enable |  | No | Number | Gen Changing2: Time Of Use Rule 2, gen Changing Enable, 0: Disable, 1: Enable |
| ecoRule2.startTime | Start Time | HH:023  mm:059 |  | No | String | Start Time2: Time Of Use Rule 2, Starting time, Format: HH:mm |
| ecoRule2.stopTime | End Time | HH:023  mm:059 |  | No | String | End Time2: Time Of Use Rule 2, Stop time, Format: HH:mm |
| ecoRule2.voltage | Target Voltage | 150~750 | V | No | Number | Target Voltage 2: Time Of Use Rule 2，Battery charging or discharging voltage，Unit：V，It is related to the "Battery Model",Each Model The range of values is 48~60V |
| ecoRule2.soc | Target SOC | 0~100 | % | No | Number | Target SOC 2: Time Of Use Rule 2，Battery charging or discharging soc，Unit：%，The range of values is 0~100% |
| ecoRule2.power | INV Power | 0~50 | KW | No | Number | INV Power 2: Time Of Use Rule 2，Battery charging or discharging power,Unit：kW，The range of values is 0~ inverter rated power |
| ecoRule3.gridChangingEnable | Grid Changing | 0:Disable   1:Enable |  | No | Number | Grid Changing3: Time Of Use Rule 3, grid Changing Enable, 0: Disable, 1: Enable |
| ecoRule3.genChangingEnable | Gen Changing | 0:Disable1:Enable |  | No | Number | Gen Changing3: Time Of Use Rule 3, gen Changing Enable, 0: Disable, 1: Enable |
| ecoRule3.startTime | Start Time | HH:023mm:059 |  | No | String | Start Time3: Time Of Use Rule 3, Starting time, Format: HH:mm |
| ecoRule3.stopTime | End Time | HH:023mm:059 |  | No | String | End Time3: Time Of Use Rule 3, Stop time, Format: HH:mm |
| ecoRule3.voltage | Target Voltage | 150~750 | V | No | Number | Target Voltage 3: Time Of Use Rule 3，Battery charging or discharging voltage，Unit：V，It is related to the "Battery Model",Each Model The range of values is 48~60V |
| ecoRule3.soc | Target SOC | 0~100 | % | No | Number | Target SOC 3: Time Of Use Rule 3，Battery charging or discharging soc，Unit：%，The range of values is 0~100% |
| ecoRule3.power | INV Power | 0~50 | KW | No | Number | INV Power 3: Time Of Use Rule 3，Battery charging or discharging power,Unit：kW，The range of values is 0~ inverter rated power |
| ecoRule4.gridChangingEnable | Grid Changing | 0:Disable1:Enable |  | No | Number | Grid Changing4: Time Of Use Rule 4, grid Changing Enable, 0: Disable, 1: Enable |
| ecoRule4.genChangingEnable | Gen Changing | 0:Disable1:Enable |  | No | Number | Gen Changing4: Time Of Use Rule 4, gen Changing Enable, 0: Disable, 1: Enable |
| ecoRule4.startTime | Start Time | HH:023mm:059 |  | No | String | Start Time4: Time Of Use Rule 4, Starting time, Format: HH:mm |
| ecoRule4.stopTime | End Time | HH:023mm:059 |  | No | String | End Time4: Time Of Use Rule 4, Stop time, Format: HH:mm |
| ecoRule4.voltage | Target Voltage | 150~750 | V | No | Number | Target Voltage 4: Time Of Use Rule 4，Battery charging or discharging voltage，Unit：V，It is related to the "Battery Model",Each Model The range of values is 48~60V |
| ecoRule4.soc | Target SOC | 0~100 | % | No | Number | Target SOC 4: Time Of Use Rule 4，Battery charging or discharging soc，Unit：%，The range of values is 0~100% |
| ecoRule4.power | INV Power | 0~50 | KW | No | Number | INV Power 4: Time Of Use Rule 4，Battery charging or discharging power,Unit：kW，The range of values is 0~ inverter rated power |
| ecoRule5.gridChangingEnable | Grid Changing | 0:Disable1:Enable |  | No | Number | Grid Changing5: Time Of Use Rule 5, grid Changing Enable, 0: Disable, 1: Enable |
| ecoRule5.genChangingEnable | Gen Changing | 0:Disable 1:Enable |  | No | Number | Gen Changing5: Time Of Use Rule 5, gen Changing Enable, 0: Disable, 1: Enable |
| ecoRule5.startTime | Start Time | HH:023 mm:059 |  | No | String | Start Time5: Time Of Use Rule 5, Starting time, Format: HH:mm |
| ecoRule5.stopTime | End Time | HH:023 mm:059 |  | No | String | End Time5: Time Of Use Rule 5, Stop time, Format: HH:mm |
| ecoRule5.voltage | Target Voltage | 150~750 | V | No | Number | Target Voltage 5: Time Of Use Rule 5，Battery charging or discharging voltage，Unit：V，It is related to the "Battery Model",Each Model The range of values is 48~60V |
| ecoRule5.soc | Target SOC | 0~100 | % | No | Number | Target SOC 5: Time Of Use Rule 5，Battery charging or discharging soc，Unit：%，The range of values is 0~100% |
| ecoRule5.power | INV Power | 0~50 | KW | No | Number | INV Power 5: Time Of Use Rule 5，Battery charging or discharging power,Unit：kW，The range of values is 0~ inverter rated power |
| ecoRule6.gridChangingEnable | Grid Changing | 0:Disable1:Enable |  | No | Number | Grid Changing6: Time Of Use Rule 6, grid Changing Enable, 0: Disable, 1: Enable |
| ecoRule6.genChangingEnable | Gen Changing | 0:Disable1:Enable |  | No | Number | Gen Changing6: Time Of Use Rule 6, gen Changing Enable, 0: Disable, 1: Enable |
| ecoRule6.startTime | Start Time | HH:023mm:059 |  | No | String | Start Time6: Time Of Use Rule 6, Starting time, Format: HH:mm |
| ecoRule6.stopTime | End Time | HH:023mm:059 |  | No | String | End Time6: Time Of Use Rule 6, Stop time, Format: HH:mm |
| ecoRule6.voltage | Target Voltage | 150~750 | V | No | Number | Target Voltage 6: Time Of Use Rule 6，Battery charging or discharging voltage，Unit：V，It is related to the "Battery Model",Each Model The range of values is 48~60V |
| ecoRule6.soc | Target SOC | 0~100 | % | No | Number | Target SOC 6: Time Of Use Rule 6，Battery charging or discharging soc，Unit：%，The range of values is 0~100% |
| ecoRule6.power | INV Power | 0~50 | KW | No | Number | INV Power 6: Time Of Use Rule 6，Battery charging or discharging power,Unit：kW，The range of values is 0~ inverter rated power |
| touEffectiveWeek | Week Of Use | MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY |  | No | Array | Week Of Use: Time Of Use Effective Week,Valuable：MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY，Multiple Choice |
| gridStandardCode | Standard | 0: Germany_VDE4105,2: General_Standard_50Hz,3: General_Standard_60Hz,4: Italy_CEI_021_2019,5: Britain_G99,6: Australia_A,7: NewZealand_AS4777,8: SouthAfrican_NRS097,9: Netherland_EN 50549-1,10: Brazil,11: EN50549,12: Poland_NC_RFG,13: Czech_CSN 50549-1,14: Austria_R25:2020-03,15: Austria_OVE-directive_R25,16: Spain_NTS_2021,17: Spain_UNE217001,18: cNetherland" |  | No | Number | State Grid regulations and standards, please set according to the power grid standards in your region |
| acOutputRatedVoltage | AC Output Rated Voltage | 380:380V400:400V | V | No | Number |  |
| acOutputRatedFrequency | AC Output Rated Frequency | 50:50Hz60:60Hz | HZ | No | Number |  |
| turnOnRampRate | Turn On Ramp Rate | 1~500 | %/S | No | Number | "It is the startup and reconnection power ramp, for example, Turn On Ramp Rate =100%/s, means the output power will increase from 0 to 100% rated power in 1s.Running P Ramp Rate: It is the power ramp response to the active power reference in normal running." |
| turnOffRampRate | Reconnection High Voltage | 1~500 | %/S | No | Number |  |
| runningActivePowerRampRate | Running P Ramp Rate | 1~500 | %/S | No | Number | It is the power ramp response to the active power reference in normal running |
| runningReactivePowerRampRate | Running Q Ramp Rate | 1~500 | %/S | No | Number |  |
| gridConnectionWaitTime | Reconnection Time | 1~600 | S | No | Number | The waiting time for the inverter connects the grid again after tripping. |
| reactivePowerControlMode | Q Mode | 0:Disable1:Const PF2:Const Q |  | No | Number | "Inverter response to the reactive power mode.Disable: not responding to the reactive power mode. Const PF: Inverter output a setting power factor(cos φ)value.Const Q: Inverter output a setting reactive power value." |
| reactivePowerGiven | Const Q | -7500~7500 | VA | No | Number | Setting the reactive power value. Const Q >0 means Inverter output capacitive reactive power, Const Q <0 means Inverter output Inductive reactive power. |
| powerFactorGiven | Const PF | -1-0.8,0.81 |  | No | Number | Setting the power factor(cos φ)value. Const PF>0 means Inverter output Inductive reactive power(or inverter will absorb capacitive reactive power from the power grid),Const PF<0 means Inverter output capacitive reactive power. |
| gridOverVoltageVoltage1 | High Voltage 1 | 105~150 | % | No | Number | Level 1 overvoltage protection point. |
| gridOverVoltageTime1 | HV1 Time | 0~655.35 | S | No | Number | Level 1 overvoltage protection time. |
| gridOverVoltageVoltage2 | HV2 | 105~150 | % | No | Number | Level 2 overvoltage protection point. |
| gridOverVoltageTime2 | HV2 Time | 0~655.35 | S | No | Number | Level 2 overvoltage protection time. |
| gridOverVoltageVoltage3 | HV3 | 105~150 | % | No | Number | Level 3 overvoltage protection point. |
| gridUnderVoltageVoltage1 | Low Voltage 1 | 5~95 | % | No | Number | Level 1 undervoltage protection point. |
| gridUnderVoltageTime1 | LV1 Time | 0~655.35 | S | No | Number | Level 1 undervoltage protection time. |
| gridUnderVoltageVoltage2 | LV2 | 5~95 | % | No | Number | Level 2 undervoltage protection point. |
| gridUnderVoltageTime2 | LV2 Time | 0~655.35 | S | No | Number | Level 2 undervoltage protection time. |
| gridUnderVoltageVoltage3 | LV3 | 5~95 | % | No | Number | Level 3 undervoltage protection point. |
| gridOverFrequencyFrequency1 | High Frequency 1 | 50~65 | HZ | No | Number | Level 1 over frequency protection point. |
| gridOverFrequencyTime1 | HF1 Time | 0~655.35 | S | No | Number | Level 1 over frequency protection time. |
| gridOverFrequencyFrequency2 | HF2 | 50~65 | HZ | No | Number | Level 2 over frequency protection point. |
| gridOverFrequencyTime2 | HF2 Time | 0~655.35 | S | No | Number | Level 2 over frequency protection protection time. |
| gridOverFrequencyFrequency3 | HF3 | 50~65 | HZ | No | Number | Level 3 over frequency protection point. |
| gridUnderFrequencyFrequency1 | Low Frequency1 | 45~60 | HZ | No | Number | Level 1 under frequency protection point. |
| gridUnderFrequencyTime1 | LF1 Time | 0~655.35 | S | No | Number | Level 1 under frequency protection time. |
| gridUnderFrequencyFrequency2 | LF2 | 45~60 | HZ | No | Number | Level 2 under frequency protection point. |
| gridUnderFrequencyTime2 | LF2 Time | 0~655.35 | S | No | Number | Level 2 under frequency protection protection time. |
| gridUnderFrequencyFrequency3 | LF3 | 45~60 | HZ | No | Number | Level 3 under frequency protection point. |
| fpResponseWorkModeEnable | F(P) | 0:Disable1:Enable |  | No | Number | It's used to adjust the output active power of inverter according to the grid frequency |
| fpResponseDelay | Start Delay T | 0~50000 | ms | No | Number | When the grid frequency reaches Start Over F, the inverter will activating active power response to over frequency after a dead time Start Delay T. |
| fpExitDelay | Stop Delay T | 0~50000 | ms | No | Number |  |
| fpOverFrequencyDeratingRatio | Droop Over F | -500~500 | %HZ | No | Number | "Decreases the power percentage of nominal power per Hz. For example, “Start Over F=50.2Hz, Stop Over F=51.2 Hz, Droop Over F =40%PE/Hz” ,define the current Grid Frequency is Fg, when the grid frequency reaches 50.2Hz, the inverter will decrease its active power at Droop of 40%. The total decrease active power=( Fg- Start Over F) * Droop Over F *Pn. when grid frequency is larger than 51.2Hz, the active power will stop decreasing." |
| fpOverFrequencyDeratingStart | Start Over F | 50~65 | HZ | No | Number | F(P) Over Frequency Derating Start |
| fpOverFrequencyDeratingEnd | Stop Over F | 50~65 | HZ | No | Number | F(P) Over Frequency Derating End |
| fpUnderFrequencyDeratingRatio | Droop Under F | -500~500 | %HZ | No | Number | F(P) Under Frequency Derating Ratio |
| fpUnderFrequencyDeratingStart | Start Under F | 45~60 | HZ | No | Number | F(P) Under Frequency Derating Start, Positive represents underfrequency upscaling, negative represents underfrequency downscaling. |
| fpUnderFrequencyDeratingEnd | Stop Under F | 45~60 | HZ | No | Number | F(P) Under Frequency Derating End |
| upDeratingWorkModeEnable | U(P) | 0:Disable1:Enable |  | No | Number | Active power response to Voltage deviation. |
| upDeratingVoltageA | U(P) V1 | 100~140 | % | No | Number | U(P) Derating Voltage A |
| upDeratingVoltageB | U(P) V2 | 100~140 | % | No | Number | U(P) Derating Voltage B |
| upDeratingVoltageC | U(P) V3 | 100~140 | % | No | Number | U(P) Derating Voltage C |
| upDeratingVoltageD | U(P) V4 | 100~140 | % | No | Number | U(P) Derating Voltage D |
| upDeratingActivePowerA | U(P) P1 | 0~110 | % | No | Number | U(P) Derating Active Power A |
| upDeratingActivePowerB | U(P) P2 | 0~110 | % | No | Number | U(P) Derating Active Power B |
| upDeratingActivePowerC | U(P) P3 | 0~110 | % | No | Number | U(P) Derating Active Power C |
| upDeratingActivePowerD | U(P) P4 | 0~110 | % | No | Number | U(P) Derating Active Power D |
| upDeratingDropRate | Enter P Rate | 0.01~500 | %/s | No | Number | U(P) Derating Drop Rate |
| upDeratingRecoveryRate | Exit P Rate | 0.01~500 | %/s | No | Number | U(P) Derating Recovery Rate |
| uqWorkModeEnable | U(Q) | 0:Disable 1:Enable |  | No | Number | Controls the reactive power output as a function of the voltage. |
| uqVoltageRiseStart | U(Q) V1 | 100~120 | % | No | Number | U(Q) Voltage Rise Start |
| uqVoltageRiseEnd | U(Q) V2 | 100~120 | % | No | Number | U(Q) Voltage Rise End |
| uqReactivePowerRiseStart | U(Q) V3 | 0~100 | % | No | Number | U(Q) Reactive Power Rise Start |
| uqReactivePowerRiseEnd | U(Q) V4 | 0~100 | % | No | Number | U(Q) Reactive Power Rise End |
| uqVoltageDropStart | U(Q) Q1 | 80~100 | % | No | Number | U(Q) Voltage Drop Start |
| uqVoltageDropEnd | U(Q) Q2 | 80~100 | % | No | Number | U(Q) Voltage Drop End |
| uqReactivePowerDropStart | U(Q) Q3 | 0~100 | % | No | Number | U(Q) Reactive Power Drop Start |
| uqReactivePowerDropEnd | U(Q) Q4 | 0~100 | % | No | Number | U(Q) Reactive Power Drop End |
| uqReactivePowerLockIn | U(Q)Lock_in/Pn | -100~100 | % | No | Number | U(Q) Reactive Power Lock-In |
| uqReactivePowerLockOut | U(Q)Lock_out/Pn | -100~100 | % | No | Number | U(Q) Reactive Power Lock-Out |
| pqWorkModeEnable | P(Q) | 0:Disable1:Enable |  | No | Number | Controls the reactive power of the output as a function of the active power output. 0: Disable, 1: Enable |
| pqActivePowerA | P(Q)P1 | 0~100 | % | No | Number | P(Q) Active Power A |
| pqActivePowerB | P(Q)P2 | 0~100 | % | No | Number | P(Q) Active Power B |
| pqActivePowerC | P(Q)P3 | 0~100 | % | No | Number | P(Q) Active Power C |
| pqActivePowerD | P(Q)P4 | 0~100 | % | No | Number | P(Q) Active Power D |
| pqReactiveActivePowerA | P(Q)Q1 | -100~100 | % | No | Number | P(Q) Reactive Active Power A |
| pqReactiveActivePowerB | P(Q)Q2 | -100~100 | % | No | Number | P(Q) Reactive Active Power B |
| pqReactiveActivePowerC | P(Q)Q3 | -100~100 | % | No | Number | P(Q) Reactive Active Power C |
| pqReactiveActivePowerD | P(Q)Q4 | -100~100 | % | No | Number | P(Q) Reactive Active Power D |
| ppfWorkModeEnable | P(PF) | 0:Disable1:Enable |  | No | Number | Controls the PF(cos φ) of the output as a function of the active power output. |
| ppfActivePowerA | P(PF)P1 | 0~100 | % | No | Number | P(PF) Active Power A |
| ppfActivePowerB | P(PF)P2 | 0~100 | % | No | Number | P(PF) Active Power B |
| ppfActivePowerC | P(PF)P3 | 0~100 | % | No | Number | P(PF) Active Power C |
| ppfActivePowerD | P(PF)P4 | 0~100 | % | No | Number | P(PF) Active Power D |
| ppfPowerFactorA | P(PF)PF1 | -100~100 | % | No | Number | P(PF) Power Factor A |
| ppfPowerFactorB | P(PF)PF2 | -100~100 | % | No | Number | P(PF) Power Factor B |
| ppfPowerFactorC | P(PF)PF3 | -100~100 | % | No | Number | P(PF) Power Factor C |
| ppfPowerFactorD | P(PF)PF4 | -100~100 | % | No | Number | P(PF) Power Factor D |
| ppfActivePowerLockIn | P(PF)Lock_in/Pn | 0~100 | % | No | Number | When the inverter output active power is higher then Lock-in/Pn rated power, it will enter the P(PF) mode. |
| ppfActivePowerLockOut | P(PF)Lock_out/Pn | 0~100 | % | No | Number | When the inverter output active power is lower then Lock-out/Pn rated power, it will exit the P(PF) mode. |
| upfWorkModeEnable | U(PF) | 0:Disable 1:Enable |  | No | Number | Controls the PF(cos φ) of the output to the Voltage deviation. |
| upfVoltageRiseStart | U(PF)U1 | 0~120 | % | No | Number | U(PF) Voltage Rise Start |
| upfVoltageRiseEnd | U(PF)U2 | 0~120 | % | No | Number | U(PF) Voltage Rise End |
| upfPowerFactorDropStart | U(PF)PF1 | -100~100 | % | No | Number | U(PF) Power Factor Drop Start |
| upfPowerFactorDropEnd | U(PF)PF2 | -100~100 | % | No | Number | U(PF) Power Factor Drop End |
| fgWorkModeEnable | F(G) | 0:Disable1:Enable |  | No | Number | Controls the active power output to the grid frequency deviation. |
| fgUnderFrequencyToDischargeFrequency | Discharge Under F | 45~60 | HZ | No | Number | Discharge Under F: F(G) Under Frequency To Discharge Frequency |
| fgUnderFrequencyToDischargePercentage | Discharge Under P | 0~100 | % | No | Number | Discharge Under P: F(G) Under Frequency To Discharge Percentage |
| fgOverFrequencyToCchargeFrequency | Charge Over F | 50~65 | HZ | No | Number | Charge Over F: F(G) Over Frequency To Ccharge Frequency |
| fgOverFrequencyToChargePercentage | Charge Over P | -100~0 | % | No | Number | Charge Over P: F(G) Over Frequency To Charge Percentage |
| lowVoltageRideThroughEnable | LVRT | 0:Disable 1:Enable |  | No | Number | Low Voltage Ride Through enable |
| lvrtDynamicReactivePowerKfFactor | L_Kf | 0~4 |  | No | Number | Dynamic reactive power factor in LVRT. if the local grid code requires dynamic reactive power support capability in grid low voltage, and the grid voltage is lower than LVRT1 value, the inverter will output reactive current Iq= L_Kf*(Vgrid – LVRT1)*In. |
| highVoltageRideThroughEnable | HVRT | 0:Disable1:Enable |  | No | Number | High Voltage Ride Through enable |
| hvrtDynamicReactivePowerKfFactor | H_Kf | 0~4 |  | No | Number | Dynamic reactive power factor in HVRT. if the local grid code requires dynamic reactive power support capability in grid high voltage, and the grid voltage is higher than HVRT1 value, the inverter will output reactive current Iq= H_Kf*(Vgrid – HVRT1) *In. |
| lvrtVoltage1 | LVRT V1 | 5~90 | % | No | Number | Level 1 undervoltage protection point and enter LVRT Voltage point |
| lvrtTime1 | LVRT T1 | 0~655.35 | S | No | Number | Level 1 undervoltage and enter LVRT Voltage protection time; |
| lvrtVoltage2 | LVRT V2 | 5~90 | % | No | Number | Level 2 undervoltage protection point. |
| lvrtTime2 | LVRT T2 | 0~655.35 | S | No | Number | Level 2 undervoltage protection time. |
| lvrtVoltage3 | LVRT V3 | 5~90 | % | No | Number | Level 3 undervoltage protection point and enter LVRT Voltage point |
| lvrtTime3 | LVRT T3 | 0~655.35 | S | No | Number | Level 3 undervoltage and enter LVRT Voltage protection time; |
| lvrtVoltage4 | LVRT V4 | 5~90 | % | No | Number | Level 4 undervoltage protection point and enter LVRT Voltage point |
| lvrtTime4 | LVRT T4 | 0~655.35 | S | No | Number | Level 4 undervoltage and enter LVRT Voltage protection time; |
| lvrtVoltage5 | LVRT V5 | 5~90 | % | No | Number | Level 5 undervoltage protection point and enter LVRT Voltage point |
| lvrtTime5 | LVRT T5 | 0~655.35 | S | No | Number | Level 5 undervoltage and enter LVRT Voltage protection time; |
| hvrtVoltage1 | HVRT V1 | 110~140 | % | No | Number | Level 1 overvoltage protection point and enter HVRT Voltage point |
| hvrtTime1 | HVRT T1 | 0~655.35 | S | No | Number | Level 1 overvoltage protection and enter HVRT Voltage protection time |
| hvrtVoltage2 | HVRT V2 | 110~140 | % | No | Number | Level 2 overvoltage protection point |
| hvrtTime2 | HVRT T2 | 0~655.35 | S | No | Number | Level 2 overvoltage protection time |
| hvrtVoltage3 | HVRT V3 | 110~140 | % | No | Number | Level 3 overvoltage protection point and enter HVRT Voltage point |
| hvrtTime3 | HVRT T3 | 0~655.35 | S | No | Number | Level 3 overvoltage protection and enter HVRT Voltageprotection time |
| hvrtVoltage4 | HVRT V4 | 110~140 | % | No | Number | Level 4 overvoltage protection point and enter HVRT Voltage point |
| hvrtTime4 | HVRT T4 | 0~655.35 | S | No | Number | Level 4 overvoltage protection and enter HVRT Voltageprotection time |
| hvrtVoltage5 | HVRT V5 | 110~140 | % | No | Number | Level 5 overvoltage protection point and enter HVRT Voltage point |
| hvrtTime5 | HVRT T5 | 0~655.35 | S | No | Number | Level 5 overvoltage protection and enter HVRT Voltageprotection time |
| smartPortModeEnable | Smart Port Mode | 0:Generator1:Smart Load2:Micro Inv |  | No | Number | Generator:Use the GEN port as an generator port.Smart Load Output: Use the GEN port as an AC output port, and the load connected to this port can be controlledon/off by the hybrid inverter.Micro inv input:Use the GEN port as an AC couple input port which can be connected with micro-inverter or other Grid-Tied inverter. |
| genRatePower | GEN Rate Power | 0~500 | KW | No | Number | Allowed Max. power from generator. |
| genInputPowerLimitEnable | GEN Peak-shaving | 0:Disable1:Enable |  | No | Number | Limit the maximum output power of the generator to the set rated power on "GEN PORT USE" page, the rest of power consumption will be provided by inverter to ensure that the generator will not overload. |
| genConnectGridEnable | Generator Connect to Grid Port | 0:Disable 1:Enable |  | No | Number | When the oil engine mode is intelligent load output and the battery energy is high, additional excess power is allowed |
| smartLoadNormalCloseEnable | Smart Load Output | 0:Disable1:Enable |  | No | Number | Use the GEN port as an AC output port, and the load connected to this port can be controlled on/off by the hybrid inverter.e.g.ON: 100%,OFF: 95%: When the battery bank SOC reaches 100%, Smart Load Port will switch on automatically and power the load connected. when the battery bank SOC < 95% , the Smart Load Port will switch off automatically |
| smartLoadCloseBatteryVoltage | Smart Load ON Bat Voltage | 150~800 |  | No | Number | When the oil engine mode is intelligent load output and the battery energy is high, additional excess power is allowed |
| smartLoadOpenBatteryVoltage | Smart Load OFF Bat Voltage | 150~800 |  | No | Number | smart Load Open Battery Voltage |
| smartLoadCloseBatterySoc | Smart Load ON Bat SOC | 0~100 | % | No | Number | Smart Load ON Battery SOC point, Battery SOC at which the Smart load will switch on. |
| smartLoadOpenBatterySoc | Smart Load OFF Bat SOC | 0~100 | % | No | Number | Smart Load OFF Bat SOC: Smart Load OFF Battery SOC point, Battery SOC at which the Smart load will switch off. |
| genOverVoltageVoltage1 | GEN High Voltage1 | 105~150 | % | No | Number | Level 1 overvoltage protection point. |
| genOverVoltageTime1 | GEN HV1 Time | 0~655.35 | S | No | Number | Level 1 overvoltage protection time. |
| genOverVoltageVoltage2 | GEN HV2 | 105~150 | % | No | Number | Level 2 overvoltage protection point. |
| genOverVoltageTime2 | GEN HV2 Time | 0~655.35 | S | No | Number | Level 2 overvoltage protection time. |
| genUnderVoltageVoltage1 | GEN Low Voltage1 | 10~95 | % | No | Number | Level 1 undervoltage protection point. |
| genUnderVoltageTime1 | GEN LV1 Time | 0~655.35 | S | No | Number | Level 1 undervoltage protection point. |
| genUnderVoltageVoltage2 | GEN LV2 | 10~95 | % | No | Number | Level 2 undervoltage protection point. |
| genUnderVoltageTime2 | GEN LV2 Time | 0~655.35 | S | No | Number | Level 2 undervoltage protection point. |
| genOverFrequencyFrequency1 | GEN High Frequency 1 | 50~65 | HZ | No | Number | Level 1 over frequency protection point. |
| genOverFrequencyTime1 | GEN HF1 Time | 0~655.35 | S | No | Number | Level 1 over frequency protection time. |
| genOverFrequencyFrequency2 | GEN HF2 | 50~65 | HZ | No | Number | Level 2 over frequency protection point. |
| genOverFrequencyTime2 | GEN HF2 Time | 0~655.35 | S | No | Number | Level 2 over frequency protection time. |
| genUnderFrequencyFrequency1 | GEN Low Frequency1 | 45~60 | HZ | No | Number | Level 1 under frequency protection point. |
| genUnderFrequencyTime1 | GEN LF1 Time | 0~655.35 | S | No | Number | Level 1 under frequency protection time. |
| genUnderFrequencyFrequency2 | GEN LF2 | 45~60 | HZ | No | Number | Level 2 under frequency protection point. |
| genUnderFrequencyTime2 | GEN LF2 Time | 0~655.35 | S | No | Number | Level 2 under frequency protection time. |
| drmEnable | DRM | 0:Disable1:Enable |  | No | Number | For AS4777 standard |
| ctRatio | CT Ratio | 0~10000 |  | No | Number | The CT ratio of the zero-export to CT mode. |
| leakageCurrentGfciProtectionEnable | GFCI | 0:Disable1:Enable |  | No | Number | The ground-fault circuit interrupter function. |
| leakageCurrentGfciProtectionThreshold | GFCI Value | 0~1000 | mA | No | Number | Leakage current protection point. |
| isoCheckEnable | ISO | 0:Disable1:Enable |  | No | Number | The PV and the battery wiring terminals Positive to ground and negative to ground insulation impedance detection. |
| isoCheckThreshold | ISO Value | 0~2000 | KΩ | No | Number | Insulation impedance protection point. |
| activeIslandingProtectionEnable | Active Islanding | 0:Disable1:Enable |  | No | Number | Active islanding detection enable or not. |
| offGridVoltageCompensation | Voltage Adjust | -20~20 | V | No | Number | If the inverter is working at off grid, we can adjust the output voltage by Voltage Adjust. |
| asymmetricPhaseFeedingEnable | Asymmetric Feeding | 0:Disable1:Enable |  | No | Number | If it was clicked, the inverter will take power from the grid balance of on each phase (L1/L2/L3). |
| machineId | CAN ID | 1~10 |  | No | Number | machine Id |
| dspParallelEnable | Parallel | 0:Disable 1:Enable |  | No | Number | "If user want to parallel operation to Expand system capacity, we need to click the parallel. And in a parallel system, we can have and must have only one Master, and the others must be set as Slaver, and we need to set a unique CAN ID to each inverter, the CAN ID is from 1 to 10." |
| masterSlaverSetting | Master&Slaver | 0:Master1:Slaver |  | No | Number |  |
| factoryReset | Factory Reset | 1:Reset |  | No | Number |  |
| remoteOnOffEnable | Remote control | 0:Turn ON1:Turn OFF |  | No | Number |  |
| clearEnergyStorageLog | Clear Energy Storage Log | 1:Clear |  | No | Number |  |
| genForceRunningEnable | GEN Force | 0:Disable1:Enable |  | No | Number |  |
| zeroExportModeSelection | Zero Export Mode | 0:CT1:Meter |  | No | Number |  |
| gridAutoStartChargeSoc | Grid Auto Start Charge | 0~100 | % | No | Number |  |
| gridAutoExitChargeSoc | Grid Exit Charge | 5~100 | % | No | Number |  |
| gridAutoStartChargeVoltage | Grid Auto Start Charge Voltage | 150~800 | V | No | Number |  |
| gridAutoExitChargeVoltage | Grid Exit Charge Voltage | 150~800 | V | No | Number |  |
| gridStartSignal | Grid Signal | 0:Disable1:Enable |  | No | Number |  |
| genDownTime | Gen Down Time | 0~24 | hours | No | Number |  |
| maxPvInputPower | Max Solar Power | 0~65000 | W | No | Number |  |
| meterSelection | Meter Selection | 0:No electricity meter1:CHNT2:Eastron |  | No | Number |  |
| electricMeterBaudRate | Electric Meter Baud Rate | 0:96001:192002:38400 |  | No | Number |  |
| grid10MinOverVoltageThreshold | 10-Min OV Threshold Grid | 0~200 | % | No | Number |  |
| gridPhaseType | Phase Type | 0:Positive sequence1:Reverse order |  | No | Number |  |
| iTSystem | IT System | 0:Disable1:Enable |  | No | Number |  |
| gridNormalConnectionOvervoltage | High Voltage | 105~150 | % | No | Number |  |
| gridNormalConnectionUndervoltage | Low Voltage | 10~95 | % | No | Number |  |
| gridNormalConnectionOverFrequency | High Frequency | 50~65 | HZ | No | Number |  |
| gridNormalConnectionUnderFrequency | Low Frequency | 45~60 | HZ | No | Number |  |
| gridReconnectionOvervoltage | Reconnection High Voltage | 105~150 | % | No | Number |  |
| gridNormalConnectionUndervoltage | Reconnection Low Voltage | 10~95 | % | No | Number |  |
| gridNormalConnectionOverFrequency | Reconnection High Frequency | 50~65 | HZ | No | Number |  |
| gridNormalConnectionUnderFrequency | Reconnection Low Frequency | 45~60 | HZ | No | Number |  |
| acCoupleFrequencyHigh | AC Couple Frz High | 50~65 | HZ | No | Number |  |
| acCoupleToGridOrLoad | AC Couple to Grid or Load | 0:Disable1:Grid2:Load |  | No | Number |  |
| microInvColseBatVoltage | Micro Inv Closed Bat. Volt. | 150~800 | V | No | Number |  |
| microInvOpenBatVoltage | Micro Inv Open Bat. Volt. | 150~800 | V | No | Number |  |
| microInvColseBatSoc | Micro Inv Closed SOC | 0~100 | % | No | Number |  |
| microInvOpenBatSoc | Micro Inv Open SOC | 0~100 | % | No | Number |  |
| backUpDelay | BackUp Delay | 0~60000 | ms | No | Number |  |
| signalIslandModeEnable | Signal Island Mode | 0:Disable1:Enable |  | No | Number |  |
| faultClearanceAndRestart | Fault Clearance and Restart | 0:Disable1:Enable |  | No | Number |  |

### IVGM100600

| Key | Name | Range | unit | Required | Type | Description |
| --- | ---- | ----- | ---- | -------- | ---- | ----------- |
| acOutputRatedVoltage | AC Output Rated Voltage | 220:220V  230:230V  240:240V | V | NO | Number |  |
| acOutputRatedFrequency | AC Output Rated Frequency | 0:50Hz  1:60Hz | Hz | NO | Number |  |
| gridPowerUnbalanceEnable | Grid Power Unbalance | 0:Disable  1:Enable |  | NO | Number |  |
| powerFactor | Power Factor | -0.99-0.8,0.81 |  | NO | Number |  |
| gridWaveformDetectionMode | Detection Mode | 0:Wave Detect  1:Half Wave Detect  2:Disable Wave Detect |  | NO | Number |  |
| batteryModel | Battery Model | 0:User defined  1:Third party(Lithium battery)  2:Felicity(LPBF/LUX-X series)  3:Felicity(LPBA/LUX-Y/LUX-E  series) |  | NO | Number |  |
| batteryOnGridDischargeDepthSoc | Battery Discharged Depth(On-Grid, Bms Connected) | 10~100 | % | NO | Number | The battery SOC is lower than the battery on-grid discharge depth, and the battery stops discharging |
| batteryOffGridDischargeDepthSoc | Battery Discharged Depth(Off-Grid, Bms Connected) | 0~100 | % | NO | Number | The battery SOC is lower than the battery off-grid discharge depth, and the battery stops discharging |
| batteryOffGridRecoveryDepthSoc | Battery Restart Depth(Off-Grid, Bms Connected) | 0~100 | % | NO | Number | When the battery SOC is lower than the setting value of "Battery discharge depth (off grid)", the inverter can only be output off the grid again after the SOC recovers to the setting value higher than "Battery restart depth |
| lcdBacklightEnable | LCD Backlight | 0:Disable  1:Enable |  | NO | Number |  |
| buzzerEnable | Buzzer | 0:Disable  1:Enable |  | NO | Number |  |
| overLoadProtectionResetEnable | Over Load Protection Reset | 0:Disable  1:Enable |  | NO | Number | The fault will be cleared automatically after the overload protection of the machine. If the overload protection occurs 3 times within half an hour, the overload fault will not be cleared |
| remoteOnOffEnable | Remote control | 0:ON  1:OFF |  | NO | Number | The machine shuts down and enters standby mode |
| remoteOutputOnOffControl | AC Output ON/OFF | 0:ON  1:OFF |  | NO | Number |  |
| zeroExportFunction | Zero Export Mode | 1:To load  2:To CT |  | NO | Number | "The feed power is limited according to the setting of ""grid connection power limit"".1) To load:The inverter can supply power to the backup load and sell power to the grid but the selling power will not exceed the setting value of ""grid connection power limit""2) To CT:The inverter can supply power to the backup load, household load and sell power to the grid, but the selling power will not exceed the setting value of ""grid connection power limit"".In this mode, a CT is needed." |
| zeroExportAdjustmentPower | Zero Export Power | -500~500 | W | NO | Number | When the grid-connected power is set to 0, it is used to calibrate the sampling deviation to ensure that the inverter will not feed power to the grid |
| clearEnergyStorageLog | Clear Energy Storage Log | 1:Clear |  | NO | Number |  |
| clearEventLog | Clear Event Log | 1:Clear |  | NO | Number |  |
| factoryReset | Factory Reset | 1:Reset |  | NO | Number |  |
| eventLogFunctionEnable | Event Log Function | 0:Disable  1:Charge  2:Discharge |  | NO | Number |  |
| faultLogFunctionEnable | Fault Log Function | 0:Disable  1:Charge  2:Discharge |  | NO | Number |  |
| gfciLevel1ProtectionEnable | GFCI One-level Protection | 0:Disable  1:Charge  2:Discharge |  | NO | Number |  |
| gfciLevel2ProtectionEnable | GFCI Two-level Protection | 0:Disable  1:Charge  2:Discharge |  | NO | Number |  |
| gfciLevel3ProtectionEnable | GFCI Three-level Protection | 0:Disable  1:Charge  2:Discharge |  | NO | Number |  |
| isoDetectionEnable | ISO Detection | 0:Disable  1:Charge  2:Discharge |  | NO | Number |  |
| antiIslandingDetectionEnable | Anti-Islanding Detection | 0:Disable  1:Charge  2:Discharge |  | NO | Number |  |
| pvParallelSetting | PV Parallel Set | 0:Stand Alone  1:Parallel |  | NO | Number |  |
| fixQPencent | FixQ Pencent | -60~60 | % | NO | Number |  |
| bmsHeartbeat | BMS Heartbeat | 0:Disable  1:Charge  2:Discharge |  | NO | Number | After enabling, if the battery type is lithium battery and BMS communication fails, it will report BMS communication failure |
| operatedMode | Operated Mode | 0:General Mode  1:Backup Mode  2:Eco Mode  3:Gen Mode |  | NO | Number | "Set inverter operation mode:1) General mode:In this mode, the load is mainly powered by PV and battery.2) Backup mode:In this mode, PV gives priority to charging the battery to ensure that the battery is always full.3) ECO mode:In this mode, you can set a specific time to take power from the grid to charge the battery or use the power of the grid to charge the battery, and operate in general mode outside the set time.4) Generator mode:In this mode, the load is mainly powered by PV and battery." |
| ecoRule1.ruleMode | ECO Mode 1 | 0:Disable  1:Charge  2:Discharge   3:AC Couple |  | NO | Number | "Economic model rules:1) Disable: No charging and discharging2) Charge: Charge the battery from the grid3) Discharge: Selling power from battery to the grid4)AC Couple:Spontaneous self-use, waste electricity Internet access" |
| ecoRule1.startTime | Start Time1 | HH:023 mm:059 |  | NO | String | Starting time, Format: HH:mm |
| ecoRule1.stopTime | Stop Time1 | HH:023 mm:059 |  | NO | String | Stop time, Format: HH:mm |
| ecoRule1.startDay | Start Day1 | MM:112 dd:131 |  | NO | String | Starting day, Format: MM:dd |
| ecoRule1.stopDay | Stop Day1 | MM:112 dd:131 |  | NO | String | Stop day, Format: MM:dd |
| ecoRule1.daysOfEffectiveWeek | Effective Week1 | MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY |  | NO | Array | Week Of Use: Time Of Use Effective Week,Valuable：MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY，Multiple Choice |
| ecoRule1.soc | SOC1 | 0~100 | % | NO | Number |  |
| ecoRule1.voltage | Voltage1 | 48~60 | V | NO | Number | "1) Charging: Stop charging voltage. Battery voltage above this value stops charging (usually set to 57.6v for a single battery).2) Discharge: Stop discharge voltage. If the battery voltage is lower than this value, it will stop discharging." |
| ecoRule1.power | Power1 | "Master Version <212 : 010000Master Version ≥212 : -1000010000" | W | NO | Number | "1) Charging: Battery charging power2) Discharge: Battery discharge power3)Dispatched power: Grid power supply or intake power" |
| ecoRule2.ruleMode | ECO Mode 2 | 0:Disable  1:Charge  2:Discharge   3:AC Couple |  | NO | Number | "Economic model rules:1) Disable: No charging and discharging2) Charge: Charge the battery from the grid3) Discharge: Selling power from battery to the grid4)AC Couple:Spontaneous self-use, waste electricity Internet access" |
| ecoRule2.startTime | Start Time2 | HH:023 mm:059 |  | NO | String | Starting time, Format: HH:mm |
| ecoRule2.stopTime | Stop Time2 | HH:023 mm:059 |  | NO | String | Stop time, Format: HH:mm |
| ecoRule2.startDay | Start Day2 | MM:112 dd:131 |  | NO | String | Starting day, Format: MM:dd |
| ecoRule2.stopDay | Stop Day2 | MM:112 dd:131 |  | NO | String | Stop day, Format: MM:dd |
| ecoRule2.voltage | Voltage2 | 48~60 | V | NO | Number | "1) Charging: Stop charging voltage. Battery voltage above this value stops charging (usually set to 57.6v for a single battery).2) Discharge: Stop discharge voltage. If the battery voltage is lower than this value, it will stop discharging." |
| ecoRule2.power | Power2 | "Master Version <212 : 010000Master Version ≥212 : -1000010000" | W | NO | Number | "1) Charging: Battery charging power2) Discharge: Battery discharge power3)Dispatched power: Grid power supply or intake power" |
| ecoRule2.daysOfEffectiveWeek | Effective Week2 | MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY |  | NO | Array | Week Of Use: Time Of Use Effective Week,Valuable：MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY，Multiple Choice |
| ecoRule2.soc | SOC2 | 0~100 | % | NO | Number |  |
| ecoRule3.ruleMode | ECO Mode 3 | 0:Disable  1:Charge  2:Discharge   3:AC Couple |  | NO | Number | "Economic model rules:1) Disable: No charging and discharging2) Charge: Charge the battery from the grid3) Discharge: Selling power from battery to the grid4)AC Couple:Spontaneous self-use, waste electricity Internet access" |
| ecoRule3.startTime | Start Time3 | HH:023 mm:059 |  | NO | String | Starting time, Format: HH:mm |
| ecoRule3.stopTime | Stop Time3 | HH:023 mm:059 |  | NO | String | Stop time, Format: HH:mm |
| ecoRule3.startDay | Start Day3 | MM:112 dd:131 |  | NO | String | Starting day, Format: MM:dd |
| ecoRule3.stopDay | Stop Day3 | MM:112 dd:131 |  | NO | String | Stop day, Format: MM:dd |
| ecoRule3.daysOfEffectiveWeek | Effective Week3 | MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY |  | NO | Array | Week Of Use: Time Of Use Effective Week,Valuable：MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY，Multiple Choice |
| ecoRule3.soc | SOC3 | 0~100 | % | NO | Number |  |
| ecoRule3.voltage | Voltage3 | 48~60 | V | NO | Number | "1) Charging: Stop charging voltage. Battery voltage above this value stops charging (usually set to 57.6v for a single battery).2) Discharge: Stop discharge voltage. If the battery voltage is lower than this value, it will stop discharging." |
| ecoRule3.power | Power3 | "Master Version <212 : 010000Master Version ≥212 : -1000010000" | W | NO | Number | "1) Charging: Battery charging power2) Discharge: Battery discharge power3)Dispatched power: Grid power supply or intake power" |
| ecoRule4.ruleMode | ECO Mode 4 | 0:Disable  1:Charge  2:Discharge   3:AC Couple |  | NO | Number | "Economic model rules:1) Disable: No charging and discharging2) Charge: Charge the battery from the grid3) Discharge: Selling power from battery to the grid4)AC Couple:Spontaneous self-use, waste electricity Internet access" |
| ecoRule4.startTime | Start Time4 | HH:023 mm:059 |  | NO | String | Starting time, Format: HH:mm |
| ecoRule4.stopTime | Stop Time4 | HH:023 mm:059 |  | NO | String | Stop time, Format: HH:mm |
| ecoRule4.startDay | Start Day4 | MM:112 dd:131 |  | NO | String | Starting day, Format: MM:dd |
| ecoRule4.stopDay | Stop Day4 | MM:112 dd:131 |  | NO | String | Stop day, Format: MM:dd |
| ecoRule4.voltage | Voltage4 | 48~60 | V | NO | Number | "1) Charging: Stop charging voltage. Battery voltage above this value stops charging (usually set to 57.6v for a single battery).2) Discharge: Stop discharge voltage. If the battery voltage is lower than this value, it will stop discharging." |
| ecoRule4.power | Power4 | "Master Version <212 : 010000Master Version ≥212 : -1000010000" | W | NO | Number | "1) Charging: Battery charging power2) Discharge: Battery discharge power3)Dispatched power: Grid power supply or intake power" |
| ecoRule4.daysOfEffectiveWeek | Effective Week4 | MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY |  | NO | Array | Week Of Use: Time Of Use Effective Week,Valuable：MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY，Multiple Choice |
| ecoRule4.soc | SOC4 | 0~100 | % | NO | Number |  |
| batteryModules | Battery Modules | 4~10 |  | NO | Number |  |
| batteryChargedVoltage | Battery Charged Voltage | 48~60 | V | NO | Number |  |
| batteryFloatingChargedVoltage | Bat float voltage | 48~60 | V | NO | Number |  |
| noBmsOnGridBatteryCutOffVoltage | Battery Cut-Off Voltage(On-Grid, No Bms) | 40~60 | V | NO | Number |  |
| noBmsOffGridBatteryCutOffVoltage | Battery Cut-Off Voltage(Off-Grid, No Bms) | 40~60 | V | NO | Number |  |
| noBmsOffGridBatteryRestartVoltage | Battery Restart Voltage(Off-Grid, No Bms) | 40~60 | V | NO | Number |  |
| batteryMaxChargedCurrent | Battery Max. Charged Current | 1~25 | A | NO | Number |  |
| batteryMaxDischargeCurrent | Battery Max. Discharged Current | 5~25 | A | NO | Number |  |
| --- | --- | --- | --- | --- | --- | --- |
| gridStandardCode | Standard | 0:Germany  1:Warehouse  2:50Hz grid default  3:60Hz grid default  4:Italy  5:Britain  6:Australia  7:New Zealand  8:South African  9:Netherland  10:Brazil  11:Europe  12:Poland  13:Czech |  | No | Number | Set the on-grid regulations in the current region |
| overVoltageStage1TripTime | OV Stage1 Trip Time | 0.02~1000 | Sec | No | Number |  |
| underVoltageStage1TripTime | UV Stage1 Trip Time | 0.02~1000 | Sec | No | Number |  |
| overVoltageStage2TripTime | OV Stage2 Trip Time | 0.02~1000 | Sec | No | Number |  |
| underVoltageStage2TripTime | UV Stage2 Trip Time | 0.02~1000 | Sec | No | Number |  |
| overVoltage10mTriggerValue | OV 10Min Mean Value | 230~300 | V | No | Number |  |
| overFrequencyStage1TripTime | OF Stage1 Trip Time | 0.02~1000 | Sec | No | Number |  |
| underFrequencyStage1TripTime | UF Stage1 Trip Time | 0.02~1000 | Sec | No | Number |  |
| overFrequencyStage2TripTime | OF Stage2 Trip Time | 0.02~1000 | Sec | No | Number |  |
| underFrequencyStage2TripTime | UF Stage2 Trip Time | 0.02~1000 | Sec | No | Number |  |
| onGridObservationTime | Observation Time | 1~3000 | Sec | No | Number |  |
| onGridPowerSlope | Grid Power Slope | 0~65535 | Sec | No | Number |  |
| onGridPowerLimit | Grid Power Limit | 0~100 | % | No | Number |  |
| pfPowerCurveFunctionEnable | PF-Power Curve Function | 0:Disable  1:Enable |  | No | Number |  |
| pfPowerCurvePointAPower | Point A Power | 0~100 | % | No | Number |  |
| pfPowerCurvePointAPowerFactor | Point A Power Factor | -0.99-0.8,0.81 |  | No | Number |  |
| pfPowerCurvePointBPower | Point B Power | 0~100 | % | No | Number |  |
| pfPowerCurvePointBPowerFactor | Point B Power Factor | -0.99-0.8,0.81 |  | No | Number |  |
| pfPowerCurvePointCPower | Point C Power | 0~100 | % | No | Number |  |
| pfPowerCurvePointCPowerFactor | Point C Power Factor | -0.99-0.8,0.81 |  | No | Number |  |
| pfPowerCurveLockoutPower | Lockout Power | 0~100 | % | No | Number |  |
| puCurveFunctionEnable | P(U) Curve Function | 0:Disable  1:Enable |  | No | Number |  |
| puCurvePointAActivePower | Point A  Active Power | -100~100 | % | No | Number |  |
| puCurvePointBActivePower | Point B  Active Power | -100~100 | % | No | Number |  |
| puCurvePointCActivePower | Point C  Active Power | -100~100 | % | No | Number |  |
| puCurvePointDActivePower | Point D  Active Power | -100~100 | % | No | Number |  |
| quCurveFunctionEnable | Q(U) Curve Function | 0:Disable  1:Enable |  | No | Number |  |
| quCurvePointAReactivePower | Point A  Reactive Power | -100~100 | % | No | Number |  |
| quCurvePointBReactivePower | Point B  Reactive Power | -100~100 | % | No | Number |  |
| quCurvePointCReactivePower | Point C  Reactive Power | -100~100 | % | No | Number |  |
| quCurvePointDReactivePower | Point D  Reactive Power | -100~100 | % | No | Number |  |
| quCurveLockInPower | Lock In Power | -100~100 | % | No | Number |  |
| quCurveLockOutPower | Lock Out Power | -100~100 | % | No | Number |  |
| fpCurveFunctionEnable | FP Curve Function | 0:Disable  1:Enable |  | No | Number |  |
| fpCurveOverFrequencyLowerLimit | Over Frequency Start Point | 30~80 | Hz | No | Number |  |
| fpUnderFrequencyLowerLimit | Under Frequency Start Point | 30~80 | Hz | No | Number |  |
| fpOverFrequencyUpperLimit | Over Frequency End Point | 30~80 | Hz | No | Number |  |
| fpUnderFrequencyUpperLimit | Under Frequency End Point | 30~80 | Hz | No | Number |  |
| fpRestoreFrequencyUperLimit | F(Stop) Upper | 30~80 | Hz | No | Number |  |
| fpRestoreFrequencyLowerLimit | F(Stop) Lower | 30~80 | Hz | No | Number |  |
| fpRestoreFrequencyWaitingTime | Restore Waiting Time | 1~65535 | Sec | No | Number |  |
| fpRestoreFrequencyPowerSlope | Reconnection Power Slope | 1~65535 | Sec | No | Number |  |
| fpOverFrequencyPowerSlope | Over Frequency Power Slope | 0~100 | % | No | Number |  |
| fpUnderFrequencyPowerSlope | Under Frequency Power Slope | 0~100 | % | No | Number |  |
| fpRecoveryPowerSlope | Recovery Power Slope | 0~100 | % | No | Number |  |
| fpChargeCurveFunctionEnable | FP Charge Curve Function | 0:Disable  1:Enable |  | No | Number |  |
| fpUnderFrequencyPowerSlopeForCharge | Under Frequency Power Slope For Charge | 0~100 | % | No | Number |  |
| lowVoltageRideThroughFunctionEnable | Low Voltage Ride Through | 0:Disable  1:Enable |  | No | Number |  |
| lowVoltageStartPointTripTime | Start Point Of Protection Time | 0.02~1000 | Sec | No | Number |  |
| lowVoltageEndPointTripTime | End Point Of Protection Time | 0.02~1000 | Sec | No | Number |  |
| highVoltageRideThroughFunctionEnable | High Voltage Ride Through Function | 0:Disable  1:Enable |  | No | Number |  |
| highVoltageStartPointTripTime | Start Point Of Protection Time | 0.02~1000 | Sec | No | Number |  |
| highVoltageEndPointTripTime | End Point Of Protection Time | 0.02~1000 | Sec | No | Number |  |
| overVoltageStage1TripValue | OV Stage1 Trip Value | 230~300 | V | No | Number |  |
| underVoltageStage1TripValue | UV Stage1 Trip Value | 0.1~300 | V | No | Number |  |
| overVoltageStage2TripValue | OV Stage2 Trip Value | 230~300 | V | No | Number |  |
| underVoltageStage2TripValue | UV Stage2 Trip Value | 0.1~300 | V | No | Number |  |
| overFrequencyStage1TripValue | OF Stage1 Trip Value | 30~80 | Hz | No | Number |  |
| underFrequencyStage1TripValue | UF Stage1 Trip Value | 30~80 | Hz | No | Number |  |
| overFrequencyStage2TripValue | OF Stage2 Trip Value | 30~80 | Hz | No | Number |  |
| underFrequencyStage2TripValue | UF Stage2 Trip Value | 30~80 | Hz | No | Number |  |
| pfPowerCurveLockinVoltage | Lockin Voltage | 60~300 | V | No | Number |  |
| pfPowerCurveLockoutVoltage | Lockout Voltage | 60~300 | V | No | Number |  |
| puCurvePointAVoltage | Point A Voltage | 60~300 | V | No | Number |  |
| puCurvePointBVoltage | Point B  Voltage | 60~300 | V | No | Number |  |
| puCurvePointCVoltage | Point C  Voltage | 60~300 | V | No | Number |  |
| puCurvePointDVoltage | Point D  Voltage | 60~300 | V | No | Number |  |
| quCurvePointAVoltage | Point A Voltage | 60~300 | V | No | Number |  |
| quCurvePointBVoltage | Point B  Voltage | 60~300 | V | No | Number |  |
| quCurvePointCVoltage | Point C  Voltage | 60~300 | V | No | Number |  |
| quCurvePointDVoltage | Point D  Voltage | 60~300 | V | No | Number |  |
| lowVoltageStartPointTripValue | Start Point Of Ride Through | 0~230 | V | No | Number |  |
| lowVoltageEndPointTripValue | End Point Of Ride Through | 0~230 | V | No | Number |  |
| lowVoltageCrossingTripThreshold | Low Voltage Limit Of Ride Through | 0~230 | V | No | Number |  |
| highVoltageStartPointTripValue | Start Point Of Ride Through | 230~300 | V | No | Number |  |
| highVoltageEndPointTripValue | End Point Of Ride Through | 230~300 | V | No | Number |  |
| highVoltageCrossingTripThreshold | High Voltage Limit Of Ride Through | 230~300 | V | No | Number |  |
| commOffLineEnable | CommOffLine | 0:Disable  1:Enable |  | No | Number |  |
| autoTestEnable | AutoTestEnable | 0:Disable  1:Enable |  | No | Number |  |
| deratingByVoltageEnable | DeratingByVoltage | 0:Disable  1:Enable |  | No | Number |  |

### IVGM10048

| Key | Name | Range | unit | Required | Type | Description |
| --- | ---- | ----- | ---- | -------- | ---- | ----------- |
| acOutputRatedVoltage | AC Output Rated Voltage | 220:220V  230:230V  240:240V | V | NO | Number |  |
| acOutputRatedFrequency | AC Output Rated Frequency | 0:50Hz  1:60Hz | Hz | NO | Number |  |
| gridPowerUnbalanceEnable | Grid Power Unbalance | 0:Disable  1:Enable |  | NO | Number |  |
| powerFactor | Power Factor | -0.99-0.8,0.81 |  | NO | Number |  |
| gridWaveformDetectionMode | Detection Mode | 0:Wave Detect  1:Half Wave Detect  2:Disable Wave Detect |  | NO | Number |  |
| batteryModel | Battery Model | 0:User defined  1:Third party(Lithium battery)  2:Felicity(LPBF/LUX-X series)  3:Felicity(LPBA/LUX-Y/LUX-E  series) |  | NO | Number |  |
| batteryOnGridDischargeDepthSoc | Battery Discharged Depth(On-Grid, Bms Connected) | 10~100 | % | NO | Number | The battery SOC is lower than the battery on-grid discharge depth, and the battery stops discharging |
| batteryOffGridDischargeDepthSoc | Battery Discharged Depth(Off-Grid, Bms Connected) | 0~100 | % | NO | Number | The battery SOC is lower than the battery off-grid discharge depth, and the battery stops discharging |
| batteryOffGridRecoveryDepthSoc | Battery Restart Depth(Off-Grid, Bms Connected) | 0~100 | % | NO | Number | When the battery SOC is lower than the setting value of "Battery discharge depth (off grid)", the inverter can only be output off the grid again after the SOC recovers to the setting value higher than "Battery restart depth |
| lcdBacklightEnable | LCD Backlight | 0:Disable  1:Enable |  | NO | Number |  |
| buzzerEnable | Buzzer | 0:Disable  1:Enable |  | NO | Number |  |
| overLoadProtectionResetEnable | Over Load Protection Reset | 0:Disable  1:Enable |  | NO | Number | The fault will be cleared automatically after the overload protection of the machine. If the overload protection occurs 3 times within half an hour, the overload fault will not be cleared |
| remoteOnOffEnable | Remote control | 0:ON  1:OFF |  | NO | Number | The machine shuts down and enters standby mode |
| remoteOutputOnOffControl | AC Output ON/OFF | 0:ON  1:OFF |  | NO | Number |  |
| zeroExportFunction | Zero Export Mode | 1:To load  2:To CT |  | NO | Number | "The feed power is limited according to the setting of ""grid connection power limit"".1) To load:The inverter can supply power to the backup load and sell power to the grid but the selling power will not exceed the setting value of ""grid connection power limit""2) To CT:The inverter can supply power to the backup load, household load and sell power to the grid, but the selling power will not exceed the setting value of ""grid connection power limit"".In this mode, a CT is needed." |
| zeroExportAdjustmentPower | Zero Export Power | -500~500 | W | NO | Number | When the grid-connected power is set to 0, it is used to calibrate the sampling deviation to ensure that the inverter will not feed power to the grid |
| clearEnergyStorageLog | Clear Energy Storage Log | 1:Clear |  | NO | Number |  |
| clearEventLog | Clear Event Log | 1:Clear |  | NO | Number |  |
| factoryReset | Factory Reset | 1:Reset |  | NO | Number |  |
| eventLogFunctionEnable | Event Log Function | 0:Disable  1:Charge  2:Discharge |  | NO | Number |  |
| faultLogFunctionEnable | Fault Log Function | 0:Disable  1:Charge  2:Discharge |  | NO | Number |  |
| gfciLevel1ProtectionEnable | GFCI One-level Protection | 0:Disable  1:Charge  2:Discharge |  | NO | Number |  |
| gfciLevel2ProtectionEnable | GFCI Two-level Protection | 0:Disable  1:Charge  2:Discharge |  | NO | Number |  |
| gfciLevel3ProtectionEnable | GFCI Three-level Protection | 0:Disable  1:Charge  2:Discharge |  | NO | Number |  |
| isoDetectionEnable | ISO Detection | 0:Disable  1:Charge  2:Discharge |  | NO | Number |  |
| antiIslandingDetectionEnable | Anti-Islanding Detection | 0:Disable  1:Charge  2:Discharge |  | NO | Number |  |
| pvParallelSetting | PV Parallel Set | 0:Stand Alone  1:Parallel |  | NO | Number |  |
| fixQPencent | FixQ Pencent | -60~60 | % | NO | Number |  |
| bmsHeartbeat | BMS Heartbeat | 0:Disable  1:Charge  2:Discharge |  | NO | Number | After enabling, if the battery type is lithium battery and BMS communication fails, it will report BMS communication failure |
| operatedMode | Operated Mode | 0:General Mode  1:Backup Mode  2:Eco Mode  3:Gen Mode |  | NO | Number | "Set inverter operation mode:1) General mode:In this mode, the load is mainly powered by PV and battery.2) Backup mode:In this mode, PV gives priority to charging the battery to ensure that the battery is always full.3) ECO mode:In this mode, you can set a specific time to take power from the grid to charge the battery or use the power of the grid to charge the battery, and operate in general mode outside the set time.4) Generator mode:In this mode, the load is mainly powered by PV and battery." |
| ecoRule1.ruleMode | ECO Mode 1 | 0:Disable  1:Charge  2:Discharge   3:AC Couple |  | NO | Number | "Economic model rules:1) Disable: No charging and discharging2) Charge: Charge the battery from the grid3) Discharge: Selling power from battery to the grid4)AC Couple:Spontaneous self-use, waste electricity Internet access" |
| ecoRule1.startTime | Start Time1 | HH:023 mm:059 |  | NO | String | Starting time, Format: HH:mm |
| ecoRule1.stopTime | Stop Time1 | HH:023 mm:059 |  | NO | String | Stop time, Format: HH:mm |
| ecoRule1.startDay | Start Day1 | MM:112 dd:131 |  | NO | String | Starting day, Format: MM:dd |
| ecoRule1.stopDay | Stop Day1 | MM:112 dd:131 |  | NO | String | Stop day, Format: MM:dd |
| ecoRule1.daysOfEffectiveWeek | Effective Week1 | MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY |  | NO | Array | Week Of Use: Time Of Use Effective Week,Valuable：MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY，Multiple Choice |
| ecoRule1.soc | SOC1 | 0~100 | % | NO | Number |  |
| ecoRule1.voltage | Voltage1 | 48~60 | V | NO | Number | "1) Charging: Stop charging voltage. Battery voltage above this value stops charging (usually set to 57.6v for a single battery).2) Discharge: Stop discharge voltage. If the battery voltage is lower than this value, it will stop discharging." |
| ecoRule1.power | Power1 | "Slave Version <106 : 010000Slave Version ≥106 : -1000010000" | W | NO | Number | "1) Charging: Battery charging power2) Discharge: Battery discharge power3)Dispatched power: Grid power supply or intake power" |
| ecoRule2.ruleMode | ECO Mode 2 | 0:Disable  1:Charge  2:Discharge   3:AC Couple |  | NO | Number | "Economic model rules:1) Disable: No charging and discharging2) Charge: Charge the battery from the grid3) Discharge: Selling power from battery to the grid |
| 4)AC Couple:Spontaneous self-use, waste electricity Internet access" |  |  |  |  |  |  |
| ecoRule2.startTime | Start Time2 | HH:023 mm:059 |  | NO | String | Starting time, Format: HH:mm |
| ecoRule2.stopTime | Stop Time2 | HH:023 mm:059 |  | NO | String | Stop time, Format: HH:mm |
| ecoRule2.startDay | Start Day2 | MM:112 dd:131 |  | NO | String | Starting day, Format: MM:dd |
| ecoRule2.stopDay | Stop Day2 | MM:112 dd:131 |  | NO | String | Stop day, Format: MM:dd |
| ecoRule2.voltage | Voltage2 | 48~60 | V | NO | Number | "1) Charging: Stop charging voltage. Battery voltage above this value stops charging (usually set to 57.6v for a single battery).2) Discharge: Stop discharge voltage. If the battery voltage is lower than this value, it will stop discharging." |
| ecoRule2.power | Power2 | "Slave Version <106 : 010000Slave Version ≥106 : -1000010000" | W | NO | Number | "1) Charging: Battery charging power2) Discharge: Battery discharge power3)Dispatched power: Grid power supply or intake power" |
| ecoRule2.daysOfEffectiveWeek | Effective Week2 | MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY |  | NO | Array | Week Of Use: Time Of Use Effective Week,Valuable：MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY，Multiple Choice |
| ecoRule2.soc | SOC2 | 0~100 | % | NO | Number |  |
| ecoRule3.ruleMode | ECO Mode 3 | 0:Disable  1:Charge  2:Discharge   3:AC Couple |  | NO | Number | "Economic model rules:1) Disable: No charging and discharging2) Charge: Charge the battery from the grid3) Discharge: Selling power from battery to the grid4)AC Couple:Spontaneous self-use, waste electricity Internet access" |
| ecoRule3.startTime | Start Time3 | HH:023 mm:059 |  | NO | String | Starting time, Format: HH:mm |
| ecoRule3.stopTime | Stop Time3 | HH:023 mm:059 |  | NO | String | Stop time, Format: HH:mm |
| ecoRule3.startDay | Start Day3 | MM:112 dd:131 |  | NO | String | Starting day, Format: MM:dd |
| ecoRule3.stopDay | Stop Day3 | MM:112 dd:131 |  | NO | String | Stop day, Format: MM:dd |
| ecoRule3.daysOfEffectiveWeek | Effective Week3 | MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY |  | NO | Array | Week Of Use: Time Of Use Effective Week,Valuable：MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY，Multiple Choice |
| ecoRule3.soc | SOC3 | 0~100 | % | NO | Number |  |
| ecoRule3.voltage | Voltage3 | 48~60 | V | NO | Number | "1) Charging: Stop charging voltage. Battery voltage above this value stops charging (usually set to 57.6v for a single battery).2) Discharge: Stop discharge voltage. If the battery voltage is lower than this value, it will stop discharging." |
| ecoRule3.power | Power3 | "Slave Version <106 : 010000Slave Version ≥106 : -1000010000" | W | NO | Number | "1) Charging: Battery charging power2) Discharge: Battery discharge power3)Dispatched power: Grid power supply or intake power" |
| ecoRule4.ruleMode | ECO Mode 4 | 0:Disable  1:Charge  2:Discharge   3:AC Couple |  | NO | Number | "Economic model rules:1) Disable: No charging and discharging2) Charge: Charge the battery from the grid3) Discharge: Selling power from battery to the grid4)AC Couple:Spontaneous self-use, waste electricity Internet access" |
| ecoRule4.startTime | Start Time4 | HH:023 mm:059 |  | NO | String | Starting time, Format: HH:mm |
| ecoRule4.stopTime | Stop Time4 | HH:023 mm:059 |  | NO | String | Stop time, Format: HH:mm |
| ecoRule4.startDay | Start Day4 | MM:112 dd:131 |  | NO | String | Starting day, Format: MM:dd |
| ecoRule4.stopDay | Stop Day4 | MM:112 dd:131 |  | NO | String | Stop day, Format: MM:dd |
| ecoRule4.voltage | Voltage4 | 48~60 | V | NO | Number | "1) Charging: Stop charging voltage. Battery voltage above this value stops charging (usually set to 57.6v for a single battery).2) Discharge: Stop discharge voltage. If the battery voltage is lower than this value, it will stop discharging." |
| ecoRule4.power | Power4 | "Slave Version <106 : 010000Slave Version ≥106 : -1000010000" | W | NO | Number | "1) Charging: Battery charging power2) Discharge: Battery discharge power3)Dispatched power: Grid power supply or intake power" |
| ecoRule4.daysOfEffectiveWeek | Effective Week4 | MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY |  | NO | Array | Week Of Use: Time Of Use Effective Week,Valuable：MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY，Multiple Choice |
| ecoRule4.soc | SOC4 | 0~100 | % | NO | Number |  |
| additionalEcoEnable | ECO 10 enable | 0:Disable  1:Enable |  | NO | Number | Only when Master Version ≥ 2204，parameter can be used, ecoRule5 ~ecoRule10 also.After enabling, there will be 10 economic rules that can be set.Only trial on some devices. If there is no value displayed or it cannot run, please use the old 4-segment mode. |
| ecoRule5.ruleMode | ECO Mode 5 | 0:Disable  1:Charge  2:Discharge |  | NO | Number | "Economic model rules:1) Disable: No charging and discharging2) Charge: Charge the battery from the grid3) Discharge: Selling power from battery to the grid4)AC Couple:Spontaneous self-use, waste electricity Internet access" |
| ecoRule5.startTime | Start Time5 | HH:023 mm:059 |  | NO | String | Starting time, Format: HH:mm |
| ecoRule5.stopTime | Stop Time5 | HH:023 mm:059 |  | NO | String | Stop time, Format: HH:mm |
| ecoRule5.startDay | Start Day5 | MM:112 dd:131 |  | NO | String | Starting day, Format: MM:dd |
| ecoRule5.stopDay | Stop Day5 | MM:112 dd:131 |  | NO | String | Stop day, Format: MM:dd |
| ecoRule5.voltage | Voltage5 | 48~60 | V | NO | Number |  |
| ecoRule5.power | Power5 | 0~10000 | W | NO | Number |  |
| ecoRule5.daysOfEffectiveWeek | Effective Week5 | MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY |  | NO | Array | Week Of Use: Time Of Use Effective Week,Valuable：MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY，Multiple Choice |
| ecoRule5.soc | SOC5 | 0~100 | % | NO | Number |  |
| ecoRule6.ruleMode | ECO Mode 6 | 0:Disable  1:Charge  2:Discharge |  | NO | Number | "Economic model rules:1) Disable: No charging and discharging2) Charge: Charge the battery from the grid3) Discharge: Selling power from battery to the grid |
| 4)AC Couple:Spontaneous self-use, waste electricity Internet access" |  |  |  |  |  |  |
| ecoRule6.startTime | Start Time6 | HH:023 mm:059 |  | NO | String | Starting time, Format: HH:mm |
| ecoRule6.stopTime | Stop Time6 | HH:023 mm:059 |  | NO | String | Stop time, Format: HH:mm |
| ecoRule6.startDay | Start Day6 | MM:112 dd:131 |  | NO | String | Starting day, Format: MM:dd |
| ecoRule6.stopDay | Stop Day6 | MM:112 dd:131 |  | NO | String | Stop day, Format: MM:dd |
| ecoRule6.voltage | Voltage6 | 48~60 | V | NO | Number |  |
| ecoRule6.power | Power6 | 0~10000 | W | NO | Number |  |
| ecoRule6.daysOfEffectiveWeek | Effective Week6 | MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY |  | NO | Array | Week Of Use: Time Of Use Effective Week,Valuable：MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY，Multiple Choice |
| ecoRule6.soc | SOC6 | 0~100 | % | NO | Number |  |
| ecoRule7.ruleMode | ECO Mode 7 | 0:Disable  1:Charge  2:Discharge |  | NO | Number | "Economic model rules:1) Disable: No charging and discharging2) Charge: Charge the battery from the grid3) Discharge: Selling power from battery to the grid4)AC Couple:Spontaneous self-use, waste electricity Internet access" |
| ecoRule7.startTime | Start Time7 | HH:023 mm:059 |  | NO | String | Starting time, Format: HH:mm |
| ecoRule7.stopTime | Stop Time7 | HH:023 mm:059 |  | NO | String | Stop time, Format: HH:mm |
| ecoRule7.startDay | Start Day7 | MM:112 dd:131 |  | NO | String | Starting day, Format: MM:dd |
| ecoRule7.stopDay | Stop Day7 | MM:112 dd:131 |  | NO | String | Stop day, Format: MM:dd |
| ecoRule7.voltage | Voltage7 | 48~60 | V | NO | Number |  |
| ecoRule7.power | Power7 | 0~10000 | W | NO | Number |  |
| ecoRule7.daysOfEffectiveWeek | Effective Week7 | MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY |  | NO | Array | Week Of Use: Time Of Use Effective Week,Valuable：MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY，Multiple Choice |
| ecoRule7.soc | SOC7 | 0~100 | % | NO | Number |  |
| ecoRule8.ruleMode | ECO Mode 8 | 0:Disable  1:Charge  2:Discharge |  | NO | Number | "Economic model rules:1) Disable: No charging and discharging2) Charge: Charge the battery from the grid3) Discharge: Selling power from battery to the grid |
| 4)AC Couple:Spontaneous self-use, waste electricity Internet access" |  |  |  |  |  |  |
| ecoRule8.startTime | Start Time8 | HH:023 mm:059 |  | NO | String | Starting time, Format: HH:mm |
| ecoRule8.stopTime | Stop Time8 | HH:023 mm:059 |  | NO | String | Stop time, Format: HH:mm |
| ecoRule8.startDay | Start Day8 | MM:112 dd:131 |  | NO | String | Starting day, Format: MM:dd |
| ecoRule8.stopDay | Stop Day8 | MM:112 dd:131 |  | NO | String | Stop day, Format: MM:dd |
| ecoRule8.voltage | Voltage8 | 48~60 | V | NO | Number |  |
| ecoRule8.power | Power8 | 0~10000 | W | NO | Number |  |
| ecoRule8.daysOfEffectiveWeek | Effective Week8 | MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY |  | NO | Array | Week Of Use: Time Of Use Effective Week,Valuable：MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY，Multiple Choice |
| ecoRule8.soc | SOC8 | 0~100 | % | NO | Number |  |
| ecoRule9.ruleMode | ECO Mode 9 | 0:Disable  1:Charge  2:Discharge |  | NO | Number | "Economic model rules:1) Disable: No charging and discharging2) Charge: Charge the battery from the grid3) Discharge: Selling power from battery to the grid4)AC Couple:Spontaneous self-use, waste electricity Internet access" |
| ecoRule9.startTime | Start Time9 | HH:023 mm:059 |  | NO | String | Starting time, Format: HH:mm |
| ecoRule9.stopTime | Stop Time9 | HH:023 mm:059 |  | NO | String | Stop time, Format: HH:mm |
| ecoRule9.startDay | Start Day9 | MM:112 dd:131 |  | NO | String | Starting day, Format: MM:dd |
| ecoRule9.stopDay | Stop Day9 | MM:112 dd:131 |  | NO | String | Stop day, Format: MM:dd |
| ecoRule9.voltage | Voltage9 | 48~60 | V | NO | Number |  |
| ecoRule9.power | Power9 | 0~10000 | W | NO | Number |  |
| ecoRule9.daysOfEffectiveWeek | Effective Week9 | MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY |  | NO | Array | Week Of Use: Time Of Use Effective Week,Valuable：MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY，Multiple Choice |
| ecoRule9.soc | SOC9 | 0~100 | % | NO | Number |  |
| ecoRule10.ruleMode | ECO Mode 10 | 0:Disable  1:Charge  2:Discharge |  | NO | Number | "Economic model rules:1) Disable: No charging and discharging2) Charge: Charge the battery from the grid3) Discharge: Selling power from battery to the grid4)AC Couple:Spontaneous self-use, waste electricity Internet access" |
| ecoRule10.startTime | Start Time10 | HH:023 mm:059 |  | NO | String | Starting time, Format: HH:mm |
| ecoRule10.stopTime | Stop Time10 | HH:023 mm:059 |  | NO | String | Stop time, Format: HH:mm |
| ecoRule10.startDay | Start Day10 | MM:112 dd:131 |  | NO | String | Starting day, Format: MM:dd |
| ecoRule10.stopDay | Stop Day10 | MM:112 dd:131 |  | NO | String | Stop day, Format: MM:dd |
| ecoRule10.voltage | Voltage10 | 48~60 | V | NO | Number |  |
| ecoRule10.power | Power10 | 0~10000 | W | NO | Number |  |
| ecoRule10.daysOfEffectiveWeek | Effective Week10 | MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY |  | NO | Array | Week Of Use: Time Of Use Effective Week,Valuable：MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY，Multiple Choice |
| ecoRule10.soc | SOC10 | 0~100 | % | NO | Number |  |
| batteryModules | Battery Modules | 1~1 |  | NO | Number |  |
| batteryChargedVoltage | Battery Charged Voltage | 48~60 | V | NO | Number |  |
| batteryFloatingChargedVoltage | Bat float voltage | 48~60 | V | NO | Number |  |
| noBmsOnGridBatteryCutOffVoltage | Battery Cut-Off Voltage(On-Grid, No Bms) | 40~60 | V | NO | Number |  |
| noBmsOffGridBatteryCutOffVoltage | Battery Cut-Off Voltage(Off-Grid, No Bms) | 40~60 | V | NO | Number |  |
| noBmsOffGridBatteryRestartVoltage | Battery Restart Voltage(Off-Grid, No Bms) | 40~60 | V | NO | Number |  |
| batteryMaxChargedCurrent | Battery Max. Charged Current | 1~200 | A | NO | Number |  |
| batteryMaxDischargeCurrent | Battery Max. Discharged Current | 5~200 | A | NO | Number |  |
| --- | --- | --- | --- | --- | --- | --- |
| gridStandardCode | Standard | 0:Germany  1:Warehouse  2:50Hz grid default  3:60Hz grid default  4:Italy  5:Britain  6:Australia  7:New Zealand  8:South African  9:Netherland  10:Brazil  11:Europe  12:Poland  13:Czech |  | No | Number | Set the on-grid regulations in the current region |
| overVoltageStage1TripTime | OV Stage1 Trip Time | 0.02~1000 | Sec | No | Number |  |
| underVoltageStage1TripTime | UV Stage1 Trip Time | 0.02~1000 | Sec | No | Number |  |
| overVoltageStage2TripTime | OV Stage2 Trip Time | 0.02~1000 | Sec | No | Number |  |
| underVoltageStage2TripTime | UV Stage2 Trip Time | 0.02~1000 | Sec | No | Number |  |
| overVoltage10mTriggerValue | OV 10Min Mean Value | 230~300 | V | No | Number |  |
| overFrequencyStage1TripTime | OF Stage1 Trip Time | 0.02~1000 | Sec | No | Number |  |
| underFrequencyStage1TripTime | UF Stage1 Trip Time | 0.02~1000 | Sec | No | Number |  |
| overFrequencyStage2TripTime | OF Stage2 Trip Time | 0.02~1000 | Sec | No | Number |  |
| underFrequencyStage2TripTime | UF Stage2 Trip Time | 0.02~1000 | Sec | No | Number |  |
| onGridObservationTime | Observation Time | 1~3000 | Sec | No | Number |  |
| onGridPowerSlope | Grid Power Slope | 0~65535 | Sec | No | Number |  |
| onGridPowerLimit | Grid Power Limit | 0~100 | % | No | Number |  |
| pfPowerCurveFunctionEnable | PF-Power Curve Function | 0:Disable  1:Enable |  | No | Number |  |
| pfPowerCurvePointAPower | Point A Power | 0~100 | % | No | Number |  |
| pfPowerCurvePointAPowerFactor | Point A Power Factor | -0.99-0.8,0.81 |  | No | Number |  |
| pfPowerCurvePointBPower | Point B Power | 0~100 | % | No | Number |  |
| pfPowerCurvePointBPowerFactor | Point B Power Factor | -0.99-0.8,0.81 |  | No | Number |  |
| pfPowerCurvePointCPower | Point C Power | 0~100 | % | No | Number |  |
| pfPowerCurvePointCPowerFactor | Point C Power Factor | -0.99-0.8,0.81 |  | No | Number |  |
| pfPowerCurveLockoutPower | Lockout Power | 0~100 | % | No | Number |  |
| puCurveFunctionEnable | P(U) Curve Function | 0:Disable  1:Enable |  | No | Number |  |
| puCurvePointAActivePower | Point A  Active Power | -100~100 | % | No | Number |  |
| puCurvePointBActivePower | Point B  Active Power | -100~100 | % | No | Number |  |
| puCurvePointCActivePower | Point C  Active Power | -100~100 | % | No | Number |  |
| puCurvePointDActivePower | Point D  Active Power | -100~100 | % | No | Number |  |
| quCurveFunctionEnable | Q(U) Curve Function | 0:Disable  1:Enable |  | No | Number |  |
| quCurvePointAReactivePower | Point A  Reactive Power | -100~100 | % | No | Number |  |
| quCurvePointBReactivePower | Point B  Reactive Power | -100~100 | % | No | Number |  |
| quCurvePointCReactivePower | Point C  Reactive Power | -100~100 | % | No | Number |  |
| quCurvePointDReactivePower | Point D  Reactive Power | -100~100 | % | No | Number |  |
| quCurveLockInPower | Lock In Power | -100~100 | % | No | Number |  |
| quCurveLockOutPower | Lock Out Power | -100~100 | % | No | Number |  |
| fpCurveFunctionEnable | FP Curve Function | 0:Disable  1:Enable |  | No | Number |  |
| fpCurveOverFrequencyLowerLimit | Over Frequency Start Point | 30~80 | Hz | No | Number |  |
| fpUnderFrequencyLowerLimit | Under Frequency Start Point | 30~80 | Hz | No | Number |  |
| fpOverFrequencyUpperLimit | Over Frequency End Point | 30~80 | Hz | No | Number |  |
| fpUnderFrequencyUpperLimit | Under Frequency End Point | 30~80 | Hz | No | Number |  |
| fpRestoreFrequencyUperLimit | F(Stop) Upper | 30~80 | Hz | No | Number |  |
| fpRestoreFrequencyLowerLimit | F(Stop) Lower | 30~80 | Hz | No | Number |  |
| fpRestoreFrequencyWaitingTime | Restore Waiting Time | 1~65535 | Sec | No | Number |  |
| fpRestoreFrequencyPowerSlope | Reconnection Power Slope | 1~65535 | Sec | No | Number |  |
| fpOverFrequencyPowerSlope | Over Frequency Power Slope | 0~100 | % | No | Number |  |
| fpUnderFrequencyPowerSlope | Under Frequency Power Slope | 0~100 | % | No | Number |  |
| fpRecoveryPowerSlope | Recovery Power Slope | 0~100 | % | No | Number |  |
| fpChargeCurveFunctionEnable | FP Charge Curve Function | 0:Disable  1:Enable |  | No | Number |  |
| fpUnderFrequencyPowerSlopeForCharge | Under Frequency Power Slope For Charge | 0~100 | % | No | Number |  |
| lowVoltageRideThroughFunctionEnable | Low Voltage Ride Through | 0:Disable  1:Enable |  | No | Number |  |
| lowVoltageStartPointTripTime | Start Point Of Protection Time | 0.02~1000 | Sec | No | Number |  |
| lowVoltageEndPointTripTime | End Point Of Protection Time | 0.02~1000 | Sec | No | Number |  |
| highVoltageRideThroughFunctionEnable | High Voltage Ride Through Function | 0:Disable  1:Enable |  | No | Number |  |
| highVoltageStartPointTripTime | Start Point Of Protection Time | 0.02~1000 | Sec | No | Number |  |
| highVoltageEndPointTripTime | End Point Of Protection Time | 0.02~1000 | Sec | No | Number |  |
| overVoltageStage1TripValue | OV Stage1 Trip Value | 230~300 | V | No | Number |  |
| underVoltageStage1TripValue | UV Stage1 Trip Value | 0.1~300 | V | No | Number |  |
| overVoltageStage2TripValue | OV Stage2 Trip Value | 230~300 | V | No | Number |  |
| underVoltageStage2TripValue | UV Stage2 Trip Value | 0.1~300 | V | No | Number |  |
| overFrequencyStage1TripValue | OF Stage1 Trip Value | 30~80 | Hz | No | Number |  |
| underFrequencyStage1TripValue | UF Stage1 Trip Value | 30~80 | Hz | No | Number |  |
| overFrequencyStage2TripValue | OF Stage2 Trip Value | 30~80 | Hz | No | Number |  |
| underFrequencyStage2TripValue | UF Stage2 Trip Value | 30~80 | Hz | No | Number |  |
| pfPowerCurveLockinVoltage | Lockin Voltage | 60~300 | V | No | Number |  |
| pfPowerCurveLockoutVoltage | Lockout Voltage | 60~300 | V | No | Number |  |
| puCurvePointAVoltage | Point A Voltage | 60~300 | V | No | Number |  |
| puCurvePointBVoltage | Point B  Voltage | 60~300 | V | No | Number |  |
| puCurvePointCVoltage | Point C  Voltage | 60~300 | V | No | Number |  |
| puCurvePointDVoltage | Point D  Voltage | 60~300 | V | No | Number |  |
| quCurvePointAVoltage | Point A Voltage | 60~300 | V | No | Number |  |
| quCurvePointBVoltage | Point B  Voltage | 60~300 | V | No | Number |  |
| quCurvePointCVoltage | Point C  Voltage | 60~300 | V | No | Number |  |
| quCurvePointDVoltage | Point D  Voltage | 60~300 | V | No | Number |  |
| lowVoltageStartPointTripValue | Start Point Of Ride Through | 0~230 | V | No | Number |  |
| lowVoltageEndPointTripValue | End Point Of Ride Through | 0~230 | V | No | Number |  |
| lowVoltageCrossingTripThreshold | Low Voltage Limit Of Ride Through | 0~230 | V | No | Number |  |
| highVoltageStartPointTripValue | Start Point Of Ride Through | 230~300 | V | No | Number |  |
| highVoltageEndPointTripValue | End Point Of Ride Through | 230~300 | V | No | Number |  |
| highVoltageCrossingTripThreshold | High Voltage Limit Of Ride Through | 230~300 | V | No | Number |  |
| commOffLineEnable | CommOffLine | 0:Disable  1:Enable |  | No | Number |  |
| autoTestEnable | AutoTestEnable | 0:Disable  1:Enable |  | No | Number |  |
| deratingByVoltageEnable | DeratingByVoltage | 0:Disable  1:Enable |  | No | Number |  |

### IVGM6048

| Key | Name | Range | unit | Required | Type | Description |
| --- | ---- | ----- | ---- | -------- | ---- | ----------- |
| acOutputRatedVoltage | AC Output Rated Voltage | 220:220V  230:230V  240:240V | V | NO | Number |  |
| acOutputRatedFrequency | AC Output Rated Frequency | 0:50Hz  1:60Hz | Hz | NO | Number |  |
| gridPowerUnbalanceEnable | Grid Power Unbalance | 0:Disable  1:Enable |  | NO | Number |  |
| powerFactor | Power Factor | -0.99-0.8,0.81 |  | NO | Number |  |
| gridWaveformDetectionMode | Detection Mode | 0:Wave Detect  1:Half Wave Detect  2:Disable Wave Detect |  | NO | Number |  |
| batteryModel | Battery Model | 0:User defined  1:Third party(Lithium battery)  2:Felicity(LPBF/LUX-X series)  3:Felicity(LPBA/LUX-Y/LUX-E  series) |  | NO | Number |  |
| batteryOnGridDischargeDepthSoc | Battery Discharged Depth(On-Grid, Bms Connected) | 10~100 | % | NO | Number | The battery SOC is lower than the battery on-grid discharge depth, and the battery stops discharging |
| batteryOffGridDischargeDepthSoc | Battery Discharged Depth(Off-Grid, Bms Connected) | 0~100 | % | NO | Number | The battery SOC is lower than the battery off-grid discharge depth, and the battery stops discharging |
| batteryOffGridRecoveryDepthSoc | Battery Restart Depth(Off-Grid, Bms Connected) | 0~100 | % | NO | Number | When the battery SOC is lower than the setting value of "Battery discharge depth (off grid)", the inverter can only be output off the grid again after the SOC recovers to the setting value higher than "Battery restart depth |
| lcdBacklightEnable | LCD Backlight | 0:Disable  1:Enable |  | NO | Number |  |
| buzzerEnable | Buzzer | 0:Disable  1:Enable |  | NO | Number |  |
| overLoadProtectionResetEnable | Over Load Protection Reset | 0:Disable  1:Enable |  | NO | Number | The fault will be cleared automatically after the overload protection of the machine. If the overload protection occurs 3 times within half an hour, the overload fault will not be cleared |
| remoteOnOffEnable | Remote control | 0:ON  1:OFF |  | NO | Number | The machine shuts down and enters standby mode |
| remoteOutputOnOffControl | AC Output ON/OFF | 0:ON  1:OFF |  | NO | Number |  |
| zeroExportFunction | Zero Export Mode | 1:To load  2:To CT |  | NO | Number | "The feed power is limited according to the setting of ""grid connection power limit"".  1) To load:  The inverter can supply power to the backup load and sell power to the grid but the selling power will not exceed the setting value of ""grid connection power limit""  2) To CT:  The inverter can supply power to the backup load, household load and sell power to the grid, but the selling power will not exceed the setting value of ""grid connection power limit"".In this mode, a CT is needed." |
| zeroExportAdjustmentPower | Zero Export Power | -500~500 | W | NO | Number | When the grid-connected power is set to 0, it is used to calibrate the sampling deviation to ensure that the inverter will not feed power to the grid |
| clearEnergyStorageLog | Clear Energy Storage Log | 1:Clear |  | NO | Number |  |
| clearEventLog | Clear Event Log | 1:Clear |  | NO | Number |  |
| factoryReset | Factory Reset | 1:Reset |  | NO | Number |  |
| eventLogFunctionEnable | Event Log Function | 0:Disable  1:Charge  2:Discharge |  | NO | Number |  |
| faultLogFunctionEnable | Fault Log Function | 0:Disable  1:Charge  2:Discharge |  | NO | Number |  |
| gfciLevel1ProtectionEnable | GFCI One-level Protection | 0:Disable  1:Charge  2:Discharge |  | NO | Number |  |
| gfciLevel2ProtectionEnable | GFCI Two-level Protection | 0:Disable  1:Charge  2:Discharge |  | NO | Number |  |
| gfciLevel3ProtectionEnable | GFCI Three-level Protection | 0:Disable  1:Charge  2:Discharge |  | NO | Number |  |
| isoDetectionEnable | ISO Detection | 0:Disable  1:Charge  2:Discharge |  | NO | Number |  |
| antiIslandingDetectionEnable | Anti-Islanding Detection | 0:Disable  1:Charge  2:Discharge |  | NO | Number |  |
| pvParallelSetting | PV Parallel Set | 0:Stand Alone  1:Parallel |  | NO | Number |  |
| fixQPencent | FixQ Pencent | -60~60 | % | NO | Number |  |
| bmsHeartbeat | BMS Heartbeat | 0:Disable  1:Charge  2:Discharge |  | NO | Number | After enabling, if the battery type is lithium battery and BMS communication fails, it will report BMS communication failure |
| operatedMode | Operated Mode | 0:General Mode  1:Backup Mode  2:Eco Mode  3:Gen Mode |  | NO | Number | "Set inverter operation mode:  1) General mode:  In this mode, the load is mainly powered by PV and battery.  2) Backup mode:  In this mode, PV gives priority to charging the battery to ensure that the battery is always full.  3) ECO mode:  In this mode, you can set a specific time to take power from the grid to charge the battery or use the power of the grid to charge the battery, and operate in general mode outside the set time.  4) Generator mode:  In this mode, the load is mainly powered by PV and battery." |
| ecoRule1.ruleMode | ECO Mode 1 | 0:Disable  1:Charge  2:Discharge   3:AC Couple |  | NO | Number | "Economic model rules:  1) Disable: No charging and discharging  2) Charge: Charge the battery from the grid  3) Discharge: Selling power from battery to the grid  4)AC Couple:Spontaneous self-use, waste electricity Internet access" |
| ecoRule1.startTime | Start Time1 | HH:023 mm:059 |  | NO | String | Starting time, Format: HH:mm |
| ecoRule1.stopTime | Stop Time1 | HH:023 mm:059 |  | NO | String | Stop time, Format: HH:mm |
| ecoRule1.startDay | Start Day1 | MM:112 dd:131 |  | NO | String | Starting day, Format: MM:dd |
| ecoRule1.stopDay | Stop Day1 | MM:112 dd:131 |  | NO | String | Stop day, Format: MM:dd |
| ecoRule1.daysOfEffectiveWeek | Effective Week1 | MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY |  | NO | Array | Week Of Use: Time Of Use Effective Week,Valuable：MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY，Multiple Choice |
| ecoRule1.soc | SOC1 | 0~100 | % | NO | Number |  |
| ecoRule1.voltage | Voltage1 | 48~60 | V | NO | Number | "1) Charging: Stop charging voltage. Battery voltage above this value stops charging (usually set to 57.6v for a single battery).  2) Discharge: Stop discharge voltage. If the battery voltage is lower than this value, it will stop discharging." |
| ecoRule1.power | Power1 | "Slave Version <203 : 06000  Slave Version ≥203 : -60006000" | W | NO | Number | "1) Charging: Battery charging power  2) Discharge: Battery discharge power  3)Dispatched power: Grid power supply or intake power" |
| ecoRule2.ruleMode | ECO Mode 2 | 0:Disable  1:Charge  2:Discharge   3:AC Couple |  | NO | Number | "Economic model rules:  1) Disable: No charging and discharging  2) Charge: Charge the battery from the grid  3) Discharge: Selling power from battery to the grid  4)AC Couple:Spontaneous self-use, waste electricity Internet access" |
| ecoRule2.startTime | Start Time2 | HH:023 mm:059 |  | NO | String | Starting time, Format: HH:mm |
| ecoRule2.stopTime | Stop Time2 | HH:023 mm:059 |  | NO | String | Stop time, Format: HH:mm |
| ecoRule2.startDay | Start Day2 | MM:112 dd:131 |  | NO | String | Starting day, Format: MM:dd |
| ecoRule2.stopDay | Stop Day2 | MM:112 dd:131 |  | NO | String | Stop day, Format: MM:dd |
| ecoRule2.voltage | Voltage2 | 48~60 | V | NO | Number | "1) Charging: Stop charging voltage. Battery voltage above this value stops charging (usually set to 57.6v for a single battery).  2) Discharge: Stop discharge voltage. If the battery voltage is lower than this value, it will stop discharging." |
| ecoRule2.power | Power2 | "Slave Version <203 : 06000  Slave Version ≥203 : -60006000" | W | NO | Number | "1) Charging: Battery charging power  2) Discharge: Battery discharge power  3)Dispatched power: Grid power supply or intake power" |
| ecoRule2.daysOfEffectiveWeek | Effective Week2 | MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY |  | NO | Array | Week Of Use: Time Of Use Effective Week,Valuable：MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY，Multiple Choice |
| ecoRule2.soc | SOC2 | 0~100 | % | NO | Number |  |
| ecoRule3.ruleMode | ECO Mode 3 | 0:Disable  1:Charge  2:Discharge   3:AC Couple |  | NO | Number | "Economic model rules:  1) Disable: No charging and discharging  2) Charge: Charge the battery from the grid  3) Discharge: Selling power from battery to the grid  4)AC Couple:Spontaneous self-use, waste electricity Internet access" |
| ecoRule3.startTime | Start Time3 | HH:023 mm:059 |  | NO | String | Starting time, Format: HH:mm |
| ecoRule3.stopTime | Stop Time3 | HH:023 mm:059 |  | NO | String | Stop time, Format: HH:mm |
| ecoRule3.startDay | Start Day3 | MM:112 dd:131 |  | NO | String | Starting day, Format: MM:dd |
| ecoRule3.stopDay | Stop Day3 | MM:112 dd:131 |  | NO | String | Stop day, Format: MM:dd |
| ecoRule3.daysOfEffectiveWeek | Effective Week3 | MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY |  | NO | Array | Week Of Use: Time Of Use Effective Week,Valuable：MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY，Multiple Choice |
| ecoRule3.soc | SOC3 | 0~100 | % | NO | Number |  |
| ecoRule3.voltage | Voltage3 | 48~60 | V | NO | Number | "1) Charging: Stop charging voltage. Battery voltage above this value stops charging (usually set to 57.6v for a single battery).  2) Discharge: Stop discharge voltage. If the battery voltage is lower than this value, it will stop discharging." |
| ecoRule3.power | Power3 | "Slave Version <203 : 06000  Slave Version ≥203 : -60006000" | W | NO | Number | "1) Charging: Battery charging power  2) Discharge: Battery discharge power  3)Dispatched power: Grid power supply or intake power" |
| ecoRule4.ruleMode | ECO Mode 4 | 0:Disable  1:Charge  2:Discharge   3:AC Couple |  | NO | Number | "Economic model rules:  1) Disable: No charging and discharging  2) Charge: Charge the battery from the grid  3) Discharge: Selling power from battery to the grid  4)AC Couple:Spontaneous self-use, waste electricity Internet access" |
| ecoRule4.startTime | Start Time4 | HH:023 mm:059 |  | NO | String | Starting time, Format: HH:mm |
| ecoRule4.stopTime | Stop Time4 | HH:023 mm:059 |  | NO | String | Stop time, Format: HH:mm |
| ecoRule4.startDay | Start Day4 | MM:112 dd:131 |  | NO | String | Starting day, Format: MM:dd |
| ecoRule4.stopDay | Stop Day4 | MM:112 dd:131 |  | NO | String | Stop day, Format: MM:dd |
| ecoRule4.voltage | Voltage4 | 48~60 | V | NO | Number | "1) Charging: Stop charging voltage. Battery voltage above this value stops charging (usually set to 57.6v for a single battery).  2) Discharge: Stop discharge voltage. If the battery voltage is lower than this value, it will stop discharging." |
| ecoRule4.power | Power4 | "Slave Version <203 : 06000  Slave Version ≥203 : -60006000" | W | NO | Number | "1) Charging: Battery charging power  2) Discharge: Battery discharge power  3)Dispatched power: Grid power supply or intake power" |
| ecoRule4.daysOfEffectiveWeek | Effective Week4 | MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY |  | NO | Array | Week Of Use: Time Of Use Effective Week,Valuable：MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY，Multiple Choice |
| ecoRule4.soc | SOC4 | 0~100 | % | NO | Number |  |
| additionalEcoEnable | ECO 10 enable | 0:Disable  1:Enable |  | NO | Number | Only when Master Version ≥ 2204，parameter can be used, ecoRule5 ~ecoRule10 also.After enabling, there will be 10 economic rules that can be set.Only trial on some devices. If there is no value displayed or it cannot run, please use the old 4-segment mode. |
| ecoRule5.ruleMode | ECO Mode 5 | 0:Disable  1:Charge  2:Discharge |  | NO | Number | "Economic model rules:  1) Disable: No charging and discharging  2) Charge: Charge the battery from the grid  3) Discharge: Selling power from battery to the grid  4)AC Couple:Spontaneous self-use, waste electricity Internet access" |
| ecoRule5.startTime | Start Time5 | HH:023 mm:059 |  | NO | String | Starting time, Format: HH:mm |
| ecoRule5.stopTime | Stop Time5 | HH:023 mm:059 |  | NO | String | Stop time, Format: HH:mm |
| ecoRule5.startDay | Start Day5 | MM:112 dd:131 |  | NO | String | Starting day, Format: MM:dd |
| ecoRule5.stopDay | Stop Day5 | MM:112 dd:131 |  | NO | String | Stop day, Format: MM:dd |
| ecoRule5.voltage | Voltage5 | 48~60 | V | NO | Number |  |
| ecoRule5.power | Power5 | 0~5000 | W | NO | Number |  |
| ecoRule5.daysOfEffectiveWeek | Effective Week5 | MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY |  | NO | Array | Week Of Use: Time Of Use Effective Week,Valuable：MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY，Multiple Choice |
| ecoRule5.soc | SOC5 | 0~100 | % | NO | Number |  |
| ecoRule6.ruleMode | ECO Mode 6 | 0:Disable  1:Charge  2:Discharge |  | NO | Number | "Economic model rules:  1) Disable: No charging and discharging  2) Charge: Charge the battery from the grid  3) Discharge: Selling power from battery to the grid  4)AC Couple:Spontaneous self-use, waste electricity Internet access" |
| ecoRule6.startTime | Start Time6 | HH:023 mm:059 |  | NO | String | Starting time, Format: HH:mm |
| ecoRule6.stopTime | Stop Time6 | HH:023 mm:059 |  | NO | String | Stop time, Format: HH:mm |
| ecoRule6.startDay | Start Day6 | MM:112 dd:131 |  | NO | String | Starting day, Format: MM:dd |
| ecoRule6.stopDay | Stop Day6 | MM:112 dd:131 |  | NO | String | Stop day, Format: MM:dd |
| ecoRule6.voltage | Voltage6 | 48~60 | V | NO | Number |  |
| ecoRule6.power | Power6 | 0~5000 | W | NO | Number |  |
| ecoRule6.daysOfEffectiveWeek | Effective Week6 | MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY |  | NO | Array | Week Of Use: Time Of Use Effective Week,Valuable：MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY，Multiple Choice |
| ecoRule6.soc | SOC6 | 0~100 | % | NO | Number |  |
| ecoRule7.ruleMode | ECO Mode 7 | 0:Disable  1:Charge  2:Discharge |  | NO | Number | "Economic model rules:  1) Disable: No charging and discharging  2) Charge: Charge the battery from the grid  3) Discharge: Selling power from battery to the grid  4)AC Couple:Spontaneous self-use, waste electricity Internet access" |
| ecoRule7.startTime | Start Time7 | HH:023 mm:059 |  | NO | String | Starting time, Format: HH:mm |
| ecoRule7.stopTime | Stop Time7 | HH:023 mm:059 |  | NO | String | Stop time, Format: HH:mm |
| ecoRule7.startDay | Start Day7 | MM:112 dd:131 |  | NO | String | Starting day, Format: MM:dd |
| ecoRule7.stopDay | Stop Day7 | MM:112 dd:131 |  | NO | String | Stop day, Format: MM:dd |
| ecoRule7.voltage | Voltage7 | 48~60 | V | NO | Number |  |
| ecoRule7.power | Power7 | 0~5000 | W | NO | Number |  |
| ecoRule7.daysOfEffectiveWeek | Effective Week7 | MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY |  | NO | Array | Week Of Use: Time Of Use Effective Week,Valuable：MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY，Multiple Choice |
| ecoRule7.soc | SOC7 | 0~100 | % | NO | Number |  |
| ecoRule8.ruleMode | ECO Mode 8 | 0:Disable  1:Charge  2:Discharge |  | NO | Number | "Economic model rules:  1) Disable: No charging and discharging  2) Charge: Charge the battery from the grid  3) Discharge: Selling power from battery to the grid  4)AC Couple:Spontaneous self-use, waste electricity Internet access" |
| ecoRule8.startTime | Start Time8 | HH:023 mm:059 |  | NO | String | Starting time, Format: HH:mm |
| ecoRule8.stopTime | Stop Time8 | HH:023 mm:059 |  | NO | String | Stop time, Format: HH:mm |
| ecoRule8.startDay | Start Day8 | MM:112 dd:131 |  | NO | String | Starting day, Format: MM:dd |
| ecoRule8.stopDay | Stop Day8 | MM:112 dd:131 |  | NO | String | Stop day, Format: MM:dd |
| ecoRule8.voltage | Voltage8 | 48~60 | V | NO | Number |  |
| ecoRule8.power | Power8 | 0~5000 | W | NO | Number |  |
| ecoRule8.daysOfEffectiveWeek | Effective Week8 | MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY |  | NO | Array | Week Of Use: Time Of Use Effective Week,Valuable：MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY，Multiple Choice |
| ecoRule8.soc | SOC8 | 0~100 | % | NO | Number |  |
| ecoRule9.ruleMode | ECO Mode 9 | 0:Disable  1:Charge  2:Discharge |  | NO | Number | "Economic model rules:  1) Disable: No charging and discharging  2) Charge: Charge the battery from the grid  3) Discharge: Selling power from battery to the grid  4)AC Couple:Spontaneous self-use, waste electricity Internet access" |
| ecoRule9.startTime | Start Time9 | HH:023 mm:059 |  | NO | String | Starting time, Format: HH:mm |
| ecoRule9.stopTime | Stop Time9 | HH:023 mm:059 |  | NO | String | Stop time, Format: HH:mm |
| ecoRule9.startDay | Start Day9 | MM:112 dd:131 |  | NO | String | Starting day, Format: MM:dd |
| ecoRule9.stopDay | Stop Day9 | MM:112 dd:131 |  | NO | String | Stop day, Format: MM:dd |
| ecoRule9.voltage | Voltage9 | 48~60 | V | NO | Number |  |
| ecoRule9.power | Power9 | 0~5000 | W | NO | Number |  |
| ecoRule9.daysOfEffectiveWeek | Effective Week9 | MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY |  | NO | Array | Week Of Use: Time Of Use Effective Week,Valuable：MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY，Multiple Choice |
| ecoRule9.soc | SOC9 | 0~100 | % | NO | Number |  |
| ecoRule10.ruleMode | ECO Mode 10 | 0:Disable  1:Charge  2:Discharge |  | NO | Number | "Economic model rules:  1) Disable: No charging and discharging  2) Charge: Charge the battery from the grid  3) Discharge: Selling power from battery to the grid  4)AC Couple:Spontaneous self-use, waste electricity Internet access" |
| ecoRule10.startTime | Start Time10 | HH:023 mm:059 |  | NO | String | Starting time, Format: HH:mm |
| ecoRule10.stopTime | Stop Time10 | HH:023 mm:059 |  | NO | String | Stop time, Format: HH:mm |
| ecoRule10.startDay | Start Day10 | MM:112 dd:131 |  | NO | String | Starting day, Format: MM:dd |
| ecoRule10.stopDay | Stop Day10 | MM:112 dd:131 |  | NO | String | Stop day, Format: MM:dd |
| ecoRule10.voltage | Voltage10 | 48~60 | V | NO | Number |  |
| ecoRule10.power | Power10 | 0~5000 | W | NO | Number |  |
| ecoRule10.daysOfEffectiveWeek | Effective Week10 | MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY |  | NO | Array | Week Of Use: Time Of Use Effective Week,Valuable：MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY，Multiple Choice |
| ecoRule10.soc | SOC10 | 0~100 | % | NO | Number |  |
| batteryModules | Battery Modules | 1~1 |  | NO | Number |  |
| batteryChargedVoltage | Battery Charged Voltage | 48~60 | V | NO | Number |  |
| batteryFloatingChargedVoltage | Bat float voltage | 48~60 | V | NO | Number |  |
| noBmsOnGridBatteryCutOffVoltage | Battery Cut-Off Voltage(On-Grid, No Bms) | 40~60 | V | NO | Number |  |
| noBmsOffGridBatteryCutOffVoltage | Battery Cut-Off Voltage(Off-Grid, No Bms) | 40~60 | V | NO | Number |  |
| noBmsOffGridBatteryRestartVoltage | Battery Restart Voltage(Off-Grid, No Bms) | 40~60 | V | NO | Number |  |
| batteryMaxChargedCurrent | Battery Max. Charged Current | 1~100 | A | NO | Number |  |
| batteryMaxDischargeCurrent | Battery Max. Discharged Current | 5~100 | A | NO | Number |  |
| parallelEnable | Parallel Enable | 0:Stand-Alone  1:Single Phase Parallel  2:Triphase Parallel-L1  3:Triphase Parallel-L2  4:Triphase Parallel-L3 |  | NO | Number | "Ensure that the inverter is operating in standby mode before setting it,Otherwise, it will cause machine malfunction." |
| --- | --- | --- | --- | --- | --- | --- |
| gridStandardCode | Standard | 0:Germany  1:Warehouse  2:50Hz grid default  3:60Hz grid default  4:Italy  5:Britain  6:Australia  7:New Zealand  8:South African  9:Netherland  10:Brazil  11:Europe  12:Poland  13:Czech |  | No | Number | Set the on-grid regulations in the current region |
| overVoltageStage1TripTime | OV Stage1 Trip Time | 0.02~1000 | Sec | No | Number |  |
| underVoltageStage1TripTime | UV Stage1 Trip Time | 0.02~1000 | Sec | No | Number |  |
| overVoltageStage2TripTime | OV Stage2 Trip Time | 0.02~1000 | Sec | No | Number |  |
| underVoltageStage2TripTime | UV Stage2 Trip Time | 0.02~1000 | Sec | No | Number |  |
| overVoltage10mTriggerValue | OV 10Min Mean Value | 230~300 | V | No | Number |  |
| overFrequencyStage1TripTime | OF Stage1 Trip Time | 0.02~1000 | Sec | No | Number |  |
| underFrequencyStage1TripTime | UF Stage1 Trip Time | 0.02~1000 | Sec | No | Number |  |
| overFrequencyStage2TripTime | OF Stage2 Trip Time | 0.02~1000 | Sec | No | Number |  |
| underFrequencyStage2TripTime | UF Stage2 Trip Time | 0.02~1000 | Sec | No | Number |  |
| onGridObservationTime | Observation Time | 1~3000 | Sec | No | Number |  |
| onGridPowerSlope | Grid Power Slope | 0~65535 | Sec | No | Number |  |
| onGridPowerLimit | Grid Power Limit | 0~100 | % | No | Number |  |
| pfPowerCurveFunctionEnable | PF-Power Curve Function | 0:Disable  1:Enable |  | No | Number |  |
| pfPowerCurvePointAPower | Point A Power | 0~100 | % | No | Number |  |
| pfPowerCurvePointAPowerFactor | Point A Power Factor | -0.99-0.8,0.81 |  | No | Number |  |
| pfPowerCurvePointBPower | Point B Power | 0~100 | % | No | Number |  |
| pfPowerCurvePointBPowerFactor | Point B Power Factor | -0.99-0.8,0.81 |  | No | Number |  |
| pfPowerCurvePointCPower | Point C Power | 0~100 | % | No | Number |  |
| pfPowerCurvePointCPowerFactor | Point C Power Factor | -0.99-0.8,0.81 |  | No | Number |  |
| pfPowerCurveLockoutPower | Lockout Power | 0~100 | % | No | Number |  |
| puCurveFunctionEnable | P(U) Curve Function | 0:Disable  1:Enable |  | No | Number |  |
| puCurvePointAActivePower | Point A  Active Power | -100~100 | % | No | Number |  |
| puCurvePointBActivePower | Point B  Active Power | -100~100 | % | No | Number |  |
| puCurvePointCActivePower | Point C  Active Power | -100~100 | % | No | Number |  |
| puCurvePointDActivePower | Point D  Active Power | -100~100 | % | No | Number |  |
| quCurveFunctionEnable | Q(U) Curve Function | 0:Disable  1:Enable |  | No | Number |  |
| quCurvePointAReactivePower | Point A  Reactive Power | -100~100 | % | No | Number |  |
| quCurvePointBReactivePower | Point B  Reactive Power | -100~100 | % | No | Number |  |
| quCurvePointCReactivePower | Point C  Reactive Power | -100~100 | % | No | Number |  |
| quCurvePointDReactivePower | Point D  Reactive Power | -100~100 | % | No | Number |  |
| quCurveLockInPower | Lock In Power | -100~100 | % | No | Number |  |
| quCurveLockOutPower | Lock Out Power | -100~100 | % | No | Number |  |
| fpCurveFunctionEnable | FP Curve Function | 0:Disable  1:Enable |  | No | Number |  |
| fpCurveOverFrequencyLowerLimit | Over Frequency Start Point | 30~80 | Hz | No | Number |  |
| fpUnderFrequencyLowerLimit | Under Frequency Start Point | 30~80 | Hz | No | Number |  |
| fpOverFrequencyUpperLimit | Over Frequency End Point | 30~80 | Hz | No | Number |  |
| fpUnderFrequencyUpperLimit | Under Frequency End Point | 30~80 | Hz | No | Number |  |
| fpRestoreFrequencyUperLimit | F(Stop) Upper | 30~80 | Hz | No | Number |  |
| fpRestoreFrequencyLowerLimit | F(Stop) Lower | 30~80 | Hz | No | Number |  |
| fpRestoreFrequencyWaitingTime | Restore Waiting Time | 1~65535 | Sec | No | Number |  |
| fpRestoreFrequencyPowerSlope | Reconnection Power Slope | 1~65535 | Sec | No | Number |  |
| fpOverFrequencyPowerSlope | Over Frequency Power Slope | 0~100 | % | No | Number |  |
| fpUnderFrequencyPowerSlope | Under Frequency Power Slope | 0~100 | % | No | Number |  |
| fpRecoveryPowerSlope | Recovery Power Slope | 0~100 | % | No | Number |  |
| fpChargeCurveFunctionEnable | FP Charge Curve Function | 0:Disable  1:Enable |  | No | Number |  |
| fpUnderFrequencyPowerSlopeForCharge | Under Frequency Power Slope For Charge | 0~100 | % | No | Number |  |
| lowVoltageRideThroughFunctionEnable | Low Voltage Ride Through | 0:Disable  1:Enable |  | No | Number |  |
| lowVoltageStartPointTripTime | Start Point Of Protection Time | 0.02~1000 | Sec | No | Number |  |
| lowVoltageEndPointTripTime | End Point Of Protection Time | 0.02~1000 | Sec | No | Number |  |
| highVoltageRideThroughFunctionEnable | High Voltage Ride Through Function | 0:Disable  1:Enable |  | No | Number |  |
| highVoltageStartPointTripTime | Start Point Of Protection Time | 0.02~1000 | Sec | No | Number |  |
| highVoltageEndPointTripTime | End Point Of Protection Time | 0.02~1000 | Sec | No | Number |  |
| overVoltageStage1TripValue | OV Stage1 Trip Value | 230~300 | V | No | Number |  |
| underVoltageStage1TripValue | UV Stage1 Trip Value | 0.1~300 | V | No | Number |  |
| overVoltageStage2TripValue | OV Stage2 Trip Value | 230~300 | V | No | Number |  |
| underVoltageStage2TripValue | UV Stage2 Trip Value | 0.1~300 | V | No | Number |  |
| overFrequencyStage1TripValue | OF Stage1 Trip Value | 30~80 | Hz | No | Number |  |
| underFrequencyStage1TripValue | UF Stage1 Trip Value | 30~80 | Hz | No | Number |  |
| overFrequencyStage2TripValue | OF Stage2 Trip Value | 30~80 | Hz | No | Number |  |
| underFrequencyStage2TripValue | UF Stage2 Trip Value | 30~80 | Hz | No | Number |  |
| pfPowerCurveLockinVoltage | Lockin Voltage | 60~300 | V | No | Number |  |
| pfPowerCurveLockoutVoltage | Lockout Voltage | 60~300 | V | No | Number |  |
| puCurvePointAVoltage | Point A Voltage | 60~300 | V | No | Number |  |
| puCurvePointBVoltage | Point B  Voltage | 60~300 | V | No | Number |  |
| puCurvePointCVoltage | Point C  Voltage | 60~300 | V | No | Number |  |
| puCurvePointDVoltage | Point D  Voltage | 60~300 | V | No | Number |  |
| quCurvePointAVoltage | Point A Voltage | 60~300 | V | No | Number |  |
| quCurvePointBVoltage | Point B  Voltage | 60~300 | V | No | Number |  |
| quCurvePointCVoltage | Point C  Voltage | 60~300 | V | No | Number |  |
| quCurvePointDVoltage | Point D  Voltage | 60~300 | V | No | Number |  |
| lowVoltageStartPointTripValue | Start Point Of Ride Through | 0~230 | V | No | Number |  |
| lowVoltageEndPointTripValue | End Point Of Ride Through | 0~230 | V | No | Number |  |
| lowVoltageCrossingTripThreshold | Low Voltage Limit Of Ride Through | 0~230 | V | No | Number |  |
| highVoltageStartPointTripValue | Start Point Of Ride Through | 230~300 | V | No | Number |  |
| highVoltageEndPointTripValue | End Point Of Ride Through | 230~300 | V | No | Number |  |
| highVoltageCrossingTripThreshold | High Voltage Limit Of Ride Through | 230~300 | V | No | Number |  |
| commOffLineEnable | CommOffLine | 0:Disable  1:Enable |  | No | Number |  |
| autoTestEnable | AutoTestEnable | 0:Disable  1:Enable |  | No | Number |  |
| deratingByVoltageEnable | DeratingByVoltage | 0:Disable  1:Enable |  | No | Number |  |

### IVGM5048

| Key | Name | Range | unit | Required | Type | Description |
| --- | ---- | ----- | ---- | -------- | ---- | ----------- |
| acOutputRatedVoltage | AC Output Rated Voltage | 220:220V  230:230V  240:240V | V | NO | Number |  |
| acOutputRatedFrequency | AC Output Rated Frequency | 0:50Hz  1:60Hz | Hz | NO | Number |  |
| gridPowerUnbalanceEnable | Grid Power Unbalance | 0:Disable  1:Enable |  | NO | Number |  |
| powerFactor | Power Factor | -0.99-0.8,0.81 |  | NO | Number |  |
| gridWaveformDetectionMode | Detection Mode | 0:Wave Detect  1:Half Wave Detect  2:Disable Wave Detect |  | NO | Number |  |
| batteryModel | Battery Model | 0:User defined  1:Third party(Lithium battery)  2:Felicity(LPBF/LUX-X series)  3:Felicity(LPBA/LUX-Y/LUX-E  series) |  | NO | Number |  |
| batteryOnGridDischargeDepthSoc | Battery Discharged Depth(On-Grid, Bms Connected) | 10~100 | % | NO | Number | The battery SOC is lower than the battery on-grid discharge depth, and the battery stops discharging |
| batteryOffGridDischargeDepthSoc | Battery Discharged Depth(Off-Grid, Bms Connected) | 0~100 | % | NO | Number | The battery SOC is lower than the battery off-grid discharge depth, and the battery stops discharging |
| batteryOffGridRecoveryDepthSoc | Battery Restart Depth(Off-Grid, Bms Connected) | 0~100 | % | NO | Number | When the battery SOC is lower than the setting value of "Battery discharge depth (off grid)", the inverter can only be output off the grid again after the SOC recovers to the setting value higher than "Battery restart depth |
| lcdBacklightEnable | LCD Backlight | 0:Disable  1:Enable |  | NO | Number |  |
| buzzerEnable | Buzzer | 0:Disable  1:Enable |  | NO | Number |  |
| overLoadProtectionResetEnable | Over Load Protection Reset | 0:Disable  1:Enable |  | NO | Number | The fault will be cleared automatically after the overload protection of the machine. If the overload protection occurs 3 times within half an hour, the overload fault will not be cleared |
| remoteOnOffEnable | Remote control | 0:ON  1:OFF |  | NO | Number | The machine shuts down and enters standby mode |
| remoteOutputOnOffControl | AC Output ON/OFF | 0:ON  1:OFF |  | NO | Number |  |
| zeroExportFunction | Zero Export Mode | 1:To load  2:To CT |  | NO | Number | "The feed power is limited according to the setting of ""grid connection power limit"".  1) To load:  The inverter can supply power to the backup load and sell power to the grid but the selling power will not exceed the setting value of ""grid connection power limit""  2) To CT:  The inverter can supply power to the backup load, household load and sell power to the grid, but the selling power will not exceed the setting value of ""grid connection power limit"".In this mode, a CT is needed." |
| zeroExportAdjustmentPower | Zero Export Power | -500~500 | W | NO | Number | When the grid-connected power is set to 0, it is used to calibrate the sampling deviation to ensure that the inverter will not feed power to the grid |
| clearEnergyStorageLog | Clear Energy Storage Log | 1:Clear |  | NO | Number |  |
| clearEventLog | Clear Event Log | 1:Clear |  | NO | Number |  |
| factoryReset | Factory Reset | 1:Reset |  | NO | Number |  |
| eventLogFunctionEnable | Event Log Function | 0:Disable  1:Charge  2:Discharge |  | NO | Number |  |
| faultLogFunctionEnable | Fault Log Function | 0:Disable  1:Charge  2:Discharge |  | NO | Number |  |
| gfciLevel1ProtectionEnable | GFCI One-level Protection | 0:Disable  1:Charge  2:Discharge |  | NO | Number |  |
| gfciLevel2ProtectionEnable | GFCI Two-level Protection | 0:Disable  1:Charge  2:Discharge |  | NO | Number |  |
| gfciLevel3ProtectionEnable | GFCI Three-level Protection | 0:Disable  1:Charge  2:Discharge |  | NO | Number |  |
| isoDetectionEnable | ISO Detection | 0:Disable  1:Charge  2:Discharge |  | NO | Number |  |
| antiIslandingDetectionEnable | Anti-Islanding Detection | 0:Disable  1:Charge  2:Discharge |  | NO | Number |  |
| pvParallelSetting | PV Parallel Set | 0:Stand Alone  1:Parallel |  | NO | Number |  |
| fixQPencent | FixQ Pencent | -60~60 | % | NO | Number |  |
| bmsHeartbeat | BMS Heartbeat | 0:Disable  1:Charge  2:Discharge |  | NO | Number | After enabling, if the battery type is lithium battery and BMS communication fails, it will report BMS communication failure |
| operatedMode | Operated Mode | 0:General Mode  1:Backup Mode  2:Eco Mode  3:Gen Mode |  | NO | Number | "Set inverter operation mode:  1) General mode:  In this mode, the load is mainly powered by PV and battery.  2) Backup mode:  In this mode, PV gives priority to charging the battery to ensure that the battery is always full.  3) ECO mode:  In this mode, you can set a specific time to take power from the grid to charge the battery or use the power of the grid to charge the battery, and operate in general mode outside the set time.  4) Generator mode:  In this mode, the load is mainly powered by PV and battery." |
| ecoRule1.ruleMode | ECO Mode 1 | 0:Disable  1:Charge  2:Discharge   3:AC Couple |  | NO | Number | "Economic model rules:  1) Disable: No charging and discharging  2) Charge: Charge the battery from the grid  3) Discharge: Selling power from battery to the grid  4)AC Couple:Spontaneous self-use, waste electricity Internet access" |
| ecoRule1.startTime | Start Time1 | HH:023 mm:059 |  | NO | String | Starting time, Format: HH:mm |
| ecoRule1.stopTime | Stop Time1 | HH:023 mm:059 |  | NO | String | Stop time, Format: HH:mm |
| ecoRule1.startDay | Start Day1 | MM:112 dd:131 |  | NO | String | Starting day, Format: MM:dd |
| ecoRule1.stopDay | Stop Day1 | MM:112 dd:131 |  | NO | String | Stop day, Format: MM:dd |
| ecoRule1.daysOfEffectiveWeek | Effective Week1 | MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY |  | NO | Array | Week Of Use: Time Of Use Effective Week,Valuable：MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY，Multiple Choice |
| ecoRule1.soc | SOC1 | 0~100 | % | NO | Number |  |
| ecoRule1.voltage | Voltage1 | 48~60 | V | NO | Number | "1) Charging: Stop charging voltage. Battery voltage above this value stops charging (usually set to 57.6v for a single battery).  2) Discharge: Stop discharge voltage. If the battery voltage is lower than this value, it will stop discharging." |
| ecoRule1.power | Power1 | "Slave Version <203 : 05000  Slave Version ≥203 : -50005000" | W | NO | Number | "1) Charging: Battery charging power  2) Discharge: Battery discharge power  3)Dispatched power: Grid power supply or intake power" |
| ecoRule2.ruleMode | ECO Mode 2 | 0:Disable  1:Charge  2:Discharge   3:AC Couple |  | NO | Number | "Economic model rules:  1) Disable: No charging and discharging  2) Charge: Charge the battery from the grid  3) Discharge: Selling power from battery to the grid  4)AC Couple:Spontaneous self-use, waste electricity Internet access" |
| ecoRule2.startTime | Start Time2 | HH:023 mm:059 |  | NO | String | Starting time, Format: HH:mm |
| ecoRule2.stopTime | Stop Time2 | HH:023 mm:059 |  | NO | String | Stop time, Format: HH:mm |
| ecoRule2.startDay | Start Day2 | MM:112 dd:131 |  | NO | String | Starting day, Format: MM:dd |
| ecoRule2.stopDay | Stop Day2 | MM:112 dd:131 |  | NO | String | Stop day, Format: MM:dd |
| ecoRule2.voltage | Voltage2 | 48~60 | V | NO | Number | "1) Charging: Stop charging voltage. Battery voltage above this value stops charging (usually set to 57.6v for a single battery).  2) Discharge: Stop discharge voltage. If the battery voltage is lower than this value, it will stop discharging." |
| ecoRule2.power | Power2 | "Slave Version <203 : 0~5000 |  |  |  |  |
| Slave Version ≥203 : -5000~5000" | W | NO | Number | "1) Charging: Battery charging power  2) Discharge: Battery discharge power  3)Dispatched power: Grid power supply or intake power" |  |  |
| ecoRule2.daysOfEffectiveWeek | Effective Week2 | MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY |  | NO | Array | Week Of Use: Time Of Use Effective Week,Valuable：MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY，Multiple Choice |
| ecoRule2.soc | SOC2 | 0~100 | % | NO | Number |  |
| ecoRule3.ruleMode | ECO Mode 3 | 0:Disable  1:Charge  2:Discharge   3:AC Couple |  | NO | Number | "Economic model rules:  1) Disable: No charging and discharging  2) Charge: Charge the battery from the grid  3) Discharge: Selling power from battery to the grid  4)AC Couple:Spontaneous self-use, waste electricity Internet access" |
| ecoRule3.startTime | Start Time3 | HH:023 mm:059 |  | NO | String | Starting time, Format: HH:mm |
| ecoRule3.stopTime | Stop Time3 | HH:023 mm:059 |  | NO | String | Stop time, Format: HH:mm |
| ecoRule3.startDay | Start Day3 | MM:112 dd:131 |  | NO | String | Starting day, Format: MM:dd |
| ecoRule3.stopDay | Stop Day3 | MM:112 dd:131 |  | NO | String | Stop day, Format: MM:dd |
| ecoRule3.daysOfEffectiveWeek | Effective Week3 | MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY |  | NO | Array | Week Of Use: Time Of Use Effective Week,Valuable：MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY，Multiple Choice |
| ecoRule3.soc | SOC3 | 0~100 | % | NO | Number |  |
| ecoRule3.voltage | Voltage3 | 48~60 | V | NO | Number | "1) Charging: Stop charging voltage. Battery voltage above this value stops charging (usually set to 57.6v for a single battery).  2) Discharge: Stop discharge voltage. If the battery voltage is lower than this value, it will stop discharging." |
| ecoRule3.power | Power3 | "Slave Version <203 : 05000  Slave Version ≥203 : -50005000" | W | NO | Number | "1) Charging: Battery charging power  2) Discharge: Battery discharge power |
| 3)Dispatched power: Grid power supply or intake power" |  |  |  |  |  |  |
| ecoRule4.ruleMode | ECO Mode 4 | 0:Disable  1:Charge  2:Discharge   3:AC Couple |  | NO | Number | "Economic model rules:  1) Disable: No charging and discharging  2) Charge: Charge the battery from the grid  3) Discharge: Selling power from battery to the grid  4)AC Couple:Spontaneous self-use, waste electricity Internet access" |
| ecoRule4.startTime | Start Time4 | HH:023 mm:059 |  | NO | String | Starting time, Format: HH:mm |
| ecoRule4.stopTime | Stop Time4 | HH:023 mm:059 |  | NO | String | Stop time, Format: HH:mm |
| ecoRule4.startDay | Start Day4 | MM:112 dd:131 |  | NO | String | Starting day, Format: MM:dd |
| ecoRule4.stopDay | Stop Day4 | MM:112 dd:131 |  | NO | String | Stop day, Format: MM:dd |
| ecoRule4.voltage | Voltage4 | 48~60 | V | NO | Number | "1) Charging: Stop charging voltage. Battery voltage above this value stops charging (usually set to 57.6v for a single battery).  2) Discharge: Stop discharge voltage. If the battery voltage is lower than this value, it will stop discharging." |
| ecoRule4.power | Power4 | "Slave Version <203 : 05000  Slave Version ≥203 : -50005000" | W | NO | Number | "1) Charging: Battery charging power  2) Discharge: Battery discharge power  3)Dispatched power: Grid power supply or intake power" |
| ecoRule4.daysOfEffectiveWeek | Effective Week4 | MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY |  | NO | Array | Week Of Use: Time Of Use Effective Week,Valuable：MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY，Multiple Choice |
| ecoRule4.soc | SOC4 | 0~100 | % | NO | Number |  |
| additionalEcoEnable | ECO 10 enable | 0:Disable  1:Enable |  | NO | Number | Only when Master Version ≥ 2204，parameter can be used, ecoRule5 ~ecoRule10 also.After enabling, there will be 10 economic rules that can be set.Only trial on some devices. If there is no value displayed or it cannot run, please use the old 4-segment mode. |
| ecoRule5.ruleMode | ECO Mode 5 | 0:Disable  1:Charge  2:Discharge |  | NO | Number | "Economic model rules:  1) Disable: No charging and discharging  2) Charge: Charge the battery from the grid  3) Discharge: Selling power from battery to the grid  4)AC Couple:Spontaneous self-use, waste electricity Internet access" |
| ecoRule5.startTime | Start Time5 | HH:023 mm:059 |  | NO | String | Starting time, Format: HH:mm |
| ecoRule5.stopTime | Stop Time5 | HH:023 mm:059 |  | NO | String | Stop time, Format: HH:mm |
| ecoRule5.startDay | Start Day5 | MM:112 dd:131 |  | NO | String | Starting day, Format: MM:dd |
| ecoRule5.stopDay | Stop Day5 | MM:112 dd:131 |  | NO | String | Stop day, Format: MM:dd |
| ecoRule5.voltage | Voltage5 | 48~60 | V | NO | Number |  |
| ecoRule5.power | Power5 | 0~5000 | W | NO | Number |  |
| ecoRule5.daysOfEffectiveWeek | Effective Week5 | MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY |  | NO | Array | Week Of Use: Time Of Use Effective Week,Valuable：MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY，Multiple Choice |
| ecoRule5.soc | SOC5 | 0~100 | % | NO | Number |  |
| ecoRule6.ruleMode | ECO Mode 6 | 0:Disable  1:Charge  2:Discharge |  | NO | Number | "Economic model rules:  1) Disable: No charging and discharging  2) Charge: Charge the battery from the grid  3) Discharge: Selling power from battery to the grid  4)AC Couple:Spontaneous self-use, waste electricity Internet access" |
| ecoRule6.startTime | Start Time6 | HH:023 mm:059 |  | NO | String | Starting time, Format: HH:mm |
| ecoRule6.stopTime | Stop Time6 | HH:023 mm:059 |  | NO | String | Stop time, Format: HH:mm |
| ecoRule6.startDay | Start Day6 | MM:112 dd:131 |  | NO | String | Starting day, Format: MM:dd |
| ecoRule6.stopDay | Stop Day6 | MM:112 dd:131 |  | NO | String | Stop day, Format: MM:dd |
| ecoRule6.voltage | Voltage6 | 48~60 | V | NO | Number |  |
| ecoRule6.power | Power6 | 0~5000 | W | NO | Number |  |
| ecoRule6.daysOfEffectiveWeek | Effective Week6 | MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY |  | NO | Array | Week Of Use: Time Of Use Effective Week,Valuable：MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY，Multiple Choice |
| ecoRule6.soc | SOC6 | 0~100 | % | NO | Number |  |
| ecoRule7.ruleMode | ECO Mode 7 | 0:Disable  1:Charge  2:Discharge |  | NO | Number | "Economic model rules:  1) Disable: No charging and discharging  2) Charge: Charge the battery from the grid  3) Discharge: Selling power from battery to the grid  4)AC Couple:Spontaneous self-use, waste electricity Internet access" |
| ecoRule7.startTime | Start Time7 | HH:023 mm:059 |  | NO | String | Starting time, Format: HH:mm |
| ecoRule7.stopTime | Stop Time7 | HH:023 mm:059 |  | NO | String | Stop time, Format: HH:mm |
| ecoRule7.startDay | Start Day7 | MM:112 dd:131 |  | NO | String | Starting day, Format: MM:dd |
| ecoRule7.stopDay | Stop Day7 | MM:112 dd:131 |  | NO | String | Stop day, Format: MM:dd |
| ecoRule7.voltage | Voltage7 | 48~60 | V | NO | Number |  |
| ecoRule7.power | Power7 | 0~5000 | W | NO | Number |  |
| ecoRule7.daysOfEffectiveWeek | Effective Week7 | MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY |  | NO | Array | Week Of Use: Time Of Use Effective Week,Valuable：MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY，Multiple Choice |
| ecoRule7.soc | SOC7 | 0~100 | % | NO | Number |  |
| ecoRule8.ruleMode | ECO Mode 8 | 0:Disable  1:Charge  2:Discharge |  | NO | Number | "Economic model rules:  1) Disable: No charging and discharging  2) Charge: Charge the battery from the grid  3) Discharge: Selling power from battery to the grid  4)AC Couple:Spontaneous self-use, waste electricity Internet access" |
| ecoRule8.startTime | Start Time8 | HH:023 mm:059 |  | NO | String | Starting time, Format: HH:mm |
| ecoRule8.stopTime | Stop Time8 | HH:023 mm:059 |  | NO | String | Stop time, Format: HH:mm |
| ecoRule8.startDay | Start Day8 | MM:112 dd:131 |  | NO | String | Starting day, Format: MM:dd |
| ecoRule8.stopDay | Stop Day8 | MM:112 dd:131 |  | NO | String | Stop day, Format: MM:dd |
| ecoRule8.voltage | Voltage8 | 48~60 | V | NO | Number |  |
| ecoRule8.power | Power8 | 0~5000 | W | NO | Number |  |
| ecoRule8.daysOfEffectiveWeek | Effective Week8 | MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY |  | NO | Array | Week Of Use: Time Of Use Effective Week,Valuable：MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY，Multiple Choice |
| ecoRule8.soc | SOC8 | 0~100 | % | NO | Number |  |
| ecoRule9.ruleMode | ECO Mode 9 | 0:Disable  1:Charge  2:Discharge |  | NO | Number | "Economic model rules:  1) Disable: No charging and discharging  2) Charge: Charge the battery from the grid  3) Discharge: Selling power from battery to the grid  4)AC Couple:Spontaneous self-use, waste electricity Internet access" |
| ecoRule9.startTime | Start Time9 | HH:023 mm:059 |  | NO | String | Starting time, Format: HH:mm |
| ecoRule9.stopTime | Stop Time9 | HH:023 mm:059 |  | NO | String | Stop time, Format: HH:mm |
| ecoRule9.startDay | Start Day9 | MM:112 dd:131 |  | NO | String | Starting day, Format: MM:dd |
| ecoRule9.stopDay | Stop Day9 | MM:112 dd:131 |  | NO | String | Stop day, Format: MM:dd |
| ecoRule9.voltage | Voltage9 | 48~60 | V | NO | Number |  |
| ecoRule9.power | Power9 | 0~5000 | W | NO | Number |  |
| ecoRule9.daysOfEffectiveWeek | Effective Week9 | MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY |  | NO | Array | Week Of Use: Time Of Use Effective Week,Valuable：MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY，Multiple Choice |
| ecoRule9.soc | SOC9 | 0~100 | % | NO | Number |  |
| ecoRule10.ruleMode | ECO Mode 10 | 0:Disable  1:Charge  2:Discharge |  | NO | Number | "Economic model rules:  1) Disable: No charging and discharging  2) Charge: Charge the battery from the grid  3) Discharge: Selling power from battery to the grid  4)AC Couple:Spontaneous self-use, waste electricity Internet access" |
| ecoRule10.startTime | Start Time10 | HH:023 mm:059 |  | NO | String | Starting time, Format: HH:mm |
| ecoRule10.stopTime | Stop Time10 | HH:023 mm:059 |  | NO | String | Stop time, Format: HH:mm |
| ecoRule10.startDay | Start Day10 | MM:112 dd:131 |  | NO | String | Starting day, Format: MM:dd |
| ecoRule10.stopDay | Stop Day10 | MM:112 dd:131 |  | NO | String | Stop day, Format: MM:dd |
| ecoRule10.voltage | Voltage10 | 48~60 | V | NO | Number |  |
| ecoRule10.power | Power10 | 0~5000 | W | NO | Number |  |
| ecoRule10.daysOfEffectiveWeek | Effective Week10 | MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY |  | NO | Array | Week Of Use: Time Of Use Effective Week,Valuable：MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY，Multiple Choice |
| ecoRule10.soc | SOC10 | 0~100 | % | NO | Number |  |
| batteryModules | Battery Modules | 1~1 |  | NO | Number |  |
| batteryChargedVoltage | Battery Charged Voltage | 48~60 | V | NO | Number |  |
| batteryFloatingChargedVoltage | Bat float voltage | 48~60 | V | NO | Number |  |
| noBmsOnGridBatteryCutOffVoltage | Battery Cut-Off Voltage(On-Grid, No Bms) | 40~60 | V | NO | Number |  |
| noBmsOffGridBatteryCutOffVoltage | Battery Cut-Off Voltage(Off-Grid, No Bms) | 40~60 | V | NO | Number |  |
| noBmsOffGridBatteryRestartVoltage | Battery Restart Voltage(Off-Grid, No Bms) | 40~60 | V | NO | Number |  |
| batteryMaxChargedCurrent | Battery Max. Charged Current | 1~100 | A | NO | Number |  |
| batteryMaxDischargeCurrent | Battery Max. Discharged Current | 5~100 | A | NO | Number |  |
| parallelEnable | Parallel Enable | 0:Stand-Alone  1:Single Phase Parallel  2:Triphase Parallel-L1  3:Triphase Parallel-L2  4:Triphase Parallel-L3 |  | NO | Number | "Ensure that the inverter is operating in standby mode before setting it, Otherwise, it will cause machine malfunction." |
| --- | --- | --- | --- | --- | --- | --- |
| gridStandardCode | Standard | 0:Germany  1:Warehouse  2:50Hz grid default  3:60Hz grid default  4:Italy  5:Britain  6:Australia  7:New Zealand  8:South African  9:Netherland  10:Brazil  11:Europe  12:Poland  13:Czech |  | No | Number | Set the on-grid regulations in the current region |
| overVoltageStage1TripTime | OV Stage1 Trip Time | 0.02~1000 | Sec | No | Number |  |
| underVoltageStage1TripTime | UV Stage1 Trip Time | 0.02~1000 | Sec | No | Number |  |
| overVoltageStage2TripTime | OV Stage2 Trip Time | 0.02~1000 | Sec | No | Number |  |
| underVoltageStage2TripTime | UV Stage2 Trip Time | 0.02~1000 | Sec | No | Number |  |
| overVoltage10mTriggerValue | OV 10Min Mean Value | 230~300 | V | No | Number |  |
| overFrequencyStage1TripTime | OF Stage1 Trip Time | 0.02~1000 | Sec | No | Number |  |
| underFrequencyStage1TripTime | UF Stage1 Trip Time | 0.02~1000 | Sec | No | Number |  |
| overFrequencyStage2TripTime | OF Stage2 Trip Time | 0.02~1000 | Sec | No | Number |  |
| underFrequencyStage2TripTime | UF Stage2 Trip Time | 0.02~1000 | Sec | No | Number |  |
| onGridObservationTime | Observation Time | 1~3000 | Sec | No | Number |  |
| onGridPowerSlope | Grid Power Slope | 0~65535 | Sec | No | Number |  |
| onGridPowerLimit | Grid Power Limit | 0~100 | % | No | Number |  |
| pfPowerCurveFunctionEnable | PF-Power Curve Function | 0:Disable  1:Enable |  | No | Number |  |
| pfPowerCurvePointAPower | Point A Power | 0~100 | % | No | Number |  |
| pfPowerCurvePointAPowerFactor | Point A Power Factor | -0.99-0.8,0.81 |  | No | Number |  |
| pfPowerCurvePointBPower | Point B Power | 0~100 | % | No | Number |  |
| pfPowerCurvePointBPowerFactor | Point B Power Factor | -0.99-0.8,0.81 |  | No | Number |  |
| pfPowerCurvePointCPower | Point C Power | 0~100 | % | No | Number |  |
| pfPowerCurvePointCPowerFactor | Point C Power Factor | -0.99-0.8,0.81 |  | No | Number |  |
| pfPowerCurveLockoutPower | Lockout Power | 0~100 | % | No | Number |  |
| puCurveFunctionEnable | P(U) Curve Function | 0:Disable  1:Enable |  | No | Number |  |
| puCurvePointAActivePower | Point A  Active Power | -100~100 | % | No | Number |  |
| puCurvePointBActivePower | Point B  Active Power | -100~100 | % | No | Number |  |
| puCurvePointCActivePower | Point C  Active Power | -100~100 | % | No | Number |  |
| puCurvePointDActivePower | Point D  Active Power | -100~100 | % | No | Number |  |
| quCurveFunctionEnable | Q(U) Curve Function | 0:Disable  1:Enable |  | No | Number |  |
| quCurvePointAReactivePower | Point A  Reactive Power | -100~100 | % | No | Number |  |
| quCurvePointBReactivePower | Point B  Reactive Power | -100~100 | % | No | Number |  |
| quCurvePointCReactivePower | Point C  Reactive Power | -100~100 | % | No | Number |  |
| quCurvePointDReactivePower | Point D  Reactive Power | -100~100 | % | No | Number |  |
| quCurveLockInPower | Lock In Power | -100~100 | % | No | Number |  |
| quCurveLockOutPower | Lock Out Power | -100~100 | % | No | Number |  |
| fpCurveFunctionEnable | FP Curve Function | 0:Disable  1:Enable |  | No | Number |  |
| fpCurveOverFrequencyLowerLimit | Over Frequency Start Point | 30~80 | Hz | No | Number |  |
| fpUnderFrequencyLowerLimit | Under Frequency Start Point | 30~80 | Hz | No | Number |  |
| fpOverFrequencyUpperLimit | Over Frequency End Point | 30~80 | Hz | No | Number |  |
| fpUnderFrequencyUpperLimit | Under Frequency End Point | 30~80 | Hz | No | Number |  |
| fpRestoreFrequencyUperLimit | F(Stop) Upper | 30~80 | Hz | No | Number |  |
| fpRestoreFrequencyLowerLimit | F(Stop) Lower | 30~80 | Hz | No | Number |  |
| fpRestoreFrequencyWaitingTime | Restore Waiting Time | 1~65535 | Sec | No | Number |  |
| fpRestoreFrequencyPowerSlope | Reconnection Power Slope | 1~65535 | Sec | No | Number |  |
| fpOverFrequencyPowerSlope | Over Frequency Power Slope | 0~100 | % | No | Number |  |
| fpUnderFrequencyPowerSlope | Under Frequency Power Slope | 0~100 | % | No | Number |  |
| fpRecoveryPowerSlope | Recovery Power Slope | 0~100 | % | No | Number |  |
| fpChargeCurveFunctionEnable | FP Charge Curve Function | 0:Disable  1:Enable |  | No | Number |  |
| fpUnderFrequencyPowerSlopeForCharge | Under Frequency Power Slope For Charge | 0~100 | % | No | Number |  |
| lowVoltageRideThroughFunctionEnable | Low Voltage Ride Through | 0:Disable  1:Enable |  | No | Number |  |
| lowVoltageStartPointTripTime | Start Point Of Protection Time | 0.02~1000 | Sec | No | Number |  |
| lowVoltageEndPointTripTime | End Point Of Protection Time | 0.02~1000 | Sec | No | Number |  |
| highVoltageRideThroughFunctionEnable | High Voltage Ride Through Function | 0:Disable  1:Enable |  | No | Number |  |
| highVoltageStartPointTripTime | Start Point Of Protection Time | 0.02~1000 | Sec | No | Number |  |
| highVoltageEndPointTripTime | End Point Of Protection Time | 0.02~1000 | Sec | No | Number |  |
| overVoltageStage1TripValue | OV Stage1 Trip Value | 230~300 | V | No | Number |  |
| underVoltageStage1TripValue | UV Stage1 Trip Value | 0.1~300 | V | No | Number |  |
| overVoltageStage2TripValue | OV Stage2 Trip Value | 230~300 | V | No | Number |  |
| underVoltageStage2TripValue | UV Stage2 Trip Value | 0.1~300 | V | No | Number |  |
| overFrequencyStage1TripValue | OF Stage1 Trip Value | 30~80 | Hz | No | Number |  |
| underFrequencyStage1TripValue | UF Stage1 Trip Value | 30~80 | Hz | No | Number |  |
| overFrequencyStage2TripValue | OF Stage2 Trip Value | 30~80 | Hz | No | Number |  |
| underFrequencyStage2TripValue | UF Stage2 Trip Value | 30~80 | Hz | No | Number |  |
| pfPowerCurveLockinVoltage | Lockin Voltage | 60~300 | V | No | Number |  |
| pfPowerCurveLockoutVoltage | Lockout Voltage | 60~300 | V | No | Number |  |
| puCurvePointAVoltage | Point A Voltage | 60~300 | V | No | Number |  |
| puCurvePointBVoltage | Point B  Voltage | 60~300 | V | No | Number |  |
| puCurvePointCVoltage | Point C  Voltage | 60~300 | V | No | Number |  |
| puCurvePointDVoltage | Point D  Voltage | 60~300 | V | No | Number |  |
| quCurvePointAVoltage | Point A Voltage | 60~300 | V | No | Number |  |
| quCurvePointBVoltage | Point B  Voltage | 60~300 | V | No | Number |  |
| quCurvePointCVoltage | Point C  Voltage | 60~300 | V | No | Number |  |
| quCurvePointDVoltage | Point D  Voltage | 60~300 | V | No | Number |  |
| lowVoltageStartPointTripValue | Start Point Of Ride Through | 0~230 | V | No | Number |  |
| lowVoltageEndPointTripValue | End Point Of Ride Through | 0~230 | V | No | Number |  |
| lowVoltageCrossingTripThreshold | Low Voltage Limit Of Ride Through | 0~230 | V | No | Number |  |
| highVoltageStartPointTripValue | Start Point Of Ride Through | 230~300 | V | No | Number |  |
| highVoltageEndPointTripValue | End Point Of Ride Through | 230~300 | V | No | Number |  |
| highVoltageCrossingTripThreshold | High Voltage Limit Of Ride Through | 230~300 | V | No | Number |  |
| commOffLineEnable | CommOffLine | 0:Disable  1:Enable |  | No | Number |  |
| autoTestEnable | AutoTestEnable | 0:Disable  1:Enable |  | No | Number |  |
| deratingByVoltageEnable | DeratingByVoltage | 0:Disable  1:Enable |  | No | Number |  |

**Request Body Example.**

```json
{
    
    "batteryMode":1,
    "ecoRule1": {
        "soc":56,
        "startTime":"10:07",
        "stopTime":"13:05",
        "power":30,
        "daysOfEffectiveWeek":["MONDAY", "TUESDAY"]
    },
   
    "touEffectiveWeek":["MONDAY", "TUESDAY"],
    "deviceSn": "013548202500010000"
}
```

**Query**

## Query Remote Control Setting value

> Created by: Timesup

> Updated by: Timesup

> Created at: 2024-06-22 04:19:50

> Updated at: 2024-08-21 03:02:53

**The application server can call this interface to remotely query parameters of devices (inverters, etc.) through the Fsolar platform.
Default support T-REX-6KLP1G01、T-REX-10KHP3G01、T-REX-5KLP1G01、T-REX-10KLP3G01. 
More device support see: Query Remote Control Setting Attachment**

**Interface Status**

> Completed

**Interface URL**

> /openApi/cmd/deviceSetting/{deviceSn}

**Request Method**

> GET

**Content-Type**

> form-data

**Request Header Parameters**

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| Content-Type | application/x-www-form-urlencoded | string | Yes | - |
| Authorization | Bearer_eyJhbGciOiJIUzI1NiJ9.eyJkZW1vVXNlciI6ZmFsc2UsInN1YiI6IueuoeeQhuWRmCIsImF1ZCI6Ik56TTNORFF4TkRrd01UVTFPREUwTkE9PSIsIm5iZiI6MTcxMTY3NjY4NiwiaXNzIjoiRkxTLVNPTEFSLVNFUlZFUiIsImlkIjo3Mzc0NDE0OTAxNTU4MTQ0LCJleHAiOjE3MTQyNjg2ODYsImlhdCI6MTcxMTY3NjY4Nn0._l5VIYevtyv2Xc66S9w6fqmkECBFvLZPJYqjU07pObE | string | Yes | User token, which can be obtained from authentication and refreshing tokens. |
| Lang | en_US | string | Yes | Language, currently supports English en_US. |

**Path Variables**

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| deviceSn | - | string | Yes | deviceSn |

**Request Body Parameters**

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| deviceSn | - | string | Yes | DeviceSN |

**Authentication Method**

> Inherit from parent

**Response Example**

* OK(200)

```javascript
{
	"code": 0,
	"message": "",
	"data": {
		"acOutputRatedFrequency": 0,
		"acOutputRatedVoltage": "",
		"antiIslandingDetectionEnable": 0,
		"batteryChargedVoltage": "",
		"batteryFloatingChargedVoltage": "",
		"batteryMaxChargedCurrent": "",
		"batteryMaxDischargeCurrent": "",
		"batteryModel": 0,
		"batteryModules": 0,
		"batteryOffGridDischargeDepthSoc": 0,
		"batteryOffGridRecoveryDepthSoc": 0,
		"batteryOnGridDischargeDepthSoc": 0,
		"buzzerEnable": 0,
		"commOffLineEnable": 0,
		"deratingByVoltageEnable": 0,
		"deviceSn": "",
		"ecoRule1": {
			"daysOfEffectiveWeek": [
				""
			],
			"power": 0,
			"ruleMode": 0,
			"soc": 0,
			"startDay": "",
			"startTime": "",
			"stopDay": "",
			"stopTime": "",
			"voltage": ""
		},
		"ecoRule2": {
			"daysOfEffectiveWeek": [
				""
			],
			"power": 0,
			"ruleMode": 0,
			"soc": 0,
			"startDay": "",
			"startTime": "",
			"stopDay": "",
			"stopTime": "",
			"voltage": ""
		},
		"ecoRule3": {
			"daysOfEffectiveWeek": [
				""
			],
			"power": 0,
			"ruleMode": 0,
			"soc": 0,
			"startDay": "",
			"startTime": "",
			"stopDay": "",
			"stopTime": "",
			"voltage": ""
		},
		"ecoRule4": {
			"daysOfEffectiveWeek": [
				""
			],
			"power": 0,
			"ruleMode": 0,
			"soc": 0,
			"startDay": "",
			"startTime": "",
			"stopDay": "",
			"stopTime": "",
			"voltage": ""
		},
		"eventLogFunctionEnable": 0,
		"faultLogFunctionEnable": 0,
		"fixQPencent": "",
		"fpChargeCurveFunctionEnable": 0,
		"fpCurveFunctionEnable": 0,
		"fpCurveOverFrequencyLowerLimit": "",
		"fpOverFrequencyPowerSlope": "",
		"fpOverFrequencyUpperLimit": "",
		"fpRecoveryPowerSlope": "",
		"fpRestoreFrequencyLowerLimit": "",
		"fpRestoreFrequencyPowerSlope": 0,
		"fpRestoreFrequencyUperLimit": "",
		"fpRestoreFrequencyWaitingTime": 0,
		"fpUnderFrequencyLowerLimit": "",
		"fpUnderFrequencyPowerSlope": "",
		"fpUnderFrequencyPowerSlopeForCharge": "",
		"fpUnderFrequencyUpperLimit": "",
		"gridPowerUnbalanceEnable": 0,
		"gridStandardCode": 0,
		"gridWaveformDetectionMode": 0,
		"highVoltageCrossingTripThreshold": "",
		"highVoltageEndPointTripTime": "",
		"highVoltageEndPointTripValue": "",
		"highVoltageRideThroughFunctionEnable": 0,
		"highVoltageStartPointTripTime": "",
		"highVoltageStartPointTripValue": "",
		"isoDetectionEnable": 0,
		"lcdBacklightEnable": 0,
		"lowVoltageCrossingTripThreshold": "",
		"lowVoltageEndPointTripTime": "",
		"lowVoltageEndPointTripValue": "",
		"lowVoltageRideThroughFunctionEnable": 0,
		"lowVoltageStartPointTripTime": "",
		"lowVoltageStartPointTripValue": "",
		"noBmsOffGridBatteryCutOffVoltage": "",
		"noBmsOffGridBatteryRestartVoltage": "",
		"noBmsOnGridBatteryCutOffVoltage": "",
		"onGridObservationTime": 0,
		"onGridPowerLimit": "",
		"onGridPowerSlope": 0,
		"operatedMode": 0,
		"overFrequencyStage1TripTime": "",
		"overFrequencyStage1TripValue": "",
		"overFrequencyStage2TripTime": "",
		"overFrequencyStage2TripValue": "",
		"overLoadProtectionResetEnable": 0,
		"overVoltage10mTriggerValue": "",
		"overVoltageStage1TripTime": "",
		"overVoltageStage1TripValue": "",
		"overVoltageStage2TripTime": "",
		"overVoltageStage2TripValue": "",
		"pfPowerCurveFunctionEnable": 0,
		"pfPowerCurveLockinVoltage": "",
		"pfPowerCurveLockoutPower": "",
		"pfPowerCurveLockoutVoltage": "",
		"pfPowerCurvePointAPower": "",
		"pfPowerCurvePointAPowerFactor": "",
		"pfPowerCurvePointBPower": "",
		"pfPowerCurvePointBPowerFactor": "",
		"pfPowerCurvePointCPower": "",
		"pfPowerCurvePointCPowerFactor": "",
		"powerFactor": "",
		"puCurveFunctionEnable": 0,
		"puCurvePointAActivePower": "",
		"puCurvePointAVoltage": "",
		"puCurvePointBActivePower": "",
		"puCurvePointBVoltage": "",
		"puCurvePointCActivePower": "",
		"puCurvePointCVoltage": "",
		"puCurvePointDActivePower": "",
		"puCurvePointDVoltage": "",
		"pvParallelSetting": 0,
		"quCurveFunctionEnable": 0,
		"quCurveLockInPower": "",
		"quCurveLockOutPower": "",
		"quCurvePointAReactivePower": "",
		"quCurvePointAVoltage": "",
		"quCurvePointBReactivePower": "",
		"quCurvePointBVoltage": "",
		"quCurvePointCReactivePower": "",
		"quCurvePointCVoltage": "",
		"quCurvePointDReactivePower": "",
		"quCurvePointDVoltage": "",
		"remoteOnOffEnable": 0,
		"remoteOutputOnOffControl": 0,
		"underFrequencyStage1TripTime": "",
		"underFrequencyStage1TripValue": "",
		"underFrequencyStage2TripTime": "",
		"underFrequencyStage2TripValue": "",
		"underVoltageStage1TripTime": "",
		"underVoltageStage1TripValue": "",
		"underVoltageStage2TripTime": "",
		"underVoltageStage2TripValue": "",
		"zeroExportAdjustmentPower": 0,
		"zeroExportFunction": 0
	}
}
```

| Parameter Name | Example Value | Parameter Type | Description |
| --- | --- | ---- | ---- |
| code | - | integer | code |
| message | - | string | message |
| data.acOutputRatedFrequency | - | integer | AC Output Rated Frequency，0：50Hz, 1：60Hz |
| data.acOutputRatedVoltage | - | number | AC Output Rated Voltage，Cannot be set |
| data.antiIslandingDetectionEnable | - | integer | Anti-Islanding Detection，0：Disable， 1：Enable |
| data.batteryChargedVoltage | - | number | Battery Charged Voltage，It is related to the "Battery Model",Each Model The range of values is 48~60V |
| data.batteryFloatingChargedVoltage | - | number | Battery Floating Charged Voltage，It is related to the "Battery Model",Each Model The range of values is 48~60V |
| data.batteryMaxChargedCurrent | - | number | Battery Max Charged Current，The range of values is 1~200A |
| data.batteryMaxDischargeCurrent | - | number | Battery Max Discharge Current，The range of values is 5~200A |
| data.batteryModel | - | integer | Battery Model，0：User defined，1：Lithium battery(default)，2：FelicitySolar(LPBF series)，3：FelicitySolar(LPBA series) |
| data.batteryModules | - | integer | Battery Modules，It is related to the "Battery Model", and can be set when the battery type is "User defined" |
| data.batteryOffGridDischargeDepthSoc | - | integer | Battery Off Grid Discharge Depth Soc，The range of values is 0~100% |
| data.batteryOffGridRecoveryDepthSoc | - | integer | Battery Off Grid Recovery Depth Soc，The range of values is 0~100% |
| data.batteryOnGridDischargeDepthSoc | - | integer | Battery On Grid Discharge DepthSoc，The range of values is 10~100% |
| data.buzzerEnable | - | integer | Buzzer Enable，0：Disable， 1：Enable |
| data.commOffLineEnable | - | integer | Comm Off Line Enable，0：Disable， 1：Enable |
| data.deratingByVoltageEnable | - | integer | 110%u Derating By Voltage Enable |
| data.deviceSn | - | string | Device serial number |
| data.ecoRule1.daysOfEffectiveWeek.0 | - | array | ECO Mode Rule 1，Days Of Effective Week,Valuable：MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY，Multiple Choice |
| data.ecoRule1.power | - | integer | ECO Mode Rule 1，Battery charging or discharging power,Unit：W，The range of values is 0~ inverter rated power |
| data.ecoRule1.ruleMode | - | integer | ECO Mode Rule 1，0：disable, 1: enable charge 2: enable discharge |
| data.ecoRule1.soc | - | integer | ECO Mode Rule 1，Battery charging or discharging soc，Unit：%，The range of values is 0~100% |
| data.ecoRule1.startDay | - | string | ECO Mode Rule 1，Starting date, Format: mm:dd |
| data.ecoRule1.startTime | - | string | ECO Mode Rule 1，Starting time, Format: HH:ss |
| data.ecoRule1.stopDay | - | string | ECO Mode Rule 1，Stop date, Format: mm:dd |
| data.ecoRule1.stopTime | - | string | ECO Mode Rule 1，Stop time, Format: HH:ss |
| data.ecoRule1.voltage | - | number | ECO Mode Rule 1，Battery charging or discharging voltage，Unit：V，It is related to the "Battery Model",Each Model The range of values is 48~60V |
| data.ecoRule1 | - | object | Economic Model Rule 1 Object |
| data.ecoRule2.daysOfEffectiveWeek.0 | - | array | ECO Mode Rule 2，Days Of Effective Week,Valuable：MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY，Multiple Choice |
| data.ecoRule2.power | - | integer | ECO Mode Rule 2，Battery charging or discharging power,Unit：W，The range of values is 0~ inverter rated power |
| data.ecoRule2.ruleMode | - | integer | ECO Mode Rule 2，0：disable, 1: enable charge 2: enable discharge |
| data.ecoRule2.soc | - | integer | ECO Mode Rule 2，Battery charging or discharging soc，Unit：%，The range of values is 0~100% |
| data.ecoRule2.startDay | - | string | ECO Mode Rule 2，Starting date, Format: mm:dd |
| data.ecoRule2.startTime | - | string | ECO Mode Rule 2，Starting time, Format: HH:ss |
| data.ecoRule2.stopDay | - | string | ECO Mode Rule 2，Stop date, Format: mm:dd |
| data.ecoRule2.stopTime | - | string | ECO Mode Rule 2，Stop time, Format: HH:ss |
| data.ecoRule2.voltage | - | number | ECO Mode Rule 2，Battery charging or discharging voltage，Unit：V，It is related to the "Battery Model",Each Model The range of values is 48~60V |
| data.ecoRule2 | - | object | Economic Model Rule 2 Object |
| data.ecoRule3.daysOfEffectiveWeek.0 | - | array | ECO Mode Rule 3，Days Of Effective Week,Valuable：MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY，Multiple Choice |
| data.ecoRule3.power | - | integer | ECO Mode Rule 3，Battery charging or discharging power,Unit：W，The range of values is 0~inverter rated power |
| data.ecoRule3.ruleMode | - | integer | ECO Mode Rule 3，0：disable, 1: enable charge 2: enable discharge |
| data.ecoRule3.soc | - | integer | ECO Mode Rule 3，Battery charging or discharging soc，Unit：%，The range of values is 0~100% |
| data.ecoRule3.startDay | - | string | ECO Mode Rule 3，Starting date, Format: mm:dd |
| data.ecoRule3.startTime | - | string | ECO Mode Rule 3，Starting time, Format: HH:ss |
| data.ecoRule3.stopDay | - | string | ECO Mode Rule 3，Stop date, Format: mm:dd |
| data.ecoRule3.stopTime | - | string | ECO Mode Rule 3，Stop time, Format: HH:ss |
| data.ecoRule3.voltage | - | number | ECO Mode Rule 3，Battery charging or discharging voltage，Unit：V，It is related to the "Battery Model",Each Model The range of values is 48~60V |
| data.ecoRule3 | - | object | Economic Model Rule 3 Object |
| data.ecoRule4.daysOfEffectiveWeek.0 | - | array | ECO Mode Rule 4，Days Of Effective Week,Valuable：MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY，Multiple Choice |
| data.ecoRule4.power | - | integer | ECO Mode Rule 4，Battery charging or discharging power,Unit：W，The range of values is 0~inverter rated power |
| data.ecoRule4.ruleMode | - | integer | ECO Mode Rule 4，0：disable, 1: enable charge 2: enable discharge |
| data.ecoRule4.soc | - | integer | ECO Mode Rule 4，Battery charging or discharging soc，Unit：%，The range of values is 0~100% |
| data.ecoRule4.startDay | - | string | ECO Mode Rule 4，Starting date, Format: mm:dd |
| data.ecoRule4.startTime | - | string | ECO Mode Rule 4，Starting time, Format: HH:ss |
| data.ecoRule4.stopDay | - | string | ECO Mode Rule 4，Stop date, Format: mm:dd |
| data.ecoRule4.stopTime | - | string | ECO Mode Rule 4，Stop time, Format: HH:ss |
| data.ecoRule4.voltage | - | number | ECO Mode Rule 4，Battery charging or discharging voltage，Unit：V，It is related to the "Battery Model",Each Model The range of values is 48~60V |
| data.ecoRule4 | - | object | Economic Mode Rule 4 Object |
| data.eventLogFunctionEnable | - | integer | Event Log Function，Cannot be set |
| data.faultLogFunctionEnable | - | integer | Fault Log Function，Cannot be set |
| data.fixQPencent | - | number | FixQ Pencent, unit：% |
| data.fpChargeCurveFunctionEnable | - | integer | Frequency-PoweryCharge Curve Function，0：Disable， 1：Enable |
| data.fpCurveFunctionEnable | - | integer | Frequency-Power Curve Function，0：Disable， 1：Enable |
| data.fpCurveOverFrequencyLowerLimit | - | number | Over Frequency Start Point |
| data.fpOverFrequencyPowerSlope | - | number | Over Frequency Power Slope |
| data.fpOverFrequencyUpperLimit | - | number | Over Frequency End Point |
| data.fpRecoveryPowerSlope | - | number | Recovery Power Slope |
| data.fpRestoreFrequencyLowerLimit | - | number | F(Stop) Lower |
| data.fpRestoreFrequencyPowerSlope | - | integer | Reconnection Power Slope |
| data.fpRestoreFrequencyUperLimit | - | number | F(Stop) Upper |
| data.fpRestoreFrequencyWaitingTime | - | integer | Restore Waiting Time |
| data.fpUnderFrequencyLowerLimit | - | number | Under Frequency Start Point |
| data.fpUnderFrequencyPowerSlope | - | number | Under Frequency Power Slope |
| data.fpUnderFrequencyPowerSlopeForCharge | - | number | Under Frequency Power Slope For Charge |
| data.fpUnderFrequencyUpperLimit | - | number | Under Frequency End Point |
| data.gridPowerUnbalanceEnable | - | integer | Grid Power Unbalance |
| data.gridStandardCode | - | integer | Standard |
| data.gridWaveformDetectionMode | - | integer | Detection Mode |
| data.highVoltageCrossingTripThreshold | - | number | High Voltage Limit Of Ride Through |
| data.highVoltageEndPointTripTime | - | number | End Point Of Protection Time |
| data.highVoltageEndPointTripValue | - | number | End Point Of Ride Through |
| data.highVoltageRideThroughFunctionEnable | - | integer | High Voltage Ride Through Function |
| data.highVoltageStartPointTripTime | - | number | Start Point Of Protection Time |
| data.highVoltageStartPointTripValue | - | number | Start Point Of Ride Through |
| data.isoDetectionEnable | - | integer | ISO Detection |
| data.lcdBacklightEnable | - | integer | LCD Backlight, 0：Disable， 1：Enable |
| data.lowVoltageCrossingTripThreshold | - | number | Low Voltage Limit Of Ride Through |
| data.lowVoltageEndPointTripTime | - | number | End Point Of Protection Time |
| data.lowVoltageEndPointTripValue | - | number | End Point Of Ride Through |
| data.lowVoltageRideThroughFunctionEnable | - | integer | Low Voltage Ride Through |
| data.lowVoltageStartPointTripTime | - | number | Start Point Of Protection Time |
| data.lowVoltageStartPointTripValue | - | number | Start Point Of Ride Through |
| data.noBmsOffGridBatteryCutOffVoltage | - | number | Battery Cut-Off Voltage(Off-Grid, No Bms) |
| data.noBmsOffGridBatteryRestartVoltage | - | number | Battery Restart Voltage(Off-Grid, No Bms) |
| data.noBmsOnGridBatteryCutOffVoltage | - | number | Battery Cut-Off Voltage(On-Grid, No Bms) |
| data.onGridObservationTime | - | integer | Observation Time |
| data.onGridPowerLimit | - | number | Grid Power Limit |
| data.onGridPowerSlope | - | integer | Grid Power Slope |
| data.operatedMode | - | integer | Operated Mode, 0:General Mode, 1:Backup Mode, 2:Eco Mode |
| data.overFrequencyStage1TripTime | - | number | OF Stage1 Trip Time |
| data.overFrequencyStage1TripValue | - | number | OF Stage1 Trip Value |
| data.overFrequencyStage2TripTime | - | number | OF Stage2 Trip Time |
| data.overFrequencyStage2TripValue | - | number | OF Stage2 Trip Value |
| data.overLoadProtectionResetEnable | - | integer | Over Load Protection Reset, 0：Disable， 1：Enable |
| data.overVoltage10mTriggerValue | - | number | OV 10Min Mean Value |
| data.overVoltageStage1TripTime | - | number | OV Stage1 Trip Time |
| data.overVoltageStage1TripValue | - | number | OV Stage1 Trip Value |
| data.overVoltageStage2TripTime | - | number | OV Stage2 Trip Time |
| data.overVoltageStage2TripValue | - | number | OV Stage2 Trip Value |
| data.pfPowerCurveFunctionEnable | - | integer | PF-Power Curve Function |
| data.pfPowerCurveLockinVoltage | - | number | Lockin Voltage |
| data.pfPowerCurveLockoutPower | - | number | Lockout Power |
| data.pfPowerCurveLockoutVoltage | - | number | Lockout Voltage |
| data.pfPowerCurvePointAPower | - | number | Point A Power |
| data.pfPowerCurvePointAPowerFactor | - | number | Point A Power Factor |
| data.pfPowerCurvePointBPower | - | number | Point B Power |
| data.pfPowerCurvePointBPowerFactor | - | number | Point B Power Factor |
| data.pfPowerCurvePointCPower | - | number | Point C Power |
| data.pfPowerCurvePointCPowerFactor | - | number | Point C Power Factor |
| data.powerFactor | - | number | Power Factor |
| data.puCurveFunctionEnable | - | integer | P(U) Curve Function |
| data.puCurvePointAActivePower | - | number | Point A Active Power |
| data.puCurvePointAVoltage | - | number | Point A Voltage |
| data.puCurvePointBActivePower | - | number | Point B Active Power |
| data.puCurvePointBVoltage | - | number | Point B Voltage |
| data.puCurvePointCActivePower | - | number | Point C Active Power |
| data.puCurvePointCVoltage | - | number | Point C Voltage |
| data.puCurvePointDActivePower | - | number | Point D Active Power |
| data.puCurvePointDVoltage | - | number | Point D Voltage |
| data.pvParallelSetting | - | integer | PV Parallel Set |
| data.quCurveFunctionEnable | - | integer | Q(U) Curve Function |
| data.quCurveLockInPower | - | number | Lock In Power |
| data.quCurveLockOutPower | - | number | Lock Out Power |
| data.quCurvePointAReactivePower | - | number | Point A Reactive Power |
| data.quCurvePointAVoltage | - | number | Point A Voltage |
| data.quCurvePointBReactivePower | - | number | Point B Reactive Power |
| data.quCurvePointBVoltage | - | number | Point B Voltage |
| data.quCurvePointCReactivePower | - | number | Point C Reactive Power |
| data.quCurvePointCVoltage | - | number | Point C Voltage |
| data.quCurvePointDReactivePower | - | number | Point D Reactive Power |
| data.quCurvePointDVoltage | - | number | Point D Voltage |
| data.remoteOnOffEnable | - | integer | Remote ON/OFF, 0：Disable， 1：Enable |
| data.remoteOutputOnOffControl | - | integer | AC Output ON/OFF, 0：off, 1: on |
| data.underFrequencyStage1TripTime | - | number | UF Stage1 Trip Time |
| data.underFrequencyStage1TripValue | - | number | UF Stage1 Trip Value |
| data.underFrequencyStage2TripTime | - | number | UF Stage2 Trip Time |
| data.underFrequencyStage2TripValue | - | number | UF Stage2 Trip Value |
| data.underVoltageStage1TripTime | - | number | UV Stage1 Trip Time |
| data.underVoltageStage1TripValue | - | number | UV Stage1 Trip Value |
| data.underVoltageStage2TripTime | - | number | UV Stage2 Trip Time |
| data.underVoltageStage2TripValue | - | number | UV Stage2 Trip Value |
| data.zeroExportAdjustmentPower | - | integer | Zero Export Power |
| data.zeroExportFunction | - | integer | Zero Export Mode，1: To load, 2: To CT |
| data | - | object | - |
| content.ecoRule5 | - | object | Economic Mode Rule 5 Object, refer to content.ecoRule (Economic Mode Rule 1 Object) |
| content.ecoRule6 | - | object | Economic Mode Rule 6 Object, refer to content.ecoRule (Economic Mode Rule 1 Object) |
| content.ecoRule7 | - | object | Economic Mode Rule 7 Object, refer to content.ecoRule (Economic Mode Rule 1 Object) |
| content.ecoRule8 | - | object | Economic Mode Rule 8 Object, refer to content.ecoRule (Economic Mode Rule 1 Object) |
| content.ecoRule9 | - | object | Economic Mode Rule 9 Object, refer to content.ecoRule (Economic Mode Rule 1 Object) |
| content.ecoRule10 | - | object | Economic Mode Rule 10 Object, refer to content.ecoRule (Economic Mode Rule 1 Object) |

* token expire(200)

```javascript
{
  "code": 998,
  "message": "The token has expired, please log in again",
  "data": {}
}
```

* Permission Denied(200)

```javascript
{
  "code": 2001528,
  "message": "Insufficient permissions",
  "data": "Insufficient permissions"
}
```

**Request Header Parameters**

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| Content-Type | application/x-www-form-urlencoded | string | Yes | - |
| Authorization | Bearer_eyJhbGciOiJIUzI1NiJ9.eyJkZW1vVXNlciI6ZmFsc2UsInN1YiI6IueuoeeQhuWRmCIsImF1ZCI6Ik56TTNORFF4TkRrd01UVTFPREUwTkE9PSIsIm5iZiI6MTcxMTY3NjY4NiwiaXNzIjoiRkxTLVNPTEFSLVNFUlZFUiIsImlkIjo3Mzc0NDE0OTAxNTU4MTQ0LCJleHAiOjE3MTQyNjg2ODYsImlhdCI6MTcxMTY3NjY4Nn0._l5VIYevtyv2Xc66S9w6fqmkECBFvLZPJYqjU07pObE | string | Yes | User token, which can be obtained from authentication and refreshing tokens. |
| Lang | en_US | string | Yes | Language, currently supports English en_US. |

**Query**

## Query Remote Control Setting Attachment

> Created by: Timesup

> Updated by: Timesup

> Created at: 2024-08-16 09:52:31

> Updated at: 2025-03-14 08:58:38

### T-REX

**for T-REX-15KLP1G01、T-REX-8KLP1G01、T-REX-50KHP3G01, the request parameters as follows：**

| Key | Name | Range | unit | Required | Type | Description |
| --- | ---- | ----- | ---- | -------- | ---- | ----------- |
| batteryMode | Bat Mode | 0:Lithium1:Use Batt V  2:No bat |  | No | Number |  |
| batteryCapacity | Bat Capacity | 0~500 | AH | No | Number |  |
| batteryMaxChargedCurrent | Max A Charge | 0~55 | A | No | Number | Max battery charg current. Parallel bat1&bat2:if the inverter battery wiring ports are connect to one battery bank, please enable this function. |
| batteryMaxDischargeCurrent | Max A Discharge | 0~55 | A | No | Number | Max battery discharge current. Parallel bat1&bat2:if the inverter battery wiring ports are connect to one battery bank, please enable this function. |
| batteryParallelEnable | Parallel bat1&bat2 | 0:Stand Alone 1:Parallel |  | No | Number | Parallel bat1&bat2:if the inverter battery wiring ports are connect to one battery bank, please enable this function. |
| genAutoStartChargeSoc | GEN Auto Start Charge | 0~100 | % | No | Number | generator Auto Start Charge Soc |
| genAutoExitChargeSoc | GEN Exit Charge | 5~100 | % | No | Number | generator Auto Exit Charge Soc |
| gridChargeCurrent | Grid Charge Current | 0~55 | A | No | Number | grid Charge Current |
| genChargeCurrent | GEN Charge Current | 0~55 | A | No | Number | generator Charge Current |
| genStartSignalEnable | GEN Start Signal | 0:Disable  1:Enable |  | No | Number | generator Start Signal Enable,0: Disable, 1: Enable |
| genChargeEnable | Grid Charge Enable | 0:Disable  1:Enable |  | No | Number | It's allowed to use power fed from the grid port, which includes grid or generator connected to the grid port, to charge the battery. |
| gridChargeEnable | GEN Charge Enable | 0:Disable  1:Enable |  | No | Number | Use the power of generator to charge the battery. |
| gridAutoStartChargeVoltage | Grid Auto Start Charge Voltage | 150~800 | V | No | Number |  |
| gridAutoExitChargeVoltage | Grid Exit Charge Voltage | 150~800 | V | No | Number |  |
| genAutoStartChargeVoltage | GEN Auto Start Charge Voltage | 150~800 | V | No | Number | generator Auto Start Charge Voltage |
| genAutoExitChargeVoltage | GEN Exit Charge Voltage | 150~800 | V | No | Number | generator Auto Exit Charge Voltage |
| genMaxRunTime | GEN Max Run Time | 0~24 | hours | No | Number | generator Max Run Time |
| lithiumProtocol | Lithium Protocol | 0~20 |  | No | Number |  |
| batteryFloatingChargedVoltage | Bat float voltage | 150~800 | V | No | Number | Battery full charge voltage. |
| batteryRestartOutputVoltage | Bat Restart | 150~800 | V | No | Number | battery Restart Output Voltage |
| batteryLowVoltageAlarmVoltage | Bat Low Alarm | 150~800 | V | No | Number | battery Low Voltage Alarm Voltage |
| batteryShutdownVoltage | Bat Shutdown | 150~800 | V | No | Number | battery Shutdown Voltage |
| batteryRestartOutputSoc | Bat Restart | 0~100 | % | No | Number | battery Restart Output Soc |
| batteryLowVoltageAlarmSoc | Bat Low Alarm SOC | 0~100 | % | No | Number | battery Low Voltage Alarm Soc |
| batteryShutdownSoc | Bat Shutdown SOC | 0~100 | % | No | Number | battery Shutdown Soc |
| operatedMode | System Mode | 0:Selling Mode   1:Zero Export To Load   2:Zero Export To CT   3:Scheduling Mode |  | No | Number | Selling First: This Mode allows hybrid inverter to sell back any excess power produced by the solar panels to the grid. If Time Of Use is active, the battery energy also can be sold into grid.  The PV energy will be used to power the load and charge the battery and then excess energy will flow to grid.  Power source priority for the load is as follows:  1. Solar Panels.  2. Grid. when Energy Pattern tick Batt First.  Battery (until programable SOC discharge is reached). when Energy Pattern tick Load First and disable Grid charge.  Zero Export To Load: Hybrid inverter will only provide power to the backup load connected. The hybrid inverter will neither provide power to the home load nor sell power to grid. The built-in CT will detect power flowing back to the grid and will reduce the power of the inverter only to supply the backup load and charge the battery.  Zero Export To CT: Hybrid inverter will not only provide power to the backup load connected but also give power to the home load connected. If PV power and battery power is insufficient, it will take grid energy as supplement. The hybrid inverter will not sell power to grid. In this mode, a CT is needed. Please refer to manual CT connection for the installation method of CT. The external CT will detect power flowing back to the grid and will reduce the power of the inverter only to supply the backup load, charge battery and home load.  Scheduling mode: Based on system requirements and operating conditions, adjust the working status of the inverter and its coordinated operation with other devices through power allocation. Scheduling mode: Based on system requirements and operating conditions, adjust the working status of the inverter and its coordinated operation with other devices through power allocation" |
| zeroExportToLoadEnable | Solar Sell(to Load) | 0:Disable   1:Enable |  | No | Number | “Solar sell” is supplement for Zero Export To Load or Zero Export To CT: when this item is active, the surplus PV energy can be sold back to grid too. When it is active, PV Power source priority usage is as follows: load consumption and charge battery and feed into grid. |
| zeroExportToCtEnable | Solar Sell(to CT) | 0:Disable   1:Enable" |  | No | Number | “Solar sell” is supplement for Zero Export To Load or Zero Export To CT: when this item is active, the surplus PV energy can be sold back to grid too. When it is active, PV Power source priority usage is as follows: load consumption and charge battery and feed into grid. |
| dispatchActivePowerGiven | Active Power | -55~55 | KW | No | Number | "The charge power(Active Power greater than 0) or discharge power(Active Power less than 0) in the Scheduling mode.Reactive power can be set at Gird Setting/Connect" |
| maxSellingPower | Max. Sell power | 0~550 | KW | No | Number | max Selling Power |
| zeroExportHysteresisPower | Zero-export Power | -5000~5000 | W | No | Number | "For Zero Export To Load or Zero Export To CT, and the “Solar sell” is not active.   It tells the grid output power threshold to ensure the hybrid inverter won' t feed power to grid." |
| energyPriority | Energy Priority | 0:Bat First   1:Load First |  | No | Number | "Energy Pattern:Priority of PV power usage.   Batt First: PV power is firstly used to charge the battery and then used to power the load. If PV power is insufficient, grid will make supplement for battery and load simultaneously.  Load First: PV power is firstly used to power the load and then used to charge the battery. If PV power is insufficient, Grid will provide power to load, but neither the battery power to load nor the Grid charge to battery." |
| gridPeakShavingEnable | Grid Peak Shaving Enable | 0:Disable   1:Enable |  | No | Number | "Grid Peak Shaving:  1. To use Peak-Shaving on a generator, the equipment MUST be connected to the “GRID” terminal of the inverter.  2. Peak-Shaving helps reduce grid consumption during peak demand by utilizing battery backup power. It can also be used to prevent generator overload above a specified power threshold.  3. Install the CT sensors on grid / generator lines L1, L2. The arrows on the CTs MUST point toward  the GRID.  4. The T-REX INVERTER supplies power from the batteries whenever the “Power” threshold is met.  5. This mode will automatically adjust the ""Grid Charge” amperage (A) to avoid generator overloads during battery charging.  6. Grid Peak-Shaving will automatically enable “Time of Use” and MUST be configured." |
| gridPeakShavingPower | Grid Peak Shaving Power | 0~550 | KW | No | Number | grid Peak Shaving Power |
| timeOfUseEnable | Time Of Use | 0:Disable   1:Enable |  | No | Number | "Time Of Use: it is used to program when to use grid or generator to charge the battery, and when to discharge the battery to power the load. Only tick ""Time Of Use"" then the follow items (Grid, charge, time, power etc.) will take effect.  Note: when tick Selling First and click Time Of Use, the battery power can be sold into grid.   Charge Source: select grid or generator to charge the battery." |
| ecoRule1.gridChangingEnable | Grid Changing | 0:Disable  1:Enable |  | No | Number | Grid Changing1: Time Of Use Rule 1, grid Changing Enable, 0: Disable, 1: Enable |
| ecoRule1.genChangingEnable | Gen Changing | 0:Disable  1:Enable |  | No | Number | Gen Changing1: Time Of Use Rule 1, gen Changing Enable, 0: Disable, 1: Enable |
| ecoRule1.startTime | Start Time | HH:023  mm:059 |  | No | String | Start Time1: Time Of Use Rule 1, Starting time, Format: HH:mm |
| ecoRule1.stopTime | End Time | HH:023  mm:059 |  | No | String | End Time1: Time Of Use Rule 1, Stop time, Format: HH:mm |
| ecoRule1.voltage | Target Voltage | 150~750 | V | No | Number | Target Voltage 1: Time Of Use Rule 1，Battery charging or discharging voltage，Unit：V，It is related to the "Battery Model",Each Model The range of values is 48~60V |
| ecoRule1.soc | Target SOC | 0~100 | % | No | Number | Target SOC 1: Time Of Use Rule 1，Battery charging or discharging soc，Unit：%，The range of values is 0~100% |
| ecoRule1.power | INV Power | 0~50 | KW | No | Number | INV Power 1: Time Of Use Rule 1，Battery charging or discharging power,Unit：kW，The range of values is 0~ inverter rated power |
| ecoRule2.gridChangingEnable | Grid Changing | 0:Disable  1:Enable |  | No | Number | Grid Changing2: Time Of Use Rule 2, grid Changing Enable, 0: Disable, 1: Enable |
| ecoRule2.genChangingEnable | Gen Changing | 0:Disable   1:Enable |  | No | Number | Gen Changing2: Time Of Use Rule 2, gen Changing Enable, 0: Disable, 1: Enable |
| ecoRule2.startTime | Start Time | HH:023  mm:059 |  | No | String | Start Time2: Time Of Use Rule 2, Starting time, Format: HH:mm |
| ecoRule2.stopTime | End Time | HH:023  mm:059 |  | No | String | End Time2: Time Of Use Rule 2, Stop time, Format: HH:mm |
| ecoRule2.voltage | Target Voltage | 150~750 | V | No | Number | Target Voltage 2: Time Of Use Rule 2，Battery charging or discharging voltage，Unit：V，It is related to the "Battery Model",Each Model The range of values is 48~60V |
| ecoRule2.soc | Target SOC | 0~100 | % | No | Number | Target SOC 2: Time Of Use Rule 2，Battery charging or discharging soc，Unit：%，The range of values is 0~100% |
| ecoRule2.power | INV Power | 0~50 | KW | No | Number | INV Power 2: Time Of Use Rule 2，Battery charging or discharging power,Unit：kW，The range of values is 0~ inverter rated power |
| ecoRule3.gridChangingEnable | Grid Changing | 0:Disable   1:Enable |  | No | Number | Grid Changing3: Time Of Use Rule 3, grid Changing Enable, 0: Disable, 1: Enable |
| ecoRule3.genChangingEnable | Gen Changing | 0:Disable1:Enable |  | No | Number | Gen Changing3: Time Of Use Rule 3, gen Changing Enable, 0: Disable, 1: Enable |
| ecoRule3.startTime | Start Time | HH:023mm:059 |  | No | String | Start Time3: Time Of Use Rule 3, Starting time, Format: HH:mm |
| ecoRule3.stopTime | End Time | HH:023mm:059 |  | No | String | End Time3: Time Of Use Rule 3, Stop time, Format: HH:mm |
| ecoRule3.voltage | Target Voltage | 150~750 | V | No | Number | Target Voltage 3: Time Of Use Rule 3，Battery charging or discharging voltage，Unit：V，It is related to the "Battery Model",Each Model The range of values is 48~60V |
| ecoRule3.soc | Target SOC | 0~100 | % | No | Number | Target SOC 3: Time Of Use Rule 3，Battery charging or discharging soc，Unit：%，The range of values is 0~100% |
| ecoRule3.power | INV Power | 0~50 | KW | No | Number | INV Power 3: Time Of Use Rule 3，Battery charging or discharging power,Unit：kW，The range of values is 0~ inverter rated power |
| ecoRule4.gridChangingEnable | Grid Changing | 0:Disable1:Enable |  | No | Number | Grid Changing4: Time Of Use Rule 4, grid Changing Enable, 0: Disable, 1: Enable |
| ecoRule4.genChangingEnable | Gen Changing | 0:Disable1:Enable |  | No | Number | Gen Changing4: Time Of Use Rule 4, gen Changing Enable, 0: Disable, 1: Enable |
| ecoRule4.startTime | Start Time | HH:023mm:059 |  | No | String | Start Time4: Time Of Use Rule 4, Starting time, Format: HH:mm |
| ecoRule4.stopTime | End Time | HH:023mm:059 |  | No | String | End Time4: Time Of Use Rule 4, Stop time, Format: HH:mm |
| ecoRule4.voltage | Target Voltage | 150~750 | V | No | Number | Target Voltage 4: Time Of Use Rule 4，Battery charging or discharging voltage，Unit：V，It is related to the "Battery Model",Each Model The range of values is 48~60V |
| ecoRule4.soc | Target SOC | 0~100 | % | No | Number | Target SOC 4: Time Of Use Rule 4，Battery charging or discharging soc，Unit：%，The range of values is 0~100% |
| ecoRule4.power | INV Power | 0~50 | KW | No | Number | INV Power 4: Time Of Use Rule 4，Battery charging or discharging power,Unit：kW，The range of values is 0~ inverter rated power |
| ecoRule5.gridChangingEnable | Grid Changing | 0:Disable1:Enable |  | No | Number | Grid Changing5: Time Of Use Rule 5, grid Changing Enable, 0: Disable, 1: Enable |
| ecoRule5.genChangingEnable | Gen Changing | 0:Disable 1:Enable |  | No | Number | Gen Changing5: Time Of Use Rule 5, gen Changing Enable, 0: Disable, 1: Enable |
| ecoRule5.startTime | Start Time | HH:023 mm:059 |  | No | String | Start Time5: Time Of Use Rule 5, Starting time, Format: HH:mm |
| ecoRule5.stopTime | End Time | HH:023 mm:059 |  | No | String | End Time5: Time Of Use Rule 5, Stop time, Format: HH:mm |
| ecoRule5.voltage | Target Voltage | 150~750 | V | No | Number | Target Voltage 5: Time Of Use Rule 5，Battery charging or discharging voltage，Unit：V，It is related to the "Battery Model",Each Model The range of values is 48~60V |
| ecoRule5.soc | Target SOC | 0~100 | % | No | Number | Target SOC 5: Time Of Use Rule 5，Battery charging or discharging soc，Unit：%，The range of values is 0~100% |
| ecoRule5.power | INV Power | 0~50 | KW | No | Number | INV Power 5: Time Of Use Rule 5，Battery charging or discharging power,Unit：kW，The range of values is 0~ inverter rated power |
| ecoRule6.gridChangingEnable | Grid Changing | 0:Disable1:Enable |  | No | Number | Grid Changing6: Time Of Use Rule 6, grid Changing Enable, 0: Disable, 1: Enable |
| ecoRule6.genChangingEnable | Gen Changing | 0:Disable1:Enable |  | No | Number | Gen Changing6: Time Of Use Rule 6, gen Changing Enable, 0: Disable, 1: Enable |
| ecoRule6.startTime | Start Time | HH:023mm:059 |  | No | String | Start Time6: Time Of Use Rule 6, Starting time, Format: HH:mm |
| ecoRule6.stopTime | End Time | HH:023mm:059 |  | No | String | End Time6: Time Of Use Rule 6, Stop time, Format: HH:mm |
| ecoRule6.voltage | Target Voltage | 150~750 | V | No | Number | Target Voltage 6: Time Of Use Rule 6，Battery charging or discharging voltage，Unit：V，It is related to the "Battery Model",Each Model The range of values is 48~60V |
| ecoRule6.soc | Target SOC | 0~100 | % | No | Number | Target SOC 6: Time Of Use Rule 6，Battery charging or discharging soc，Unit：%，The range of values is 0~100% |
| ecoRule6.power | INV Power | 0~50 | KW | No | Number | INV Power 6: Time Of Use Rule 6，Battery charging or discharging power,Unit：kW，The range of values is 0~ inverter rated power |
| touEffectiveWeek | Week Of Use | MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY |  | No | Array | Week Of Use: Time Of Use Effective Week,Valuable：MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY，Multiple Choice |
| gridStandardCode | Standard | 0: Germany_VDE4105,2: General_Standard_50Hz,3: General_Standard_60Hz,4: Italy_CEI_021_2019,5: Britain_G99,6: Australia_A,7: NewZealand_AS4777,8: SouthAfrican_NRS097,9: Netherland_EN 50549-1,10: Brazil,11: EN50549,12: Poland_NC_RFG,13: Czech_CSN 50549-1,14: Austria_R25:2020-03,15: Austria_OVE-directive_R25,16: Spain_NTS_2021,17: Spain_UNE217001,18: cNetherland" |  | No | Number | State Grid regulations and standards, please set according to the power grid standards in your region |
| acOutputRatedVoltage | AC Output Rated Voltage | 380:380V400:400V | V | No | Number |  |
| acOutputRatedFrequency | AC Output Rated Frequency | 50:50Hz60:60Hz | HZ | No | Number |  |
| turnOnRampRate | Turn On Ramp Rate | 1~500 | %/S | No | Number | "It is the startup and reconnection power ramp, for example, Turn On Ramp Rate =100%/s, means the output power will increase from 0 to 100% rated power in 1s.Running P Ramp Rate: It is the power ramp response to the active power reference in normal running." |
| turnOffRampRate | Reconnection High Voltage | 1~500 | %/S | No | Number |  |
| runningActivePowerRampRate | Running P Ramp Rate | 1~500 | %/S | No | Number | It is the power ramp response to the active power reference in normal running |
| runningReactivePowerRampRate | Running Q Ramp Rate | 1~500 | %/S | No | Number |  |
| gridConnectionWaitTime | Reconnection Time | 1~600 | S | No | Number | The waiting time for the inverter connects the grid again after tripping. |
| reactivePowerControlMode | Q Mode | 0:Disable1:Const PF2:Const Q |  | No | Number | "Inverter response to the reactive power mode.Disable: not responding to the reactive power mode. Const PF: Inverter output a setting power factor(cos φ)value.Const Q: Inverter output a setting reactive power value." |
| reactivePowerGiven | Const Q | -7500~7500 | VA | No | Number | Setting the reactive power value. Const Q >0 means Inverter output capacitive reactive power, Const Q <0 means Inverter output Inductive reactive power. |
| powerFactorGiven | Const PF | -1-0.8,0.81 |  | No | Number | Setting the power factor(cos φ)value. Const PF>0 means Inverter output Inductive reactive power(or inverter will absorb capacitive reactive power from the power grid),Const PF<0 means Inverter output capacitive reactive power. |
| gridOverVoltageVoltage1 | High Voltage 1 | 105~150 | % | No | Number | Level 1 overvoltage protection point. |
| gridOverVoltageTime1 | HV1 Time | 0~655.35 | S | No | Number | Level 1 overvoltage protection time. |
| gridOverVoltageVoltage2 | HV2 | 105~150 | % | No | Number | Level 2 overvoltage protection point. |
| gridOverVoltageTime2 | HV2 Time | 0~655.35 | S | No | Number | Level 2 overvoltage protection time. |
| gridOverVoltageVoltage3 | HV3 | 105~150 | % | No | Number | Level 3 overvoltage protection point. |
| gridUnderVoltageVoltage1 | Low Voltage 1 | 5~95 | % | No | Number | Level 1 undervoltage protection point. |
| gridUnderVoltageTime1 | LV1 Time | 0~655.35 | S | No | Number | Level 1 undervoltage protection time. |
| gridUnderVoltageVoltage2 | LV2 | 5~95 | % | No | Number | Level 2 undervoltage protection point. |
| gridUnderVoltageTime2 | LV2 Time | 0~655.35 | S | No | Number | Level 2 undervoltage protection time. |
| gridUnderVoltageVoltage3 | LV3 | 5~95 | % | No | Number | Level 3 undervoltage protection point. |
| gridOverFrequencyFrequency1 | High Frequency 1 | 50~65 | HZ | No | Number | Level 1 over frequency protection point. |
| gridOverFrequencyTime1 | HF1 Time | 0~655.35 | S | No | Number | Level 1 over frequency protection time. |
| gridOverFrequencyFrequency2 | HF2 | 50~65 | HZ | No | Number | Level 2 over frequency protection point. |
| gridOverFrequencyTime2 | HF2 Time | 0~655.35 | S | No | Number | Level 2 over frequency protection protection time. |
| gridOverFrequencyFrequency3 | HF3 | 50~65 | HZ | No | Number | Level 3 over frequency protection point. |
| gridUnderFrequencyFrequency1 | Low Frequency1 | 45~60 | HZ | No | Number | Level 1 under frequency protection point. |
| gridUnderFrequencyTime1 | LF1 Time | 0~655.35 | S | No | Number | Level 1 under frequency protection time. |
| gridUnderFrequencyFrequency2 | LF2 | 45~60 | HZ | No | Number | Level 2 under frequency protection point. |
| gridUnderFrequencyTime2 | LF2 Time | 0~655.35 | S | No | Number | Level 2 under frequency protection protection time. |
| gridUnderFrequencyFrequency3 | LF3 | 45~60 | HZ | No | Number | Level 3 under frequency protection point. |
| fpResponseWorkModeEnable | F(P) | 0:Disable1:Enable |  | No | Number | It's used to adjust the output active power of inverter according to the grid frequency |
| fpResponseDelay | Start Delay T | 0~50000 | ms | No | Number | When the grid frequency reaches Start Over F, the inverter will activating active power response to over frequency after a dead time Start Delay T. |
| fpExitDelay | Stop Delay T | 0~50000 | ms | No | Number |  |
| fpOverFrequencyDeratingRatio | Droop Over F | -500~500 | %HZ | No | Number | "Decreases the power percentage of nominal power per Hz. For example, “Start Over F=50.2Hz, Stop Over F=51.2 Hz, Droop Over F =40%PE/Hz” ,define the current Grid Frequency is Fg, when the grid frequency reaches 50.2Hz, the inverter will decrease its active power at Droop of 40%. The total decrease active power=( Fg- Start Over F) * Droop Over F *Pn. when grid frequency is larger than 51.2Hz, the active power will stop decreasing." |
| fpOverFrequencyDeratingStart | Start Over F | 50~65 | HZ | No | Number | F(P) Over Frequency Derating Start |
| fpOverFrequencyDeratingEnd | Stop Over F | 50~65 | HZ | No | Number | F(P) Over Frequency Derating End |
| fpUnderFrequencyDeratingRatio | Droop Under F | -500~500 | %HZ | No | Number | F(P) Under Frequency Derating Ratio |
| fpUnderFrequencyDeratingStart | Start Under F | 45~60 | HZ | No | Number | F(P) Under Frequency Derating Start, Positive represents underfrequency upscaling, negative represents underfrequency downscaling. |
| fpUnderFrequencyDeratingEnd | Stop Under F | 45~60 | HZ | No | Number | F(P) Under Frequency Derating End |
| upDeratingWorkModeEnable | U(P) | 0:Disable1:Enable |  | No | Number | Active power response to Voltage deviation. |
| upDeratingVoltageA | U(P) V1 | 100~140 | % | No | Number | U(P) Derating Voltage A |
| upDeratingVoltageB | U(P) V2 | 100~140 | % | No | Number | U(P) Derating Voltage B |
| upDeratingVoltageC | U(P) V3 | 100~140 | % | No | Number | U(P) Derating Voltage C |
| upDeratingVoltageD | U(P) V4 | 100~140 | % | No | Number | U(P) Derating Voltage D |
| upDeratingActivePowerA | U(P) P1 | 0~110 | % | No | Number | U(P) Derating Active Power A |
| upDeratingActivePowerB | U(P) P2 | 0~110 | % | No | Number | U(P) Derating Active Power B |
| upDeratingActivePowerC | U(P) P3 | 0~110 | % | No | Number | U(P) Derating Active Power C |
| upDeratingActivePowerD | U(P) P4 | 0~110 | % | No | Number | U(P) Derating Active Power D |
| upDeratingDropRate | Enter P Rate | 0.01~500 | %/s | No | Number | U(P) Derating Drop Rate |
| upDeratingRecoveryRate | Exit P Rate | 0.01~500 | %/s | No | Number | U(P) Derating Recovery Rate |
| uqWorkModeEnable | U(Q) | 0:Disable 1:Enable |  | No | Number | Controls the reactive power output as a function of the voltage. |
| uqVoltageRiseStart | U(Q) V1 | 100~120 | % | No | Number | U(Q) Voltage Rise Start |
| uqVoltageRiseEnd | U(Q) V2 | 100~120 | % | No | Number | U(Q) Voltage Rise End |
| uqReactivePowerRiseStart | U(Q) V3 | 0~100 | % | No | Number | U(Q) Reactive Power Rise Start |
| uqReactivePowerRiseEnd | U(Q) V4 | 0~100 | % | No | Number | U(Q) Reactive Power Rise End |
| uqVoltageDropStart | U(Q) Q1 | 80~100 | % | No | Number | U(Q) Voltage Drop Start |
| uqVoltageDropEnd | U(Q) Q2 | 80~100 | % | No | Number | U(Q) Voltage Drop End |
| uqReactivePowerDropStart | U(Q) Q3 | 0~100 | % | No | Number | U(Q) Reactive Power Drop Start |
| uqReactivePowerDropEnd | U(Q) Q4 | 0~100 | % | No | Number | U(Q) Reactive Power Drop End |
| uqReactivePowerLockIn | U(Q)Lock_in/Pn | -100~100 | % | No | Number | U(Q) Reactive Power Lock-In |
| uqReactivePowerLockOut | U(Q)Lock_out/Pn | -100~100 | % | No | Number | U(Q) Reactive Power Lock-Out |
| pqWorkModeEnable | P(Q) | 0:Disable1:Enable |  | No | Number | Controls the reactive power of the output as a function of the active power output. 0: Disable, 1: Enable |
| pqActivePowerA | P(Q)P1 | 0~100 | % | No | Number | P(Q) Active Power A |
| pqActivePowerB | P(Q)P2 | 0~100 | % | No | Number | P(Q) Active Power B |
| pqActivePowerC | P(Q)P3 | 0~100 | % | No | Number | P(Q) Active Power C |
| pqActivePowerD | P(Q)P4 | 0~100 | % | No | Number | P(Q) Active Power D |
| pqReactiveActivePowerA | P(Q)Q1 | -100~100 | % | No | Number | P(Q) Reactive Active Power A |
| pqReactiveActivePowerB | P(Q)Q2 | -100~100 | % | No | Number | P(Q) Reactive Active Power B |
| pqReactiveActivePowerC | P(Q)Q3 | -100~100 | % | No | Number | P(Q) Reactive Active Power C |
| pqReactiveActivePowerD | P(Q)Q4 | -100~100 | % | No | Number | P(Q) Reactive Active Power D |
| ppfWorkModeEnable | P(PF) | 0:Disable1:Enable |  | No | Number | Controls the PF(cos φ) of the output as a function of the active power output. |
| ppfActivePowerA | P(PF)P1 | 0~100 | % | No | Number | P(PF) Active Power A |
| ppfActivePowerB | P(PF)P2 | 0~100 | % | No | Number | P(PF) Active Power B |
| ppfActivePowerC | P(PF)P3 | 0~100 | % | No | Number | P(PF) Active Power C |
| ppfActivePowerD | P(PF)P4 | 0~100 | % | No | Number | P(PF) Active Power D |
| ppfPowerFactorA | P(PF)PF1 | -100~100 | % | No | Number | P(PF) Power Factor A |
| ppfPowerFactorB | P(PF)PF2 | -100~100 | % | No | Number | P(PF) Power Factor B |
| ppfPowerFactorC | P(PF)PF3 | -100~100 | % | No | Number | P(PF) Power Factor C |
| ppfPowerFactorD | P(PF)PF4 | -100~100 | % | No | Number | P(PF) Power Factor D |
| ppfActivePowerLockIn | P(PF)Lock_in/Pn | 0~100 | % | No | Number | When the inverter output active power is higher then Lock-in/Pn rated power, it will enter the P(PF) mode. |
| ppfActivePowerLockOut | P(PF)Lock_out/Pn | 0~100 | % | No | Number | When the inverter output active power is lower then Lock-out/Pn rated power, it will exit the P(PF) mode. |
| upfWorkModeEnable | U(PF) | 0:Disable 1:Enable |  | No | Number | Controls the PF(cos φ) of the output to the Voltage deviation. |
| upfVoltageRiseStart | U(PF)U1 | 0~120 | % | No | Number | U(PF) Voltage Rise Start |
| upfVoltageRiseEnd | U(PF)U2 | 0~120 | % | No | Number | U(PF) Voltage Rise End |
| upfPowerFactorDropStart | U(PF)PF1 | -100~100 | % | No | Number | U(PF) Power Factor Drop Start |
| upfPowerFactorDropEnd | U(PF)PF2 | -100~100 | % | No | Number | U(PF) Power Factor Drop End |
| fgWorkModeEnable | F(G) | 0:Disable1:Enable |  | No | Number | Controls the active power output to the grid frequency deviation. |
| fgUnderFrequencyToDischargeFrequency | Discharge Under F | 45~60 | HZ | No | Number | Discharge Under F: F(G) Under Frequency To Discharge Frequency |
| fgUnderFrequencyToDischargePercentage | Discharge Under P | 0~100 | % | No | Number | Discharge Under P: F(G) Under Frequency To Discharge Percentage |
| fgOverFrequencyToCchargeFrequency | Charge Over F | 50~65 | HZ | No | Number | Charge Over F: F(G) Over Frequency To Ccharge Frequency |
| fgOverFrequencyToChargePercentage | Charge Over P | -100~0 | % | No | Number | Charge Over P: F(G) Over Frequency To Charge Percentage |
| lowVoltageRideThroughEnable | LVRT | 0:Disable 1:Enable |  | No | Number | Low Voltage Ride Through enable |
| lvrtDynamicReactivePowerKfFactor | L_Kf | 0~4 |  | No | Number | Dynamic reactive power factor in LVRT. if the local grid code requires dynamic reactive power support capability in grid low voltage, and the grid voltage is lower than LVRT1 value, the inverter will output reactive current Iq= L_Kf*(Vgrid – LVRT1)*In. |
| highVoltageRideThroughEnable | HVRT | 0:Disable1:Enable |  | No | Number | High Voltage Ride Through enable |
| hvrtDynamicReactivePowerKfFactor | H_Kf | 0~4 |  | No | Number | Dynamic reactive power factor in HVRT. if the local grid code requires dynamic reactive power support capability in grid high voltage, and the grid voltage is higher than HVRT1 value, the inverter will output reactive current Iq= H_Kf*(Vgrid – HVRT1) *In. |
| lvrtVoltage1 | LVRT V1 | 5~90 | % | No | Number | Level 1 undervoltage protection point and enter LVRT Voltage point |
| lvrtTime1 | LVRT T1 | 0~655.35 | S | No | Number | Level 1 undervoltage and enter LVRT Voltage protection time; |
| lvrtVoltage2 | LVRT V2 | 5~90 | % | No | Number | Level 2 undervoltage protection point. |
| lvrtTime2 | LVRT T2 | 0~655.35 | S | No | Number | Level 2 undervoltage protection time. |
| lvrtVoltage3 | LVRT V3 | 5~90 | % | No | Number | Level 3 undervoltage protection point and enter LVRT Voltage point |
| lvrtTime3 | LVRT T3 | 0~655.35 | S | No | Number | Level 3 undervoltage and enter LVRT Voltage protection time; |
| lvrtVoltage4 | LVRT V4 | 5~90 | % | No | Number | Level 4 undervoltage protection point and enter LVRT Voltage point |
| lvrtTime4 | LVRT T4 | 0~655.35 | S | No | Number | Level 4 undervoltage and enter LVRT Voltage protection time; |
| lvrtVoltage5 | LVRT V5 | 5~90 | % | No | Number | Level 5 undervoltage protection point and enter LVRT Voltage point |
| lvrtTime5 | LVRT T5 | 0~655.35 | S | No | Number | Level 5 undervoltage and enter LVRT Voltage protection time; |
| hvrtVoltage1 | HVRT V1 | 110~140 | % | No | Number | Level 1 overvoltage protection point and enter HVRT Voltage point |
| hvrtTime1 | HVRT T1 | 0~655.35 | S | No | Number | Level 1 overvoltage protection and enter HVRT Voltage protection time |
| hvrtVoltage2 | HVRT V2 | 110~140 | % | No | Number | Level 2 overvoltage protection point |
| hvrtTime2 | HVRT T2 | 0~655.35 | S | No | Number | Level 2 overvoltage protection time |
| hvrtVoltage3 | HVRT V3 | 110~140 | % | No | Number | Level 3 overvoltage protection point and enter HVRT Voltage point |
| hvrtTime3 | HVRT T3 | 0~655.35 | S | No | Number | Level 3 overvoltage protection and enter HVRT Voltageprotection time |
| hvrtVoltage4 | HVRT V4 | 110~140 | % | No | Number | Level 4 overvoltage protection point and enter HVRT Voltage point |
| hvrtTime4 | HVRT T4 | 0~655.35 | S | No | Number | Level 4 overvoltage protection and enter HVRT Voltageprotection time |
| hvrtVoltage5 | HVRT V5 | 110~140 | % | No | Number | Level 5 overvoltage protection point and enter HVRT Voltage point |
| hvrtTime5 | HVRT T5 | 0~655.35 | S | No | Number | Level 5 overvoltage protection and enter HVRT Voltageprotection time |
| smartPortModeEnable | Smart Port Mode | 0:Generator1:Smart Load2:Micro Inv |  | No | Number | Generator:Use the GEN port as an generator port.Smart Load Output: Use the GEN port as an AC output port, and the load connected to this port can be controlledon/off by the hybrid inverter.Micro inv input:Use the GEN port as an AC couple input port which can be connected with micro-inverter or other Grid-Tied inverter. |
| genRatePower | GEN Rate Power | 0~500 | KW | No | Number | Allowed Max. power from generator. |
| genInputPowerLimitEnable | GEN Peak-shaving | 0:Disable1:Enable |  | No | Number | Limit the maximum output power of the generator to the set rated power on "GEN PORT USE" page, the rest of power consumption will be provided by inverter to ensure that the generator will not overload. |
| genConnectGridEnable | Generator Connect to Grid Port | 0:Disable 1:Enable |  | No | Number | When the oil engine mode is intelligent load output and the battery energy is high, additional excess power is allowed |
| smartLoadNormalCloseEnable | Smart Load Output | 0:Disable1:Enable |  | No | Number | Use the GEN port as an AC output port, and the load connected to this port can be controlled on/off by the hybrid inverter.e.g.ON: 100%,OFF: 95%: When the battery bank SOC reaches 100%, Smart Load Port will switch on automatically and power the load connected. when the battery bank SOC < 95% , the Smart Load Port will switch off automatically |
| smartLoadCloseBatteryVoltage | Smart Load ON Bat Voltage | 150~800 |  | No | Number | When the oil engine mode is intelligent load output and the battery energy is high, additional excess power is allowed |
| smartLoadOpenBatteryVoltage | Smart Load OFF Bat Voltage | 150~800 |  | No | Number | smart Load Open Battery Voltage |
| smartLoadCloseBatterySoc | Smart Load ON Bat SOC | 0~100 | % | No | Number | Smart Load ON Battery SOC point, Battery SOC at which the Smart load will switch on. |
| smartLoadOpenBatterySoc | Smart Load OFF Bat SOC | 0~100 | % | No | Number | Smart Load OFF Bat SOC: Smart Load OFF Battery SOC point, Battery SOC at which the Smart load will switch off. |
| genOverVoltageVoltage1 | GEN High Voltage1 | 105~150 | % | No | Number | Level 1 overvoltage protection point. |
| genOverVoltageTime1 | GEN HV1 Time | 0~655.35 | S | No | Number | Level 1 overvoltage protection time. |
| genOverVoltageVoltage2 | GEN HV2 | 105~150 | % | No | Number | Level 2 overvoltage protection point. |
| genOverVoltageTime2 | GEN HV2 Time | 0~655.35 | S | No | Number | Level 2 overvoltage protection time. |
| genUnderVoltageVoltage1 | GEN Low Voltage1 | 10~95 | % | No | Number | Level 1 undervoltage protection point. |
| genUnderVoltageTime1 | GEN LV1 Time | 0~655.35 | S | No | Number | Level 1 undervoltage protection point. |
| genUnderVoltageVoltage2 | GEN LV2 | 10~95 | % | No | Number | Level 2 undervoltage protection point. |
| genUnderVoltageTime2 | GEN LV2 Time | 0~655.35 | S | No | Number | Level 2 undervoltage protection point. |
| genOverFrequencyFrequency1 | GEN High Frequency 1 | 50~65 | HZ | No | Number | Level 1 over frequency protection point. |
| genOverFrequencyTime1 | GEN HF1 Time | 0~655.35 | S | No | Number | Level 1 over frequency protection time. |
| genOverFrequencyFrequency2 | GEN HF2 | 50~65 | HZ | No | Number | Level 2 over frequency protection point. |
| genOverFrequencyTime2 | GEN HF2 Time | 0~655.35 | S | No | Number | Level 2 over frequency protection time. |
| genUnderFrequencyFrequency1 | GEN Low Frequency1 | 45~60 | HZ | No | Number | Level 1 under frequency protection point. |
| genUnderFrequencyTime1 | GEN LF1 Time | 0~655.35 | S | No | Number | Level 1 under frequency protection time. |
| genUnderFrequencyFrequency2 | GEN LF2 | 45~60 | HZ | No | Number | Level 2 under frequency protection point. |
| genUnderFrequencyTime2 | GEN LF2 Time | 0~655.35 | S | No | Number | Level 2 under frequency protection time. |
| drmEnable | DRM | 0:Disable1:Enable |  | No | Number | For AS4777 standard |
| ctRatio | CT Ratio | 0~10000 |  | No | Number | The CT ratio of the zero-export to CT mode. |
| leakageCurrentGfciProtectionEnable | GFCI | 0:Disable1:Enable |  | No | Number | The ground-fault circuit interrupter function. |
| leakageCurrentGfciProtectionThreshold | GFCI Value | 0~1000 | mA | No | Number | Leakage current protection point. |
| isoCheckEnable | ISO | 0:Disable1:Enable |  | No | Number | The PV and the battery wiring terminals Positive to ground and negative to ground insulation impedance detection. |
| isoCheckThreshold | ISO Value | 0~2000 | KΩ | No | Number | Insulation impedance protection point. |
| activeIslandingProtectionEnable | Active Islanding | 0:Disable1:Enable |  | No | Number | Active islanding detection enable or not. |
| offGridVoltageCompensation | Voltage Adjust | -20~20 | V | No | Number | If the inverter is working at off grid, we can adjust the output voltage by Voltage Adjust. |
| asymmetricPhaseFeedingEnable | Asymmetric Feeding | 0:Disable1:Enable |  | No | Number | If it was clicked, the inverter will take power from the grid balance of on each phase (L1/L2/L3). |
| machineId | CAN ID | 1~10 |  | No | Number | machine Id |
| dspParallelEnable | Parallel | 0:Disable 1:Enable |  | No | Number | "If user want to parallel operation to Expand system capacity, we need to click the parallel. And in a parallel system, we can have and must have only one Master, and the others must be set as Slaver, and we need to set a unique CAN ID to each inverter, the CAN ID is from 1 to 10." |
| masterSlaverSetting | Master&Slaver | 0:Master1:Slaver |  | No | Number |  |
| factoryReset | Factory Reset | 1:Reset |  | No | Number |  |
| remoteOnOffEnable | Remote control | 0:Turn ON1:Turn OFF |  | No | Number |  |
| clearEnergyStorageLog | Clear Energy Storage Log | 1:Clear |  | No | Number |  |
| genForceRunningEnable | GEN Force | 0:Disable1:Enable |  | No | Number |  |
| zeroExportModeSelection | Zero Export Mode | 0:CT1:Meter |  | No | Number |  |
| gridAutoStartChargeSoc | Grid Auto Start Charge | 0~100 | % | No | Number |  |
| gridAutoExitChargeSoc | Grid Exit Charge | 5~100 | % | No | Number |  |
| gridAutoStartChargeVoltage | Grid Auto Start Charge Voltage | 150~800 | V | No | Number |  |
| gridAutoExitChargeVoltage | Grid Exit Charge Voltage | 150~800 | V | No | Number |  |
| gridStartSignal | Grid Signal | 0:Disable1:Enable |  | No | Number |  |
| genDownTime | Gen Down Time | 0~24 | hours | No | Number |  |
| maxPvInputPower | Max Solar Power | 0~65000 | W | No | Number |  |
| meterSelection | Meter Selection | 0:No electricity meter1:CHNT2:Eastron |  | No | Number |  |
| electricMeterBaudRate | Electric Meter Baud Rate | 0:96001:192002:38400 |  | No | Number |  |
| grid10MinOverVoltageThreshold | 10-Min OV Threshold Grid | 0~200 | % | No | Number |  |
| gridPhaseType | Phase Type | 0:Positive sequence1:Reverse order |  | No | Number |  |
| iTSystem | IT System | 0:Disable1:Enable |  | No | Number |  |
| gridNormalConnectionOvervoltage | High Voltage | 105~150 | % | No | Number |  |
| gridNormalConnectionUndervoltage | Low Voltage | 10~95 | % | No | Number |  |
| gridNormalConnectionOverFrequency | High Frequency | 50~65 | HZ | No | Number |  |
| gridNormalConnectionUnderFrequency | Low Frequency | 45~60 | HZ | No | Number |  |
| gridReconnectionOvervoltage | Reconnection High Voltage | 105~150 | % | No | Number |  |
| gridNormalConnectionUndervoltage | Reconnection Low Voltage | 10~95 | % | No | Number |  |
| gridNormalConnectionOverFrequency | Reconnection High Frequency | 50~65 | HZ | No | Number |  |
| gridNormalConnectionUnderFrequency | Reconnection Low Frequency | 45~60 | HZ | No | Number |  |
| acCoupleFrequencyHigh | AC Couple Frz High | 50~65 | HZ | No | Number |  |
| acCoupleToGridOrLoad | AC Couple to Grid or Load | 0:Disable1:Grid2:Load |  | No | Number |  |
| microInvColseBatVoltage | Micro Inv Closed Bat. Volt. | 150~800 | V | No | Number |  |
| microInvOpenBatVoltage | Micro Inv Open Bat. Volt. | 150~800 | V | No | Number |  |
| microInvColseBatSoc | Micro Inv Closed SOC | 0~100 | % | No | Number |  |
| microInvOpenBatSoc | Micro Inv Open SOC | 0~100 | % | No | Number |  |
| backUpDelay | BackUp Delay | 0~60000 | ms | No | Number |  |
| signalIslandModeEnable | Signal Island Mode | 0:Disable1:Enable |  | No | Number |  |
| faultClearanceAndRestart | Fault Clearance and Restart | 0:Disable1:Enable |  | No | Number |  |
| deviceSn | 013548202500010000 |  |  | Yes | String | Device serial number |

### IVGM100600

| Key | Name | Range | unit | Required | Type | Description |
| --- | ---- | ----- | ---- | -------- | ---- | ----------- |
| acOutputRatedVoltage | AC Output Rated Voltage | 220:220V  230:230V  240:240V | V | NO | Number |  |
| acOutputRatedFrequency | AC Output Rated Frequency | 0:50Hz  1:60Hz | Hz | NO | Number |  |
| gridPowerUnbalanceEnable | Grid Power Unbalance | 0:Disable  1:Enable |  | NO | Number |  |
| powerFactor | Power Factor | -0.99-0.8,0.81 |  | NO | Number |  |
| gridWaveformDetectionMode | Detection Mode | 0:Wave Detect  1:Half Wave Detect  2:Disable Wave Detect |  | NO | Number |  |
| batteryModel | Battery Model | 0:User defined  1:Third party(Lithium battery)  2:Felicity(LPBF/LUX-X series)  3:Felicity(LPBA/LUX-Y/LUX-E  series) |  | NO | Number |  |
| batteryOnGridDischargeDepthSoc | Battery Discharged Depth(On-Grid, Bms Connected) | 10~100 | % | NO | Number | The battery SOC is lower than the battery on-grid discharge depth, and the battery stops discharging |
| batteryOffGridDischargeDepthSoc | Battery Discharged Depth(Off-Grid, Bms Connected) | 0~100 | % | NO | Number | The battery SOC is lower than the battery off-grid discharge depth, and the battery stops discharging |
| batteryOffGridRecoveryDepthSoc | Battery Restart Depth(Off-Grid, Bms Connected) | 0~100 | % | NO | Number | When the battery SOC is lower than the setting value of "Battery discharge depth (off grid)", the inverter can only be output off the grid again after the SOC recovers to the setting value higher than "Battery restart depth |
| lcdBacklightEnable | LCD Backlight | 0:Disable  1:Enable |  | NO | Number |  |
| buzzerEnable | Buzzer | 0:Disable  1:Enable |  | NO | Number |  |
| overLoadProtectionResetEnable | Over Load Protection Reset | 0:Disable  1:Enable |  | NO | Number | The fault will be cleared automatically after the overload protection of the machine. If the overload protection occurs 3 times within half an hour, the overload fault will not be cleared |
| remoteOnOffEnable | Remote control | 0:ON  1:OFF |  | NO | Number | The machine shuts down and enters standby mode |
| remoteOutputOnOffControl | AC Output ON/OFF | 0:ON  1:OFF |  | NO | Number |  |
| zeroExportFunction | Zero Export Mode | 1:To load  2:To CT |  | NO | Number | "The feed power is limited according to the setting of ""grid connection power limit"".1) To load:The inverter can supply power to the backup load and sell power to the grid but the selling power will not exceed the setting value of ""grid connection power limit""2) To CT:The inverter can supply power to the backup load, household load and sell power to the grid, but the selling power will not exceed the setting value of ""grid connection power limit"".In this mode, a CT is needed." |
| zeroExportAdjustmentPower | Zero Export Power | -500~500 | W | NO | Number | When the grid-connected power is set to 0, it is used to calibrate the sampling deviation to ensure that the inverter will not feed power to the grid |
| clearEnergyStorageLog | Clear Energy Storage Log | 1:Clear |  | NO | Number |  |
| clearEventLog | Clear Event Log | 1:Clear |  | NO | Number |  |
| factoryReset | Factory Reset | 1:Reset |  | NO | Number |  |
| eventLogFunctionEnable | Event Log Function | 0:Disable  1:Charge  2:Discharge |  | NO | Number |  |
| faultLogFunctionEnable | Fault Log Function | 0:Disable  1:Charge  2:Discharge |  | NO | Number |  |
| gfciLevel1ProtectionEnable | GFCI One-level Protection | 0:Disable  1:Charge  2:Discharge |  | NO | Number |  |
| gfciLevel2ProtectionEnable | GFCI Two-level Protection | 0:Disable  1:Charge  2:Discharge |  | NO | Number |  |
| gfciLevel3ProtectionEnable | GFCI Three-level Protection | 0:Disable  1:Charge  2:Discharge |  | NO | Number |  |
| isoDetectionEnable | ISO Detection | 0:Disable  1:Charge  2:Discharge |  | NO | Number |  |
| antiIslandingDetectionEnable | Anti-Islanding Detection | 0:Disable  1:Charge  2:Discharge |  | NO | Number |  |
| pvParallelSetting | PV Parallel Set | 0:Stand Alone  1:Parallel |  | NO | Number |  |
| fixQPencent | FixQ Pencent | -60~60 | % | NO | Number |  |
| bmsHeartbeat | BMS Heartbeat | 0:Disable  1:Charge  2:Discharge |  | NO | Number | After enabling, if the battery type is lithium battery and BMS communication fails, it will report BMS communication failure |
| operatedMode | Operated Mode | 0:General Mode  1:Backup Mode  2:Eco Mode  3:Gen Mode |  | NO | Number | "Set inverter operation mode:1) General mode:In this mode, the load is mainly powered by PV and battery.2) Backup mode:In this mode, PV gives priority to charging the battery to ensure that the battery is always full.3) ECO mode:In this mode, you can set a specific time to take power from the grid to charge the battery or use the power of the grid to charge the battery, and operate in general mode outside the set time.4) Generator mode:In this mode, the load is mainly powered by PV and battery." |
| ecoRule1.ruleMode | ECO Mode 1 | 0:Disable  1:Charge  2:Discharge   3:AC Couple |  | NO | Number | "Economic model rules:1) Disable: No charging and discharging2) Charge: Charge the battery from the grid3) Discharge: Selling power from battery to the grid4)AC Couple:Spontaneous self-use, waste electricity Internet access" |
| ecoRule1.startTime | Start Time1 | HH:023 mm:059 |  | NO | String | Starting time, Format: HH:mm |
| ecoRule1.stopTime | Stop Time1 | HH:023 mm:059 |  | NO | String | Stop time, Format: HH:mm |
| ecoRule1.startDay | Start Day1 | MM:112 dd:131 |  | NO | String | Starting day, Format: MM:dd |
| ecoRule1.stopDay | Stop Day1 | MM:112 dd:131 |  | NO | String | Stop day, Format: MM:dd |
| ecoRule1.daysOfEffectiveWeek | Effective Week1 | MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY |  | NO | Array | Week Of Use: Time Of Use Effective Week,Valuable：MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY，Multiple Choice |
| ecoRule1.soc | SOC1 | 0~100 | % | NO | Number |  |
| ecoRule1.voltage | Voltage1 | 48~60 | V | NO | Number | "1) Charging: Stop charging voltage. Battery voltage above this value stops charging (usually set to 57.6v for a single battery).2) Discharge: Stop discharge voltage. If the battery voltage is lower than this value, it will stop discharging." |
| ecoRule1.power | Power1 | "Master Version <212 : 010000Master Version ≥212 : -1000010000" | W | NO | Number | "1) Charging: Battery charging power2) Discharge: Battery discharge power3)Dispatched power: Grid power supply or intake power" |
| ecoRule2.ruleMode | ECO Mode 2 | 0:Disable  1:Charge  2:Discharge   3:AC Couple |  | NO | Number | "Economic model rules:1) Disable: No charging and discharging2) Charge: Charge the battery from the grid3) Discharge: Selling power from battery to the grid4)AC Couple:Spontaneous self-use, waste electricity Internet access" |
| ecoRule2.startTime | Start Time2 | HH:023 mm:059 |  | NO | String | Starting time, Format: HH:mm |
| ecoRule2.stopTime | Stop Time2 | HH:023 mm:059 |  | NO | String | Stop time, Format: HH:mm |
| ecoRule2.startDay | Start Day2 | MM:112 dd:131 |  | NO | String | Starting day, Format: MM:dd |
| ecoRule2.stopDay | Stop Day2 | MM:112 dd:131 |  | NO | String | Stop day, Format: MM:dd |
| ecoRule2.voltage | Voltage2 | 48~60 | V | NO | Number | "1) Charging: Stop charging voltage. Battery voltage above this value stops charging (usually set to 57.6v for a single battery).2) Discharge: Stop discharge voltage. If the battery voltage is lower than this value, it will stop discharging." |
| ecoRule2.power | Power2 | "Master Version <212 : 010000Master Version ≥212 : -1000010000" | W | NO | Number | "1) Charging: Battery charging power2) Discharge: Battery discharge power3)Dispatched power: Grid power supply or intake power" |
| ecoRule2.daysOfEffectiveWeek | Effective Week2 | MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY |  | NO | Array | Week Of Use: Time Of Use Effective Week,Valuable：MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY，Multiple Choice |
| ecoRule2.soc | SOC2 | 0~100 | % | NO | Number |  |
| ecoRule3.ruleMode | ECO Mode 3 | 0:Disable  1:Charge  2:Discharge   3:AC Couple |  | NO | Number | "Economic model rules:1) Disable: No charging and discharging2) Charge: Charge the battery from the grid3) Discharge: Selling power from battery to the grid4)AC Couple:Spontaneous self-use, waste electricity Internet access" |
| ecoRule3.startTime | Start Time3 | HH:023 mm:059 |  | NO | String | Starting time, Format: HH:mm |
| ecoRule3.stopTime | Stop Time3 | HH:023 mm:059 |  | NO | String | Stop time, Format: HH:mm |
| ecoRule3.startDay | Start Day3 | MM:112 dd:131 |  | NO | String | Starting day, Format: MM:dd |
| ecoRule3.stopDay | Stop Day3 | MM:112 dd:131 |  | NO | String | Stop day, Format: MM:dd |
| ecoRule3.daysOfEffectiveWeek | Effective Week3 | MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY |  | NO | Array | Week Of Use: Time Of Use Effective Week,Valuable：MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY，Multiple Choice |
| ecoRule3.soc | SOC3 | 0~100 | % | NO | Number |  |
| ecoRule3.voltage | Voltage3 | 48~60 | V | NO | Number | "1) Charging: Stop charging voltage. Battery voltage above this value stops charging (usually set to 57.6v for a single battery).2) Discharge: Stop discharge voltage. If the battery voltage is lower than this value, it will stop discharging." |
| ecoRule3.power | Power3 | "Master Version <212 : 010000Master Version ≥212 : -1000010000" | W | NO | Number | "1) Charging: Battery charging power2) Discharge: Battery discharge power3)Dispatched power: Grid power supply or intake power" |
| ecoRule4.ruleMode | ECO Mode 4 | 0:Disable  1:Charge  2:Discharge   3:AC Couple |  | NO | Number | "Economic model rules:1) Disable: No charging and discharging2) Charge: Charge the battery from the grid3) Discharge: Selling power from battery to the grid4)AC Couple:Spontaneous self-use, waste electricity Internet access" |
| ecoRule4.startTime | Start Time4 | HH:023 mm:059 |  | NO | String | Starting time, Format: HH:mm |
| ecoRule4.stopTime | Stop Time4 | HH:023 mm:059 |  | NO | String | Stop time, Format: HH:mm |
| ecoRule4.startDay | Start Day4 | MM:112 dd:131 |  | NO | String | Starting day, Format: MM:dd |
| ecoRule4.stopDay | Stop Day4 | MM:112 dd:131 |  | NO | String | Stop day, Format: MM:dd |
| ecoRule4.voltage | Voltage4 | 48~60 | V | NO | Number | "1) Charging: Stop charging voltage. Battery voltage above this value stops charging (usually set to 57.6v for a single battery).2) Discharge: Stop discharge voltage. If the battery voltage is lower than this value, it will stop discharging." |
| ecoRule4.power | Power4 | "Master Version <212 : 010000Master Version ≥212 : -1000010000" | W | NO | Number | "1) Charging: Battery charging power2) Discharge: Battery discharge power3)Dispatched power: Grid power supply or intake power" |
| ecoRule4.daysOfEffectiveWeek | Effective Week4 | MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY |  | NO | Array | Week Of Use: Time Of Use Effective Week,Valuable：MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY，Multiple Choice |
| ecoRule4.soc | SOC4 | 0~100 | % | NO | Number |  |
| batteryModules | Battery Modules | 4~10 |  | NO | Number |  |
| batteryChargedVoltage | Battery Charged Voltage | 48~60 | V | NO | Number |  |
| batteryFloatingChargedVoltage | Bat float voltage | 48~60 | V | NO | Number |  |
| noBmsOnGridBatteryCutOffVoltage | Battery Cut-Off Voltage(On-Grid, No Bms) | 40~60 | V | NO | Number |  |
| noBmsOffGridBatteryCutOffVoltage | Battery Cut-Off Voltage(Off-Grid, No Bms) | 40~60 | V | NO | Number |  |
| noBmsOffGridBatteryRestartVoltage | Battery Restart Voltage(Off-Grid, No Bms) | 40~60 | V | NO | Number |  |
| batteryMaxChargedCurrent | Battery Max. Charged Current | 1~25 | A | NO | Number |  |
| batteryMaxDischargeCurrent | Battery Max. Discharged Current | 5~25 | A | NO | Number |  |
| --- | --- | --- | --- | --- | --- | --- |
| gridStandardCode | Standard | 0:Germany  1:Warehouse  2:50Hz grid default  3:60Hz grid default  4:Italy  5:Britain  6:Australia  7:New Zealand  8:South African  9:Netherland  10:Brazil  11:Europe  12:Poland  13:Czech |  | No | Number | Set the on-grid regulations in the current region |
| overVoltageStage1TripTime | OV Stage1 Trip Time | 0.02~1000 | Sec | No | Number |  |
| underVoltageStage1TripTime | UV Stage1 Trip Time | 0.02~1000 | Sec | No | Number |  |
| overVoltageStage2TripTime | OV Stage2 Trip Time | 0.02~1000 | Sec | No | Number |  |
| underVoltageStage2TripTime | UV Stage2 Trip Time | 0.02~1000 | Sec | No | Number |  |
| overVoltage10mTriggerValue | OV 10Min Mean Value | 230~300 | V | No | Number |  |
| overFrequencyStage1TripTime | OF Stage1 Trip Time | 0.02~1000 | Sec | No | Number |  |
| underFrequencyStage1TripTime | UF Stage1 Trip Time | 0.02~1000 | Sec | No | Number |  |
| overFrequencyStage2TripTime | OF Stage2 Trip Time | 0.02~1000 | Sec | No | Number |  |
| underFrequencyStage2TripTime | UF Stage2 Trip Time | 0.02~1000 | Sec | No | Number |  |
| onGridObservationTime | Observation Time | 1~3000 | Sec | No | Number |  |
| onGridPowerSlope | Grid Power Slope | 0~65535 | Sec | No | Number |  |
| onGridPowerLimit | Grid Power Limit | 0~100 | % | No | Number |  |
| pfPowerCurveFunctionEnable | PF-Power Curve Function | 0:Disable  1:Enable |  | No | Number |  |
| pfPowerCurvePointAPower | Point A Power | 0~100 | % | No | Number |  |
| pfPowerCurvePointAPowerFactor | Point A Power Factor | -0.99-0.8,0.81 |  | No | Number |  |
| pfPowerCurvePointBPower | Point B Power | 0~100 | % | No | Number |  |
| pfPowerCurvePointBPowerFactor | Point B Power Factor | -0.99-0.8,0.81 |  | No | Number |  |
| pfPowerCurvePointCPower | Point C Power | 0~100 | % | No | Number |  |
| pfPowerCurvePointCPowerFactor | Point C Power Factor | -0.99-0.8,0.81 |  | No | Number |  |
| pfPowerCurveLockoutPower | Lockout Power | 0~100 | % | No | Number |  |
| puCurveFunctionEnable | P(U) Curve Function | 0:Disable  1:Enable |  | No | Number |  |
| puCurvePointAActivePower | Point A  Active Power | -100~100 | % | No | Number |  |
| puCurvePointBActivePower | Point B  Active Power | -100~100 | % | No | Number |  |
| puCurvePointCActivePower | Point C  Active Power | -100~100 | % | No | Number |  |
| puCurvePointDActivePower | Point D  Active Power | -100~100 | % | No | Number |  |
| quCurveFunctionEnable | Q(U) Curve Function | 0:Disable  1:Enable |  | No | Number |  |
| quCurvePointAReactivePower | Point A  Reactive Power | -100~100 | % | No | Number |  |
| quCurvePointBReactivePower | Point B  Reactive Power | -100~100 | % | No | Number |  |
| quCurvePointCReactivePower | Point C  Reactive Power | -100~100 | % | No | Number |  |
| quCurvePointDReactivePower | Point D  Reactive Power | -100~100 | % | No | Number |  |
| quCurveLockInPower | Lock In Power | -100~100 | % | No | Number |  |
| quCurveLockOutPower | Lock Out Power | -100~100 | % | No | Number |  |
| fpCurveFunctionEnable | FP Curve Function | 0:Disable  1:Enable |  | No | Number |  |
| fpCurveOverFrequencyLowerLimit | Over Frequency Start Point | 30~80 | Hz | No | Number |  |
| fpUnderFrequencyLowerLimit | Under Frequency Start Point | 30~80 | Hz | No | Number |  |
| fpOverFrequencyUpperLimit | Over Frequency End Point | 30~80 | Hz | No | Number |  |
| fpUnderFrequencyUpperLimit | Under Frequency End Point | 30~80 | Hz | No | Number |  |
| fpRestoreFrequencyUperLimit | F(Stop) Upper | 30~80 | Hz | No | Number |  |
| fpRestoreFrequencyLowerLimit | F(Stop) Lower | 30~80 | Hz | No | Number |  |
| fpRestoreFrequencyWaitingTime | Restore Waiting Time | 1~65535 | Sec | No | Number |  |
| fpRestoreFrequencyPowerSlope | Reconnection Power Slope | 1~65535 | Sec | No | Number |  |
| fpOverFrequencyPowerSlope | Over Frequency Power Slope | 0~100 | % | No | Number |  |
| fpUnderFrequencyPowerSlope | Under Frequency Power Slope | 0~100 | % | No | Number |  |
| fpRecoveryPowerSlope | Recovery Power Slope | 0~100 | % | No | Number |  |
| fpChargeCurveFunctionEnable | FP Charge Curve Function | 0:Disable  1:Enable |  | No | Number |  |
| fpUnderFrequencyPowerSlopeForCharge | Under Frequency Power Slope For Charge | 0~100 | % | No | Number |  |
| lowVoltageRideThroughFunctionEnable | Low Voltage Ride Through | 0:Disable  1:Enable |  | No | Number |  |
| lowVoltageStartPointTripTime | Start Point Of Protection Time | 0.02~1000 | Sec | No | Number |  |
| lowVoltageEndPointTripTime | End Point Of Protection Time | 0.02~1000 | Sec | No | Number |  |
| highVoltageRideThroughFunctionEnable | High Voltage Ride Through Function | 0:Disable  1:Enable |  | No | Number |  |
| highVoltageStartPointTripTime | Start Point Of Protection Time | 0.02~1000 | Sec | No | Number |  |
| highVoltageEndPointTripTime | End Point Of Protection Time | 0.02~1000 | Sec | No | Number |  |
| overVoltageStage1TripValue | OV Stage1 Trip Value | 230~300 | V | No | Number |  |
| underVoltageStage1TripValue | UV Stage1 Trip Value | 0.1~300 | V | No | Number |  |
| overVoltageStage2TripValue | OV Stage2 Trip Value | 230~300 | V | No | Number |  |
| underVoltageStage2TripValue | UV Stage2 Trip Value | 0.1~300 | V | No | Number |  |
| overFrequencyStage1TripValue | OF Stage1 Trip Value | 30~80 | Hz | No | Number |  |
| underFrequencyStage1TripValue | UF Stage1 Trip Value | 30~80 | Hz | No | Number |  |
| overFrequencyStage2TripValue | OF Stage2 Trip Value | 30~80 | Hz | No | Number |  |
| underFrequencyStage2TripValue | UF Stage2 Trip Value | 30~80 | Hz | No | Number |  |
| pfPowerCurveLockinVoltage | Lockin Voltage | 60~300 | V | No | Number |  |
| pfPowerCurveLockoutVoltage | Lockout Voltage | 60~300 | V | No | Number |  |
| puCurvePointAVoltage | Point A Voltage | 60~300 | V | No | Number |  |
| puCurvePointBVoltage | Point B  Voltage | 60~300 | V | No | Number |  |
| puCurvePointCVoltage | Point C  Voltage | 60~300 | V | No | Number |  |
| puCurvePointDVoltage | Point D  Voltage | 60~300 | V | No | Number |  |
| quCurvePointAVoltage | Point A Voltage | 60~300 | V | No | Number |  |
| quCurvePointBVoltage | Point B  Voltage | 60~300 | V | No | Number |  |
| quCurvePointCVoltage | Point C  Voltage | 60~300 | V | No | Number |  |
| quCurvePointDVoltage | Point D  Voltage | 60~300 | V | No | Number |  |
| lowVoltageStartPointTripValue | Start Point Of Ride Through | 0~230 | V | No | Number |  |
| lowVoltageEndPointTripValue | End Point Of Ride Through | 0~230 | V | No | Number |  |
| lowVoltageCrossingTripThreshold | Low Voltage Limit Of Ride Through | 0~230 | V | No | Number |  |
| highVoltageStartPointTripValue | Start Point Of Ride Through | 230~300 | V | No | Number |  |
| highVoltageEndPointTripValue | End Point Of Ride Through | 230~300 | V | No | Number |  |
| highVoltageCrossingTripThreshold | High Voltage Limit Of Ride Through | 230~300 | V | No | Number |  |
| commOffLineEnable | CommOffLine | 0:Disable  1:Enable |  | No | Number |  |
| autoTestEnable | AutoTestEnable | 0:Disable  1:Enable |  | No | Number |  |
| deratingByVoltageEnable | DeratingByVoltage | 0:Disable  1:Enable |  | No | Number |  |
| deviceSn | 013548202500010000 |  |  | Yes | String | Device serial number |

### IVGM10048

| Key | Name | Range | unit | Required | Type | Description |
| --- | ---- | ----- | ---- | -------- | ---- | ----------- |
| acOutputRatedVoltage | AC Output Rated Voltage | 220:220V  230:230V  240:240V | V | NO | Number |  |
| acOutputRatedFrequency | AC Output Rated Frequency | 0:50Hz  1:60Hz | Hz | NO | Number |  |
| gridPowerUnbalanceEnable | Grid Power Unbalance | 0:Disable  1:Enable |  | NO | Number |  |
| powerFactor | Power Factor | -0.99-0.8,0.81 |  | NO | Number |  |
| gridWaveformDetectionMode | Detection Mode | 0:Wave Detect  1:Half Wave Detect  2:Disable Wave Detect |  | NO | Number |  |
| batteryModel | Battery Model | 0:User defined  1:Third party(Lithium battery)  2:Felicity(LPBF/LUX-X series)  3:Felicity(LPBA/LUX-Y/LUX-E  series) |  | NO | Number |  |
| batteryOnGridDischargeDepthSoc | Battery Discharged Depth(On-Grid, Bms Connected) | 10~100 | % | NO | Number | The battery SOC is lower than the battery on-grid discharge depth, and the battery stops discharging |
| batteryOffGridDischargeDepthSoc | Battery Discharged Depth(Off-Grid, Bms Connected) | 0~100 | % | NO | Number | The battery SOC is lower than the battery off-grid discharge depth, and the battery stops discharging |
| batteryOffGridRecoveryDepthSoc | Battery Restart Depth(Off-Grid, Bms Connected) | 0~100 | % | NO | Number | When the battery SOC is lower than the setting value of "Battery discharge depth (off grid)", the inverter can only be output off the grid again after the SOC recovers to the setting value higher than "Battery restart depth |
| lcdBacklightEnable | LCD Backlight | 0:Disable  1:Enable |  | NO | Number |  |
| buzzerEnable | Buzzer | 0:Disable  1:Enable |  | NO | Number |  |
| overLoadProtectionResetEnable | Over Load Protection Reset | 0:Disable  1:Enable |  | NO | Number | The fault will be cleared automatically after the overload protection of the machine. If the overload protection occurs 3 times within half an hour, the overload fault will not be cleared |
| remoteOnOffEnable | Remote control | 0:ON  1:OFF |  | NO | Number | The machine shuts down and enters standby mode |
| remoteOutputOnOffControl | AC Output ON/OFF | 0:ON  1:OFF |  | NO | Number |  |
| zeroExportFunction | Zero Export Mode | 1:To load  2:To CT |  | NO | Number | "The feed power is limited according to the setting of ""grid connection power limit"".1) To load:The inverter can supply power to the backup load and sell power to the grid but the selling power will not exceed the setting value of ""grid connection power limit""2) To CT:The inverter can supply power to the backup load, household load and sell power to the grid, but the selling power will not exceed the setting value of ""grid connection power limit"".In this mode, a CT is needed." |
| zeroExportAdjustmentPower | Zero Export Power | -500~500 | W | NO | Number | When the grid-connected power is set to 0, it is used to calibrate the sampling deviation to ensure that the inverter will not feed power to the grid |
| clearEnergyStorageLog | Clear Energy Storage Log | 1:Clear |  | NO | Number |  |
| clearEventLog | Clear Event Log | 1:Clear |  | NO | Number |  |
| factoryReset | Factory Reset | 1:Reset |  | NO | Number |  |
| eventLogFunctionEnable | Event Log Function | 0:Disable  1:Charge  2:Discharge |  | NO | Number |  |
| faultLogFunctionEnable | Fault Log Function | 0:Disable  1:Charge  2:Discharge |  | NO | Number |  |
| gfciLevel1ProtectionEnable | GFCI One-level Protection | 0:Disable  1:Charge  2:Discharge |  | NO | Number |  |
| gfciLevel2ProtectionEnable | GFCI Two-level Protection | 0:Disable  1:Charge  2:Discharge |  | NO | Number |  |
| gfciLevel3ProtectionEnable | GFCI Three-level Protection | 0:Disable  1:Charge  2:Discharge |  | NO | Number |  |
| isoDetectionEnable | ISO Detection | 0:Disable  1:Charge  2:Discharge |  | NO | Number |  |
| antiIslandingDetectionEnable | Anti-Islanding Detection | 0:Disable  1:Charge  2:Discharge |  | NO | Number |  |
| pvParallelSetting | PV Parallel Set | 0:Stand Alone  1:Parallel |  | NO | Number |  |
| fixQPencent | FixQ Pencent | -60~60 | % | NO | Number |  |
| bmsHeartbeat | BMS Heartbeat | 0:Disable  1:Charge  2:Discharge |  | NO | Number | After enabling, if the battery type is lithium battery and BMS communication fails, it will report BMS communication failure |
| operatedMode | Operated Mode | 0:General Mode  1:Backup Mode  2:Eco Mode  3:Gen Mode |  | NO | Number | "Set inverter operation mode:1) General mode:In this mode, the load is mainly powered by PV and battery.2) Backup mode:In this mode, PV gives priority to charging the battery to ensure that the battery is always full.3) ECO mode:In this mode, you can set a specific time to take power from the grid to charge the battery or use the power of the grid to charge the battery, and operate in general mode outside the set time.4) Generator mode:In this mode, the load is mainly powered by PV and battery." |
| ecoRule1.ruleMode | ECO Mode 1 | 0:Disable  1:Charge  2:Discharge   3:AC Couple |  | NO | Number | "Economic model rules:1) Disable: No charging and discharging2) Charge: Charge the battery from the grid3) Discharge: Selling power from battery to the grid4)AC Couple:Spontaneous self-use, waste electricity Internet access" |
| ecoRule1.startTime | Start Time1 | HH:023 mm:059 |  | NO | String | Starting time, Format: HH:mm |
| ecoRule1.stopTime | Stop Time1 | HH:023 mm:059 |  | NO | String | Stop time, Format: HH:mm |
| ecoRule1.startDay | Start Day1 | MM:112 dd:131 |  | NO | String | Starting day, Format: MM:dd |
| ecoRule1.stopDay | Stop Day1 | MM:112 dd:131 |  | NO | String | Stop day, Format: MM:dd |
| ecoRule1.daysOfEffectiveWeek | Effective Week1 | MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY |  | NO | Array | Week Of Use: Time Of Use Effective Week,Valuable：MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY，Multiple Choice |
| ecoRule1.soc | SOC1 | 0~100 | % | NO | Number |  |
| ecoRule1.voltage | Voltage1 | 48~60 | V | NO | Number | "1) Charging: Stop charging voltage. Battery voltage above this value stops charging (usually set to 57.6v for a single battery).2) Discharge: Stop discharge voltage. If the battery voltage is lower than this value, it will stop discharging." |
| ecoRule1.power | Power1 | "Slave Version <106 : 010000Slave Version ≥106 : -1000010000" | W | NO | Number | "1) Charging: Battery charging power2) Discharge: Battery discharge power3)Dispatched power: Grid power supply or intake power" |
| ecoRule2.ruleMode | ECO Mode 2 | 0:Disable  1:Charge  2:Discharge   3:AC Couple |  | NO | Number | "Economic model rules:1) Disable: No charging and discharging2) Charge: Charge the battery from the grid3) Discharge: Selling power from battery to the grid |
| 4)AC Couple:Spontaneous self-use, waste electricity Internet access" |  |  |  |  |  |  |
| ecoRule2.startTime | Start Time2 | HH:023 mm:059 |  | NO | String | Starting time, Format: HH:mm |
| ecoRule2.stopTime | Stop Time2 | HH:023 mm:059 |  | NO | String | Stop time, Format: HH:mm |
| ecoRule2.startDay | Start Day2 | MM:112 dd:131 |  | NO | String | Starting day, Format: MM:dd |
| ecoRule2.stopDay | Stop Day2 | MM:112 dd:131 |  | NO | String | Stop day, Format: MM:dd |
| ecoRule2.voltage | Voltage2 | 48~60 | V | NO | Number | "1) Charging: Stop charging voltage. Battery voltage above this value stops charging (usually set to 57.6v for a single battery).2) Discharge: Stop discharge voltage. If the battery voltage is lower than this value, it will stop discharging." |
| ecoRule2.power | Power2 | "Slave Version <106 : 010000Slave Version ≥106 : -1000010000" | W | NO | Number | "1) Charging: Battery charging power2) Discharge: Battery discharge power3)Dispatched power: Grid power supply or intake power" |
| ecoRule2.daysOfEffectiveWeek | Effective Week2 | MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY |  | NO | Array | Week Of Use: Time Of Use Effective Week,Valuable：MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY，Multiple Choice |
| ecoRule2.soc | SOC2 | 0~100 | % | NO | Number |  |
| ecoRule3.ruleMode | ECO Mode 3 | 0:Disable  1:Charge  2:Discharge   3:AC Couple |  | NO | Number | "Economic model rules:1) Disable: No charging and discharging2) Charge: Charge the battery from the grid3) Discharge: Selling power from battery to the grid4)AC Couple:Spontaneous self-use, waste electricity Internet access" |
| ecoRule3.startTime | Start Time3 | HH:023 mm:059 |  | NO | String | Starting time, Format: HH:mm |
| ecoRule3.stopTime | Stop Time3 | HH:023 mm:059 |  | NO | String | Stop time, Format: HH:mm |
| ecoRule3.startDay | Start Day3 | MM:112 dd:131 |  | NO | String | Starting day, Format: MM:dd |
| ecoRule3.stopDay | Stop Day3 | MM:112 dd:131 |  | NO | String | Stop day, Format: MM:dd |
| ecoRule3.daysOfEffectiveWeek | Effective Week3 | MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY |  | NO | Array | Week Of Use: Time Of Use Effective Week,Valuable：MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY，Multiple Choice |
| ecoRule3.soc | SOC3 | 0~100 | % | NO | Number |  |
| ecoRule3.voltage | Voltage3 | 48~60 | V | NO | Number | "1) Charging: Stop charging voltage. Battery voltage above this value stops charging (usually set to 57.6v for a single battery).2) Discharge: Stop discharge voltage. If the battery voltage is lower than this value, it will stop discharging." |
| ecoRule3.power | Power3 | "Slave Version <106 : 010000Slave Version ≥106 : -1000010000" | W | NO | Number | "1) Charging: Battery charging power2) Discharge: Battery discharge power3)Dispatched power: Grid power supply or intake power" |
| ecoRule4.ruleMode | ECO Mode 4 | 0:Disable  1:Charge  2:Discharge   3:AC Couple |  | NO | Number | "Economic model rules:1) Disable: No charging and discharging2) Charge: Charge the battery from the grid3) Discharge: Selling power from battery to the grid4)AC Couple:Spontaneous self-use, waste electricity Internet access" |
| ecoRule4.startTime | Start Time4 | HH:023 mm:059 |  | NO | String | Starting time, Format: HH:mm |
| ecoRule4.stopTime | Stop Time4 | HH:023 mm:059 |  | NO | String | Stop time, Format: HH:mm |
| ecoRule4.startDay | Start Day4 | MM:112 dd:131 |  | NO | String | Starting day, Format: MM:dd |
| ecoRule4.stopDay | Stop Day4 | MM:112 dd:131 |  | NO | String | Stop day, Format: MM:dd |
| ecoRule4.voltage | Voltage4 | 48~60 | V | NO | Number | "1) Charging: Stop charging voltage. Battery voltage above this value stops charging (usually set to 57.6v for a single battery).2) Discharge: Stop discharge voltage. If the battery voltage is lower than this value, it will stop discharging." |
| ecoRule4.power | Power4 | "Slave Version <106 : 010000Slave Version ≥106 : -1000010000" | W | NO | Number | "1) Charging: Battery charging power2) Discharge: Battery discharge power3)Dispatched power: Grid power supply or intake power" |
| ecoRule4.daysOfEffectiveWeek | Effective Week4 | MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY |  | NO | Array | Week Of Use: Time Of Use Effective Week,Valuable：MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY，Multiple Choice |
| ecoRule4.soc | SOC4 | 0~100 | % | NO | Number |  |
| additionalEcoEnable | ECO 10 enable | 0:Disable  1:Enable |  | NO | Number | Only when Master Version ≥ 2204，parameter can be used, ecoRule5 ~ecoRule10 also.After enabling, there will be 10 economic rules that can be set.Only trial on some devices. If there is no value displayed or it cannot run, please use the old 4-segment mode. |
| ecoRule5.ruleMode | ECO Mode 5 | 0:Disable  1:Charge  2:Discharge |  | NO | Number | "Economic model rules:1) Disable: No charging and discharging2) Charge: Charge the battery from the grid3) Discharge: Selling power from battery to the grid4)AC Couple:Spontaneous self-use, waste electricity Internet access" |
| ecoRule5.startTime | Start Time5 | HH:023 mm:059 |  | NO | String | Starting time, Format: HH:mm |
| ecoRule5.stopTime | Stop Time5 | HH:023 mm:059 |  | NO | String | Stop time, Format: HH:mm |
| ecoRule5.startDay | Start Day5 | MM:112 dd:131 |  | NO | String | Starting day, Format: MM:dd |
| ecoRule5.stopDay | Stop Day5 | MM:112 dd:131 |  | NO | String | Stop day, Format: MM:dd |
| ecoRule5.voltage | Voltage5 | 48~60 | V | NO | Number |  |
| ecoRule5.power | Power5 | 0~10000 | W | NO | Number |  |
| ecoRule5.daysOfEffectiveWeek | Effective Week5 | MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY |  | NO | Array | Week Of Use: Time Of Use Effective Week,Valuable：MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY，Multiple Choice |
| ecoRule5.soc | SOC5 | 0~100 | % | NO | Number |  |
| ecoRule6.ruleMode | ECO Mode 6 | 0:Disable  1:Charge  2:Discharge |  | NO | Number | "Economic model rules:1) Disable: No charging and discharging2) Charge: Charge the battery from the grid3) Discharge: Selling power from battery to the grid |
| 4)AC Couple:Spontaneous self-use, waste electricity Internet access" |  |  |  |  |  |  |
| ecoRule6.startTime | Start Time6 | HH:023 mm:059 |  | NO | String | Starting time, Format: HH:mm |
| ecoRule6.stopTime | Stop Time6 | HH:023 mm:059 |  | NO | String | Stop time, Format: HH:mm |
| ecoRule6.startDay | Start Day6 | MM:112 dd:131 |  | NO | String | Starting day, Format: MM:dd |
| ecoRule6.stopDay | Stop Day6 | MM:112 dd:131 |  | NO | String | Stop day, Format: MM:dd |
| ecoRule6.voltage | Voltage6 | 48~60 | V | NO | Number |  |
| ecoRule6.power | Power6 | 0~10000 | W | NO | Number |  |
| ecoRule6.daysOfEffectiveWeek | Effective Week6 | MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY |  | NO | Array | Week Of Use: Time Of Use Effective Week,Valuable：MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY，Multiple Choice |
| ecoRule6.soc | SOC6 | 0~100 | % | NO | Number |  |
| ecoRule7.ruleMode | ECO Mode 7 | 0:Disable  1:Charge  2:Discharge |  | NO | Number | "Economic model rules:1) Disable: No charging and discharging2) Charge: Charge the battery from the grid3) Discharge: Selling power from battery to the grid4)AC Couple:Spontaneous self-use, waste electricity Internet access" |
| ecoRule7.startTime | Start Time7 | HH:023 mm:059 |  | NO | String | Starting time, Format: HH:mm |
| ecoRule7.stopTime | Stop Time7 | HH:023 mm:059 |  | NO | String | Stop time, Format: HH:mm |
| ecoRule7.startDay | Start Day7 | MM:112 dd:131 |  | NO | String | Starting day, Format: MM:dd |
| ecoRule7.stopDay | Stop Day7 | MM:112 dd:131 |  | NO | String | Stop day, Format: MM:dd |
| ecoRule7.voltage | Voltage7 | 48~60 | V | NO | Number |  |
| ecoRule7.power | Power7 | 0~10000 | W | NO | Number |  |
| ecoRule7.daysOfEffectiveWeek | Effective Week7 | MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY |  | NO | Array | Week Of Use: Time Of Use Effective Week,Valuable：MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY，Multiple Choice |
| ecoRule7.soc | SOC7 | 0~100 | % | NO | Number |  |
| ecoRule8.ruleMode | ECO Mode 8 | 0:Disable  1:Charge  2:Discharge |  | NO | Number | "Economic model rules:1) Disable: No charging and discharging2) Charge: Charge the battery from the grid3) Discharge: Selling power from battery to the grid |
| 4)AC Couple:Spontaneous self-use, waste electricity Internet access" |  |  |  |  |  |  |
| ecoRule8.startTime | Start Time8 | HH:023 mm:059 |  | NO | String | Starting time, Format: HH:mm |
| ecoRule8.stopTime | Stop Time8 | HH:023 mm:059 |  | NO | String | Stop time, Format: HH:mm |
| ecoRule8.startDay | Start Day8 | MM:112 dd:131 |  | NO | String | Starting day, Format: MM:dd |
| ecoRule8.stopDay | Stop Day8 | MM:112 dd:131 |  | NO | String | Stop day, Format: MM:dd |
| ecoRule8.voltage | Voltage8 | 48~60 | V | NO | Number |  |
| ecoRule8.power | Power8 | 0~10000 | W | NO | Number |  |
| ecoRule8.daysOfEffectiveWeek | Effective Week8 | MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY |  | NO | Array | Week Of Use: Time Of Use Effective Week,Valuable：MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY，Multiple Choice |
| ecoRule8.soc | SOC8 | 0~100 | % | NO | Number |  |
| ecoRule9.ruleMode | ECO Mode 9 | 0:Disable  1:Charge  2:Discharge |  | NO | Number | "Economic model rules:1) Disable: No charging and discharging2) Charge: Charge the battery from the grid3) Discharge: Selling power from battery to the grid4)AC Couple:Spontaneous self-use, waste electricity Internet access" |
| ecoRule9.startTime | Start Time9 | HH:023 mm:059 |  | NO | String | Starting time, Format: HH:mm |
| ecoRule9.stopTime | Stop Time9 | HH:023 mm:059 |  | NO | String | Stop time, Format: HH:mm |
| ecoRule9.startDay | Start Day9 | MM:112 dd:131 |  | NO | String | Starting day, Format: MM:dd |
| ecoRule9.stopDay | Stop Day9 | MM:112 dd:131 |  | NO | String | Stop day, Format: MM:dd |
| ecoRule9.voltage | Voltage9 | 48~60 | V | NO | Number |  |
| ecoRule9.power | Power9 | 0~10000 | W | NO | Number |  |
| ecoRule9.daysOfEffectiveWeek | Effective Week9 | MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY |  | NO | Array | Week Of Use: Time Of Use Effective Week,Valuable：MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY，Multiple Choice |
| ecoRule9.soc | SOC9 | 0~100 | % | NO | Number |  |
| ecoRule10.ruleMode | ECO Mode 10 | 0:Disable  1:Charge  2:Discharge |  | NO | Number | "Economic model rules:1) Disable: No charging and discharging2) Charge: Charge the battery from the grid3) Discharge: Selling power from battery to the grid4)AC Couple:Spontaneous self-use, waste electricity Internet access" |
| ecoRule10.startTime | Start Time10 | HH:023 mm:059 |  | NO | String | Starting time, Format: HH:mm |
| ecoRule10.stopTime | Stop Time10 | HH:023 mm:059 |  | NO | String | Stop time, Format: HH:mm |
| ecoRule10.startDay | Start Day10 | MM:112 dd:131 |  | NO | String | Starting day, Format: MM:dd |
| ecoRule10.stopDay | Stop Day10 | MM:112 dd:131 |  | NO | String | Stop day, Format: MM:dd |
| ecoRule10.voltage | Voltage10 | 48~60 | V | NO | Number |  |
| ecoRule10.power | Power10 | 0~10000 | W | NO | Number |  |
| ecoRule10.daysOfEffectiveWeek | Effective Week10 | MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY |  | NO | Array | Week Of Use: Time Of Use Effective Week,Valuable：MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY，Multiple Choice |
| ecoRule10.soc | SOC10 | 0~100 | % | NO | Number |  |
| batteryModules | Battery Modules | 1~1 |  | NO | Number |  |
| batteryChargedVoltage | Battery Charged Voltage | 48~60 | V | NO | Number |  |
| batteryFloatingChargedVoltage | Bat float voltage | 48~60 | V | NO | Number |  |
| noBmsOnGridBatteryCutOffVoltage | Battery Cut-Off Voltage(On-Grid, No Bms) | 40~60 | V | NO | Number |  |
| noBmsOffGridBatteryCutOffVoltage | Battery Cut-Off Voltage(Off-Grid, No Bms) | 40~60 | V | NO | Number |  |
| noBmsOffGridBatteryRestartVoltage | Battery Restart Voltage(Off-Grid, No Bms) | 40~60 | V | NO | Number |  |
| batteryMaxChargedCurrent | Battery Max. Charged Current | 1~200 | A | NO | Number |  |
| batteryMaxDischargeCurrent | Battery Max. Discharged Current | 5~200 | A | NO | Number |  |
| --- | --- | --- | --- | --- | --- | --- |
| gridStandardCode | Standard | 0:Germany  1:Warehouse  2:50Hz grid default  3:60Hz grid default  4:Italy  5:Britain  6:Australia  7:New Zealand  8:South African  9:Netherland  10:Brazil  11:Europe  12:Poland  13:Czech |  | No | Number | Set the on-grid regulations in the current region |
| overVoltageStage1TripTime | OV Stage1 Trip Time | 0.02~1000 | Sec | No | Number |  |
| underVoltageStage1TripTime | UV Stage1 Trip Time | 0.02~1000 | Sec | No | Number |  |
| overVoltageStage2TripTime | OV Stage2 Trip Time | 0.02~1000 | Sec | No | Number |  |
| underVoltageStage2TripTime | UV Stage2 Trip Time | 0.02~1000 | Sec | No | Number |  |
| overVoltage10mTriggerValue | OV 10Min Mean Value | 230~300 | V | No | Number |  |
| overFrequencyStage1TripTime | OF Stage1 Trip Time | 0.02~1000 | Sec | No | Number |  |
| underFrequencyStage1TripTime | UF Stage1 Trip Time | 0.02~1000 | Sec | No | Number |  |
| overFrequencyStage2TripTime | OF Stage2 Trip Time | 0.02~1000 | Sec | No | Number |  |
| underFrequencyStage2TripTime | UF Stage2 Trip Time | 0.02~1000 | Sec | No | Number |  |
| onGridObservationTime | Observation Time | 1~3000 | Sec | No | Number |  |
| onGridPowerSlope | Grid Power Slope | 0~65535 | Sec | No | Number |  |
| onGridPowerLimit | Grid Power Limit | 0~100 | % | No | Number |  |
| pfPowerCurveFunctionEnable | PF-Power Curve Function | 0:Disable  1:Enable |  | No | Number |  |
| pfPowerCurvePointAPower | Point A Power | 0~100 | % | No | Number |  |
| pfPowerCurvePointAPowerFactor | Point A Power Factor | -0.99-0.8,0.81 |  | No | Number |  |
| pfPowerCurvePointBPower | Point B Power | 0~100 | % | No | Number |  |
| pfPowerCurvePointBPowerFactor | Point B Power Factor | -0.99-0.8,0.81 |  | No | Number |  |
| pfPowerCurvePointCPower | Point C Power | 0~100 | % | No | Number |  |
| pfPowerCurvePointCPowerFactor | Point C Power Factor | -0.99-0.8,0.81 |  | No | Number |  |
| pfPowerCurveLockoutPower | Lockout Power | 0~100 | % | No | Number |  |
| puCurveFunctionEnable | P(U) Curve Function | 0:Disable  1:Enable |  | No | Number |  |
| puCurvePointAActivePower | Point A  Active Power | -100~100 | % | No | Number |  |
| puCurvePointBActivePower | Point B  Active Power | -100~100 | % | No | Number |  |
| puCurvePointCActivePower | Point C  Active Power | -100~100 | % | No | Number |  |
| puCurvePointDActivePower | Point D  Active Power | -100~100 | % | No | Number |  |
| quCurveFunctionEnable | Q(U) Curve Function | 0:Disable  1:Enable |  | No | Number |  |
| quCurvePointAReactivePower | Point A  Reactive Power | -100~100 | % | No | Number |  |
| quCurvePointBReactivePower | Point B  Reactive Power | -100~100 | % | No | Number |  |
| quCurvePointCReactivePower | Point C  Reactive Power | -100~100 | % | No | Number |  |
| quCurvePointDReactivePower | Point D  Reactive Power | -100~100 | % | No | Number |  |
| quCurveLockInPower | Lock In Power | -100~100 | % | No | Number |  |
| quCurveLockOutPower | Lock Out Power | -100~100 | % | No | Number |  |
| fpCurveFunctionEnable | FP Curve Function | 0:Disable  1:Enable |  | No | Number |  |
| fpCurveOverFrequencyLowerLimit | Over Frequency Start Point | 30~80 | Hz | No | Number |  |
| fpUnderFrequencyLowerLimit | Under Frequency Start Point | 30~80 | Hz | No | Number |  |
| fpOverFrequencyUpperLimit | Over Frequency End Point | 30~80 | Hz | No | Number |  |
| fpUnderFrequencyUpperLimit | Under Frequency End Point | 30~80 | Hz | No | Number |  |
| fpRestoreFrequencyUperLimit | F(Stop) Upper | 30~80 | Hz | No | Number |  |
| fpRestoreFrequencyLowerLimit | F(Stop) Lower | 30~80 | Hz | No | Number |  |
| fpRestoreFrequencyWaitingTime | Restore Waiting Time | 1~65535 | Sec | No | Number |  |
| fpRestoreFrequencyPowerSlope | Reconnection Power Slope | 1~65535 | Sec | No | Number |  |
| fpOverFrequencyPowerSlope | Over Frequency Power Slope | 0~100 | % | No | Number |  |
| fpUnderFrequencyPowerSlope | Under Frequency Power Slope | 0~100 | % | No | Number |  |
| fpRecoveryPowerSlope | Recovery Power Slope | 0~100 | % | No | Number |  |
| fpChargeCurveFunctionEnable | FP Charge Curve Function | 0:Disable  1:Enable |  | No | Number |  |
| fpUnderFrequencyPowerSlopeForCharge | Under Frequency Power Slope For Charge | 0~100 | % | No | Number |  |
| lowVoltageRideThroughFunctionEnable | Low Voltage Ride Through | 0:Disable  1:Enable |  | No | Number |  |
| lowVoltageStartPointTripTime | Start Point Of Protection Time | 0.02~1000 | Sec | No | Number |  |
| lowVoltageEndPointTripTime | End Point Of Protection Time | 0.02~1000 | Sec | No | Number |  |
| highVoltageRideThroughFunctionEnable | High Voltage Ride Through Function | 0:Disable  1:Enable |  | No | Number |  |
| highVoltageStartPointTripTime | Start Point Of Protection Time | 0.02~1000 | Sec | No | Number |  |
| highVoltageEndPointTripTime | End Point Of Protection Time | 0.02~1000 | Sec | No | Number |  |
| overVoltageStage1TripValue | OV Stage1 Trip Value | 230~300 | V | No | Number |  |
| underVoltageStage1TripValue | UV Stage1 Trip Value | 0.1~300 | V | No | Number |  |
| overVoltageStage2TripValue | OV Stage2 Trip Value | 230~300 | V | No | Number |  |
| underVoltageStage2TripValue | UV Stage2 Trip Value | 0.1~300 | V | No | Number |  |
| overFrequencyStage1TripValue | OF Stage1 Trip Value | 30~80 | Hz | No | Number |  |
| underFrequencyStage1TripValue | UF Stage1 Trip Value | 30~80 | Hz | No | Number |  |
| overFrequencyStage2TripValue | OF Stage2 Trip Value | 30~80 | Hz | No | Number |  |
| underFrequencyStage2TripValue | UF Stage2 Trip Value | 30~80 | Hz | No | Number |  |
| pfPowerCurveLockinVoltage | Lockin Voltage | 60~300 | V | No | Number |  |
| pfPowerCurveLockoutVoltage | Lockout Voltage | 60~300 | V | No | Number |  |
| puCurvePointAVoltage | Point A Voltage | 60~300 | V | No | Number |  |
| puCurvePointBVoltage | Point B  Voltage | 60~300 | V | No | Number |  |
| puCurvePointCVoltage | Point C  Voltage | 60~300 | V | No | Number |  |
| puCurvePointDVoltage | Point D  Voltage | 60~300 | V | No | Number |  |
| quCurvePointAVoltage | Point A Voltage | 60~300 | V | No | Number |  |
| quCurvePointBVoltage | Point B  Voltage | 60~300 | V | No | Number |  |
| quCurvePointCVoltage | Point C  Voltage | 60~300 | V | No | Number |  |
| quCurvePointDVoltage | Point D  Voltage | 60~300 | V | No | Number |  |
| lowVoltageStartPointTripValue | Start Point Of Ride Through | 0~230 | V | No | Number |  |
| lowVoltageEndPointTripValue | End Point Of Ride Through | 0~230 | V | No | Number |  |
| lowVoltageCrossingTripThreshold | Low Voltage Limit Of Ride Through | 0~230 | V | No | Number |  |
| highVoltageStartPointTripValue | Start Point Of Ride Through | 230~300 | V | No | Number |  |
| highVoltageEndPointTripValue | End Point Of Ride Through | 230~300 | V | No | Number |  |
| highVoltageCrossingTripThreshold | High Voltage Limit Of Ride Through | 230~300 | V | No | Number |  |
| commOffLineEnable | CommOffLine | 0:Disable  1:Enable |  | No | Number |  |
| autoTestEnable | AutoTestEnable | 0:Disable  1:Enable |  | No | Number |  |
| deratingByVoltageEnable | DeratingByVoltage | 0:Disable  1:Enable |  | No | Number |  |
| deviceSn | 013548202500010000 |  |  | Yes | String | Device serial number |

### IVGM6048

| Key | Name | Range | unit | Required | Type | Description |
| --- | ---- | ----- | ---- | -------- | ---- | ----------- |
| acOutputRatedVoltage | AC Output Rated Voltage | 220:220V  230:230V  240:240V | V | NO | Number |  |
| acOutputRatedFrequency | AC Output Rated Frequency | 0:50Hz  1:60Hz | Hz | NO | Number |  |
| gridPowerUnbalanceEnable | Grid Power Unbalance | 0:Disable  1:Enable |  | NO | Number |  |
| powerFactor | Power Factor | -0.99-0.8,0.81 |  | NO | Number |  |
| gridWaveformDetectionMode | Detection Mode | 0:Wave Detect  1:Half Wave Detect  2:Disable Wave Detect |  | NO | Number |  |
| batteryModel | Battery Model | 0:User defined  1:Third party(Lithium battery)  2:Felicity(LPBF/LUX-X series)  3:Felicity(LPBA/LUX-Y/LUX-E  series) |  | NO | Number |  |
| batteryOnGridDischargeDepthSoc | Battery Discharged Depth(On-Grid, Bms Connected) | 10~100 | % | NO | Number | The battery SOC is lower than the battery on-grid discharge depth, and the battery stops discharging |
| batteryOffGridDischargeDepthSoc | Battery Discharged Depth(Off-Grid, Bms Connected) | 0~100 | % | NO | Number | The battery SOC is lower than the battery off-grid discharge depth, and the battery stops discharging |
| batteryOffGridRecoveryDepthSoc | Battery Restart Depth(Off-Grid, Bms Connected) | 0~100 | % | NO | Number | When the battery SOC is lower than the setting value of "Battery discharge depth (off grid)", the inverter can only be output off the grid again after the SOC recovers to the setting value higher than "Battery restart depth |
| lcdBacklightEnable | LCD Backlight | 0:Disable  1:Enable |  | NO | Number |  |
| buzzerEnable | Buzzer | 0:Disable  1:Enable |  | NO | Number |  |
| overLoadProtectionResetEnable | Over Load Protection Reset | 0:Disable  1:Enable |  | NO | Number | The fault will be cleared automatically after the overload protection of the machine. If the overload protection occurs 3 times within half an hour, the overload fault will not be cleared |
| remoteOnOffEnable | Remote control | 0:ON  1:OFF |  | NO | Number | The machine shuts down and enters standby mode |
| remoteOutputOnOffControl | AC Output ON/OFF | 0:ON  1:OFF |  | NO | Number |  |
| zeroExportFunction | Zero Export Mode | 1:To load  2:To CT |  | NO | Number | "The feed power is limited according to the setting of ""grid connection power limit"".  1) To load:  The inverter can supply power to the backup load and sell power to the grid but the selling power will not exceed the setting value of ""grid connection power limit""  2) To CT:  The inverter can supply power to the backup load, household load and sell power to the grid, but the selling power will not exceed the setting value of ""grid connection power limit"".In this mode, a CT is needed." |
| zeroExportAdjustmentPower | Zero Export Power | -500~500 | W | NO | Number | When the grid-connected power is set to 0, it is used to calibrate the sampling deviation to ensure that the inverter will not feed power to the grid |
| clearEnergyStorageLog | Clear Energy Storage Log | 1:Clear |  | NO | Number |  |
| clearEventLog | Clear Event Log | 1:Clear |  | NO | Number |  |
| factoryReset | Factory Reset | 1:Reset |  | NO | Number |  |
| eventLogFunctionEnable | Event Log Function | 0:Disable  1:Charge  2:Discharge |  | NO | Number |  |
| faultLogFunctionEnable | Fault Log Function | 0:Disable  1:Charge  2:Discharge |  | NO | Number |  |
| gfciLevel1ProtectionEnable | GFCI One-level Protection | 0:Disable  1:Charge  2:Discharge |  | NO | Number |  |
| gfciLevel2ProtectionEnable | GFCI Two-level Protection | 0:Disable  1:Charge  2:Discharge |  | NO | Number |  |
| gfciLevel3ProtectionEnable | GFCI Three-level Protection | 0:Disable  1:Charge  2:Discharge |  | NO | Number |  |
| isoDetectionEnable | ISO Detection | 0:Disable  1:Charge  2:Discharge |  | NO | Number |  |
| antiIslandingDetectionEnable | Anti-Islanding Detection | 0:Disable  1:Charge  2:Discharge |  | NO | Number |  |
| pvParallelSetting | PV Parallel Set | 0:Stand Alone  1:Parallel |  | NO | Number |  |
| fixQPencent | FixQ Pencent | -60~60 | % | NO | Number |  |
| bmsHeartbeat | BMS Heartbeat | 0:Disable  1:Charge  2:Discharge |  | NO | Number | After enabling, if the battery type is lithium battery and BMS communication fails, it will report BMS communication failure |
| operatedMode | Operated Mode | 0:General Mode  1:Backup Mode  2:Eco Mode  3:Gen Mode |  | NO | Number | "Set inverter operation mode:  1) General mode:  In this mode, the load is mainly powered by PV and battery.  2) Backup mode:  In this mode, PV gives priority to charging the battery to ensure that the battery is always full.  3) ECO mode:  In this mode, you can set a specific time to take power from the grid to charge the battery or use the power of the grid to charge the battery, and operate in general mode outside the set time.  4) Generator mode:  In this mode, the load is mainly powered by PV and battery." |
| ecoRule1.ruleMode | ECO Mode 1 | 0:Disable  1:Charge  2:Discharge   3:AC Couple |  | NO | Number | "Economic model rules:  1) Disable: No charging and discharging  2) Charge: Charge the battery from the grid  3) Discharge: Selling power from battery to the grid  4)AC Couple:Spontaneous self-use, waste electricity Internet access" |
| ecoRule1.startTime | Start Time1 | HH:023 mm:059 |  | NO | String | Starting time, Format: HH:mm |
| ecoRule1.stopTime | Stop Time1 | HH:023 mm:059 |  | NO | String | Stop time, Format: HH:mm |
| ecoRule1.startDay | Start Day1 | MM:112 dd:131 |  | NO | String | Starting day, Format: MM:dd |
| ecoRule1.stopDay | Stop Day1 | MM:112 dd:131 |  | NO | String | Stop day, Format: MM:dd |
| ecoRule1.daysOfEffectiveWeek | Effective Week1 | MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY |  | NO | Array | Week Of Use: Time Of Use Effective Week,Valuable：MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY，Multiple Choice |
| ecoRule1.soc | SOC1 | 0~100 | % | NO | Number |  |
| ecoRule1.voltage | Voltage1 | 48~60 | V | NO | Number | "1) Charging: Stop charging voltage. Battery voltage above this value stops charging (usually set to 57.6v for a single battery).  2) Discharge: Stop discharge voltage. If the battery voltage is lower than this value, it will stop discharging." |
| ecoRule1.power | Power1 | "Slave Version <203 : 06000  Slave Version ≥203 : -60006000" | W | NO | Number | "1) Charging: Battery charging power  2) Discharge: Battery discharge power  3)Dispatched power: Grid power supply or intake power" |
| ecoRule2.ruleMode | ECO Mode 2 | 0:Disable  1:Charge  2:Discharge   3:AC Couple |  | NO | Number | "Economic model rules:  1) Disable: No charging and discharging  2) Charge: Charge the battery from the grid  3) Discharge: Selling power from battery to the grid  4)AC Couple:Spontaneous self-use, waste electricity Internet access" |
| ecoRule2.startTime | Start Time2 | HH:023 mm:059 |  | NO | String | Starting time, Format: HH:mm |
| ecoRule2.stopTime | Stop Time2 | HH:023 mm:059 |  | NO | String | Stop time, Format: HH:mm |
| ecoRule2.startDay | Start Day2 | MM:112 dd:131 |  | NO | String | Starting day, Format: MM:dd |
| ecoRule2.stopDay | Stop Day2 | MM:112 dd:131 |  | NO | String | Stop day, Format: MM:dd |
| ecoRule2.voltage | Voltage2 | 48~60 | V | NO | Number | "1) Charging: Stop charging voltage. Battery voltage above this value stops charging (usually set to 57.6v for a single battery).  2) Discharge: Stop discharge voltage. If the battery voltage is lower than this value, it will stop discharging." |
| ecoRule2.power | Power2 | "Slave Version <203 : 06000  Slave Version ≥203 : -60006000" | W | NO | Number | "1) Charging: Battery charging power  2) Discharge: Battery discharge power  3)Dispatched power: Grid power supply or intake power" |
| ecoRule2.daysOfEffectiveWeek | Effective Week2 | MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY |  | NO | Array | Week Of Use: Time Of Use Effective Week,Valuable：MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY，Multiple Choice |
| ecoRule2.soc | SOC2 | 0~100 | % | NO | Number |  |
| ecoRule3.ruleMode | ECO Mode 3 | 0:Disable  1:Charge  2:Discharge   3:AC Couple |  | NO | Number | "Economic model rules:  1) Disable: No charging and discharging  2) Charge: Charge the battery from the grid  3) Discharge: Selling power from battery to the grid  4)AC Couple:Spontaneous self-use, waste electricity Internet access" |
| ecoRule3.startTime | Start Time3 | HH:023 mm:059 |  | NO | String | Starting time, Format: HH:mm |
| ecoRule3.stopTime | Stop Time3 | HH:023 mm:059 |  | NO | String | Stop time, Format: HH:mm |
| ecoRule3.startDay | Start Day3 | MM:112 dd:131 |  | NO | String | Starting day, Format: MM:dd |
| ecoRule3.stopDay | Stop Day3 | MM:112 dd:131 |  | NO | String | Stop day, Format: MM:dd |
| ecoRule3.daysOfEffectiveWeek | Effective Week3 | MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY |  | NO | Array | Week Of Use: Time Of Use Effective Week,Valuable：MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY，Multiple Choice |
| ecoRule3.soc | SOC3 | 0~100 | % | NO | Number |  |
| ecoRule3.voltage | Voltage3 | 48~60 | V | NO | Number | "1) Charging: Stop charging voltage. Battery voltage above this value stops charging (usually set to 57.6v for a single battery).  2) Discharge: Stop discharge voltage. If the battery voltage is lower than this value, it will stop discharging." |
| ecoRule3.power | Power3 | "Slave Version <203 : 06000  Slave Version ≥203 : -60006000" | W | NO | Number | "1) Charging: Battery charging power  2) Discharge: Battery discharge power  3)Dispatched power: Grid power supply or intake power" |
| ecoRule4.ruleMode | ECO Mode 4 | 0:Disable  1:Charge  2:Discharge   3:AC Couple |  | NO | Number | "Economic model rules:  1) Disable: No charging and discharging  2) Charge: Charge the battery from the grid  3) Discharge: Selling power from battery to the grid  4)AC Couple:Spontaneous self-use, waste electricity Internet access" |
| ecoRule4.startTime | Start Time4 | HH:023 mm:059 |  | NO | String | Starting time, Format: HH:mm |
| ecoRule4.stopTime | Stop Time4 | HH:023 mm:059 |  | NO | String | Stop time, Format: HH:mm |
| ecoRule4.startDay | Start Day4 | MM:112 dd:131 |  | NO | String | Starting day, Format: MM:dd |
| ecoRule4.stopDay | Stop Day4 | MM:112 dd:131 |  | NO | String | Stop day, Format: MM:dd |
| ecoRule4.voltage | Voltage4 | 48~60 | V | NO | Number | "1) Charging: Stop charging voltage. Battery voltage above this value stops charging (usually set to 57.6v for a single battery).  2) Discharge: Stop discharge voltage. If the battery voltage is lower than this value, it will stop discharging." |
| ecoRule4.power | Power4 | "Slave Version <203 : 06000  Slave Version ≥203 : -60006000" | W | NO | Number | "1) Charging: Battery charging power  2) Discharge: Battery discharge power  3)Dispatched power: Grid power supply or intake power" |
| ecoRule4.daysOfEffectiveWeek | Effective Week4 | MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY |  | NO | Array | Week Of Use: Time Of Use Effective Week,Valuable：MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY，Multiple Choice |
| ecoRule4.soc | SOC4 | 0~100 | % | NO | Number |  |
| additionalEcoEnable | ECO 10 enable | 0:Disable  1:Enable |  | NO | Number | Only when Master Version ≥ 2204，parameter can be used, ecoRule5 ~ecoRule10 also.After enabling, there will be 10 economic rules that can be set.Only trial on some devices. If there is no value displayed or it cannot run, please use the old 4-segment mode. |
| ecoRule5.ruleMode | ECO Mode 5 | 0:Disable  1:Charge  2:Discharge |  | NO | Number | "Economic model rules:  1) Disable: No charging and discharging  2) Charge: Charge the battery from the grid  3) Discharge: Selling power from battery to the grid  4)AC Couple:Spontaneous self-use, waste electricity Internet access" |
| ecoRule5.startTime | Start Time5 | HH:023 mm:059 |  | NO | String | Starting time, Format: HH:mm |
| ecoRule5.stopTime | Stop Time5 | HH:023 mm:059 |  | NO | String | Stop time, Format: HH:mm |
| ecoRule5.startDay | Start Day5 | MM:112 dd:131 |  | NO | String | Starting day, Format: MM:dd |
| ecoRule5.stopDay | Stop Day5 | MM:112 dd:131 |  | NO | String | Stop day, Format: MM:dd |
| ecoRule5.voltage | Voltage5 | 48~60 | V | NO | Number |  |
| ecoRule5.power | Power5 | 0~5000 | W | NO | Number |  |
| ecoRule5.daysOfEffectiveWeek | Effective Week5 | MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY |  | NO | Array | Week Of Use: Time Of Use Effective Week,Valuable：MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY，Multiple Choice |
| ecoRule5.soc | SOC5 | 0~100 | % | NO | Number |  |
| ecoRule6.ruleMode | ECO Mode 6 | 0:Disable  1:Charge  2:Discharge |  | NO | Number | "Economic model rules:  1) Disable: No charging and discharging  2) Charge: Charge the battery from the grid  3) Discharge: Selling power from battery to the grid  4)AC Couple:Spontaneous self-use, waste electricity Internet access" |
| ecoRule6.startTime | Start Time6 | HH:023 mm:059 |  | NO | String | Starting time, Format: HH:mm |
| ecoRule6.stopTime | Stop Time6 | HH:023 mm:059 |  | NO | String | Stop time, Format: HH:mm |
| ecoRule6.startDay | Start Day6 | MM:112 dd:131 |  | NO | String | Starting day, Format: MM:dd |
| ecoRule6.stopDay | Stop Day6 | MM:112 dd:131 |  | NO | String | Stop day, Format: MM:dd |
| ecoRule6.voltage | Voltage6 | 48~60 | V | NO | Number |  |
| ecoRule6.power | Power6 | 0~5000 | W | NO | Number |  |
| ecoRule6.daysOfEffectiveWeek | Effective Week6 | MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY |  | NO | Array | Week Of Use: Time Of Use Effective Week,Valuable：MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY，Multiple Choice |
| ecoRule6.soc | SOC6 | 0~100 | % | NO | Number |  |
| ecoRule7.ruleMode | ECO Mode 7 | 0:Disable  1:Charge  2:Discharge |  | NO | Number | "Economic model rules:  1) Disable: No charging and discharging  2) Charge: Charge the battery from the grid  3) Discharge: Selling power from battery to the grid  4)AC Couple:Spontaneous self-use, waste electricity Internet access" |
| ecoRule7.startTime | Start Time7 | HH:023 mm:059 |  | NO | String | Starting time, Format: HH:mm |
| ecoRule7.stopTime | Stop Time7 | HH:023 mm:059 |  | NO | String | Stop time, Format: HH:mm |
| ecoRule7.startDay | Start Day7 | MM:112 dd:131 |  | NO | String | Starting day, Format: MM:dd |
| ecoRule7.stopDay | Stop Day7 | MM:112 dd:131 |  | NO | String | Stop day, Format: MM:dd |
| ecoRule7.voltage | Voltage7 | 48~60 | V | NO | Number |  |
| ecoRule7.power | Power7 | 0~5000 | W | NO | Number |  |
| ecoRule7.daysOfEffectiveWeek | Effective Week7 | MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY |  | NO | Array | Week Of Use: Time Of Use Effective Week,Valuable：MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY，Multiple Choice |
| ecoRule7.soc | SOC7 | 0~100 | % | NO | Number |  |
| ecoRule8.ruleMode | ECO Mode 8 | 0:Disable  1:Charge  2:Discharge |  | NO | Number | "Economic model rules:  1) Disable: No charging and discharging  2) Charge: Charge the battery from the grid  3) Discharge: Selling power from battery to the grid  4)AC Couple:Spontaneous self-use, waste electricity Internet access" |
| ecoRule8.startTime | Start Time8 | HH:023 mm:059 |  | NO | String | Starting time, Format: HH:mm |
| ecoRule8.stopTime | Stop Time8 | HH:023 mm:059 |  | NO | String | Stop time, Format: HH:mm |
| ecoRule8.startDay | Start Day8 | MM:112 dd:131 |  | NO | String | Starting day, Format: MM:dd |
| ecoRule8.stopDay | Stop Day8 | MM:112 dd:131 |  | NO | String | Stop day, Format: MM:dd |
| ecoRule8.voltage | Voltage8 | 48~60 | V | NO | Number |  |
| ecoRule8.power | Power8 | 0~5000 | W | NO | Number |  |
| ecoRule8.daysOfEffectiveWeek | Effective Week8 | MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY |  | NO | Array | Week Of Use: Time Of Use Effective Week,Valuable：MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY，Multiple Choice |
| ecoRule8.soc | SOC8 | 0~100 | % | NO | Number |  |
| ecoRule9.ruleMode | ECO Mode 9 | 0:Disable  1:Charge  2:Discharge |  | NO | Number | "Economic model rules:  1) Disable: No charging and discharging  2) Charge: Charge the battery from the grid  3) Discharge: Selling power from battery to the grid  4)AC Couple:Spontaneous self-use, waste electricity Internet access" |
| ecoRule9.startTime | Start Time9 | HH:023 mm:059 |  | NO | String | Starting time, Format: HH:mm |
| ecoRule9.stopTime | Stop Time9 | HH:023 mm:059 |  | NO | String | Stop time, Format: HH:mm |
| ecoRule9.startDay | Start Day9 | MM:112 dd:131 |  | NO | String | Starting day, Format: MM:dd |
| ecoRule9.stopDay | Stop Day9 | MM:112 dd:131 |  | NO | String | Stop day, Format: MM:dd |
| ecoRule9.voltage | Voltage9 | 48~60 | V | NO | Number |  |
| ecoRule9.power | Power9 | 0~5000 | W | NO | Number |  |
| ecoRule9.daysOfEffectiveWeek | Effective Week9 | MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY |  | NO | Array | Week Of Use: Time Of Use Effective Week,Valuable：MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY，Multiple Choice |
| ecoRule9.soc | SOC9 | 0~100 | % | NO | Number |  |
| ecoRule10.ruleMode | ECO Mode 10 | 0:Disable  1:Charge  2:Discharge |  | NO | Number | "Economic model rules:  1) Disable: No charging and discharging  2) Charge: Charge the battery from the grid  3) Discharge: Selling power from battery to the grid  4)AC Couple:Spontaneous self-use, waste electricity Internet access" |
| ecoRule10.startTime | Start Time10 | HH:023 mm:059 |  | NO | String | Starting time, Format: HH:mm |
| ecoRule10.stopTime | Stop Time10 | HH:023 mm:059 |  | NO | String | Stop time, Format: HH:mm |
| ecoRule10.startDay | Start Day10 | MM:112 dd:131 |  | NO | String | Starting day, Format: MM:dd |
| ecoRule10.stopDay | Stop Day10 | MM:112 dd:131 |  | NO | String | Stop day, Format: MM:dd |
| ecoRule10.voltage | Voltage10 | 48~60 | V | NO | Number |  |
| ecoRule10.power | Power10 | 0~5000 | W | NO | Number |  |
| ecoRule10.daysOfEffectiveWeek | Effective Week10 | MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY |  | NO | Array | Week Of Use: Time Of Use Effective Week,Valuable：MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY，Multiple Choice |
| ecoRule10.soc | SOC10 | 0~100 | % | NO | Number |  |
| batteryModules | Battery Modules | 1~1 |  | NO | Number |  |
| batteryChargedVoltage | Battery Charged Voltage | 48~60 | V | NO | Number |  |
| batteryFloatingChargedVoltage | Bat float voltage | 48~60 | V | NO | Number |  |
| noBmsOnGridBatteryCutOffVoltage | Battery Cut-Off Voltage(On-Grid, No Bms) | 40~60 | V | NO | Number |  |
| noBmsOffGridBatteryCutOffVoltage | Battery Cut-Off Voltage(Off-Grid, No Bms) | 40~60 | V | NO | Number |  |
| noBmsOffGridBatteryRestartVoltage | Battery Restart Voltage(Off-Grid, No Bms) | 40~60 | V | NO | Number |  |
| batteryMaxChargedCurrent | Battery Max. Charged Current | 1~100 | A | NO | Number |  |
| batteryMaxDischargeCurrent | Battery Max. Discharged Current | 5~100 | A | NO | Number |  |
| parallelEnable | Parallel Enable | 0:Stand-Alone  1:Single Phase Parallel  2:Triphase Parallel-L1  3:Triphase Parallel-L2  4:Triphase Parallel-L3 |  | NO | Number | "Ensure that the inverter is operating in standby mode before setting it,Otherwise, it will cause machine malfunction." |
| --- | --- | --- | --- | --- | --- | --- |
| gridStandardCode | Standard | 0:Germany  1:Warehouse  2:50Hz grid default  3:60Hz grid default  4:Italy  5:Britain  6:Australia  7:New Zealand  8:South African  9:Netherland  10:Brazil  11:Europe  12:Poland  13:Czech |  | No | Number | Set the on-grid regulations in the current region |
| overVoltageStage1TripTime | OV Stage1 Trip Time | 0.02~1000 | Sec | No | Number |  |
| underVoltageStage1TripTime | UV Stage1 Trip Time | 0.02~1000 | Sec | No | Number |  |
| overVoltageStage2TripTime | OV Stage2 Trip Time | 0.02~1000 | Sec | No | Number |  |
| underVoltageStage2TripTime | UV Stage2 Trip Time | 0.02~1000 | Sec | No | Number |  |
| overVoltage10mTriggerValue | OV 10Min Mean Value | 230~300 | V | No | Number |  |
| overFrequencyStage1TripTime | OF Stage1 Trip Time | 0.02~1000 | Sec | No | Number |  |
| underFrequencyStage1TripTime | UF Stage1 Trip Time | 0.02~1000 | Sec | No | Number |  |
| overFrequencyStage2TripTime | OF Stage2 Trip Time | 0.02~1000 | Sec | No | Number |  |
| underFrequencyStage2TripTime | UF Stage2 Trip Time | 0.02~1000 | Sec | No | Number |  |
| onGridObservationTime | Observation Time | 1~3000 | Sec | No | Number |  |
| onGridPowerSlope | Grid Power Slope | 0~65535 | Sec | No | Number |  |
| onGridPowerLimit | Grid Power Limit | 0~100 | % | No | Number |  |
| pfPowerCurveFunctionEnable | PF-Power Curve Function | 0:Disable  1:Enable |  | No | Number |  |
| pfPowerCurvePointAPower | Point A Power | 0~100 | % | No | Number |  |
| pfPowerCurvePointAPowerFactor | Point A Power Factor | -0.99-0.8,0.81 |  | No | Number |  |
| pfPowerCurvePointBPower | Point B Power | 0~100 | % | No | Number |  |
| pfPowerCurvePointBPowerFactor | Point B Power Factor | -0.99-0.8,0.81 |  | No | Number |  |
| pfPowerCurvePointCPower | Point C Power | 0~100 | % | No | Number |  |
| pfPowerCurvePointCPowerFactor | Point C Power Factor | -0.99-0.8,0.81 |  | No | Number |  |
| pfPowerCurveLockoutPower | Lockout Power | 0~100 | % | No | Number |  |
| puCurveFunctionEnable | P(U) Curve Function | 0:Disable  1:Enable |  | No | Number |  |
| puCurvePointAActivePower | Point A  Active Power | -100~100 | % | No | Number |  |
| puCurvePointBActivePower | Point B  Active Power | -100~100 | % | No | Number |  |
| puCurvePointCActivePower | Point C  Active Power | -100~100 | % | No | Number |  |
| puCurvePointDActivePower | Point D  Active Power | -100~100 | % | No | Number |  |
| quCurveFunctionEnable | Q(U) Curve Function | 0:Disable  1:Enable |  | No | Number |  |
| quCurvePointAReactivePower | Point A  Reactive Power | -100~100 | % | No | Number |  |
| quCurvePointBReactivePower | Point B  Reactive Power | -100~100 | % | No | Number |  |
| quCurvePointCReactivePower | Point C  Reactive Power | -100~100 | % | No | Number |  |
| quCurvePointDReactivePower | Point D  Reactive Power | -100~100 | % | No | Number |  |
| quCurveLockInPower | Lock In Power | -100~100 | % | No | Number |  |
| quCurveLockOutPower | Lock Out Power | -100~100 | % | No | Number |  |
| fpCurveFunctionEnable | FP Curve Function | 0:Disable  1:Enable |  | No | Number |  |
| fpCurveOverFrequencyLowerLimit | Over Frequency Start Point | 30~80 | Hz | No | Number |  |
| fpUnderFrequencyLowerLimit | Under Frequency Start Point | 30~80 | Hz | No | Number |  |
| fpOverFrequencyUpperLimit | Over Frequency End Point | 30~80 | Hz | No | Number |  |
| fpUnderFrequencyUpperLimit | Under Frequency End Point | 30~80 | Hz | No | Number |  |
| fpRestoreFrequencyUperLimit | F(Stop) Upper | 30~80 | Hz | No | Number |  |
| fpRestoreFrequencyLowerLimit | F(Stop) Lower | 30~80 | Hz | No | Number |  |
| fpRestoreFrequencyWaitingTime | Restore Waiting Time | 1~65535 | Sec | No | Number |  |
| fpRestoreFrequencyPowerSlope | Reconnection Power Slope | 1~65535 | Sec | No | Number |  |
| fpOverFrequencyPowerSlope | Over Frequency Power Slope | 0~100 | % | No | Number |  |
| fpUnderFrequencyPowerSlope | Under Frequency Power Slope | 0~100 | % | No | Number |  |
| fpRecoveryPowerSlope | Recovery Power Slope | 0~100 | % | No | Number |  |
| fpChargeCurveFunctionEnable | FP Charge Curve Function | 0:Disable  1:Enable |  | No | Number |  |
| fpUnderFrequencyPowerSlopeForCharge | Under Frequency Power Slope For Charge | 0~100 | % | No | Number |  |
| lowVoltageRideThroughFunctionEnable | Low Voltage Ride Through | 0:Disable  1:Enable |  | No | Number |  |
| lowVoltageStartPointTripTime | Start Point Of Protection Time | 0.02~1000 | Sec | No | Number |  |
| lowVoltageEndPointTripTime | End Point Of Protection Time | 0.02~1000 | Sec | No | Number |  |
| highVoltageRideThroughFunctionEnable | High Voltage Ride Through Function | 0:Disable  1:Enable |  | No | Number |  |
| highVoltageStartPointTripTime | Start Point Of Protection Time | 0.02~1000 | Sec | No | Number |  |
| highVoltageEndPointTripTime | End Point Of Protection Time | 0.02~1000 | Sec | No | Number |  |
| overVoltageStage1TripValue | OV Stage1 Trip Value | 230~300 | V | No | Number |  |
| underVoltageStage1TripValue | UV Stage1 Trip Value | 0.1~300 | V | No | Number |  |
| overVoltageStage2TripValue | OV Stage2 Trip Value | 230~300 | V | No | Number |  |
| underVoltageStage2TripValue | UV Stage2 Trip Value | 0.1~300 | V | No | Number |  |
| overFrequencyStage1TripValue | OF Stage1 Trip Value | 30~80 | Hz | No | Number |  |
| underFrequencyStage1TripValue | UF Stage1 Trip Value | 30~80 | Hz | No | Number |  |
| overFrequencyStage2TripValue | OF Stage2 Trip Value | 30~80 | Hz | No | Number |  |
| underFrequencyStage2TripValue | UF Stage2 Trip Value | 30~80 | Hz | No | Number |  |
| pfPowerCurveLockinVoltage | Lockin Voltage | 60~300 | V | No | Number |  |
| pfPowerCurveLockoutVoltage | Lockout Voltage | 60~300 | V | No | Number |  |
| puCurvePointAVoltage | Point A Voltage | 60~300 | V | No | Number |  |
| puCurvePointBVoltage | Point B  Voltage | 60~300 | V | No | Number |  |
| puCurvePointCVoltage | Point C  Voltage | 60~300 | V | No | Number |  |
| puCurvePointDVoltage | Point D  Voltage | 60~300 | V | No | Number |  |
| quCurvePointAVoltage | Point A Voltage | 60~300 | V | No | Number |  |
| quCurvePointBVoltage | Point B  Voltage | 60~300 | V | No | Number |  |
| quCurvePointCVoltage | Point C  Voltage | 60~300 | V | No | Number |  |
| quCurvePointDVoltage | Point D  Voltage | 60~300 | V | No | Number |  |
| lowVoltageStartPointTripValue | Start Point Of Ride Through | 0~230 | V | No | Number |  |
| lowVoltageEndPointTripValue | End Point Of Ride Through | 0~230 | V | No | Number |  |
| lowVoltageCrossingTripThreshold | Low Voltage Limit Of Ride Through | 0~230 | V | No | Number |  |
| highVoltageStartPointTripValue | Start Point Of Ride Through | 230~300 | V | No | Number |  |
| highVoltageEndPointTripValue | End Point Of Ride Through | 230~300 | V | No | Number |  |
| highVoltageCrossingTripThreshold | High Voltage Limit Of Ride Through | 230~300 | V | No | Number |  |
| commOffLineEnable | CommOffLine | 0:Disable  1:Enable |  | No | Number |  |
| autoTestEnable | AutoTestEnable | 0:Disable  1:Enable |  | No | Number |  |
| deratingByVoltageEnable | DeratingByVoltage | 0:Disable  1:Enable |  | No | Number |  |
| deviceSn | 013548202500010000 |  |  | Yes | String | Device serial number |

### IVGM5048

| Key | Name | Range | unit | Required | Type | Description |
| --- | ---- | ----- | ---- | -------- | ---- | ----------- |
| acOutputRatedVoltage | AC Output Rated Voltage | 220:220V  230:230V  240:240V | V | NO | Number |  |
| acOutputRatedFrequency | AC Output Rated Frequency | 0:50Hz  1:60Hz | Hz | NO | Number |  |
| gridPowerUnbalanceEnable | Grid Power Unbalance | 0:Disable  1:Enable |  | NO | Number |  |
| powerFactor | Power Factor | -0.99-0.8,0.81 |  | NO | Number |  |
| gridWaveformDetectionMode | Detection Mode | 0:Wave Detect  1:Half Wave Detect  2:Disable Wave Detect |  | NO | Number |  |
| batteryModel | Battery Model | 0:User defined  1:Third party(Lithium battery)  2:Felicity(LPBF/LUX-X series)  3:Felicity(LPBA/LUX-Y/LUX-E  series) |  | NO | Number |  |
| batteryOnGridDischargeDepthSoc | Battery Discharged Depth(On-Grid, Bms Connected) | 10~100 | % | NO | Number | The battery SOC is lower than the battery on-grid discharge depth, and the battery stops discharging |
| batteryOffGridDischargeDepthSoc | Battery Discharged Depth(Off-Grid, Bms Connected) | 0~100 | % | NO | Number | The battery SOC is lower than the battery off-grid discharge depth, and the battery stops discharging |
| batteryOffGridRecoveryDepthSoc | Battery Restart Depth(Off-Grid, Bms Connected) | 0~100 | % | NO | Number | When the battery SOC is lower than the setting value of "Battery discharge depth (off grid)", the inverter can only be output off the grid again after the SOC recovers to the setting value higher than "Battery restart depth |
| lcdBacklightEnable | LCD Backlight | 0:Disable  1:Enable |  | NO | Number |  |
| buzzerEnable | Buzzer | 0:Disable  1:Enable |  | NO | Number |  |
| overLoadProtectionResetEnable | Over Load Protection Reset | 0:Disable  1:Enable |  | NO | Number | The fault will be cleared automatically after the overload protection of the machine. If the overload protection occurs 3 times within half an hour, the overload fault will not be cleared |
| remoteOnOffEnable | Remote control | 0:ON  1:OFF |  | NO | Number | The machine shuts down and enters standby mode |
| remoteOutputOnOffControl | AC Output ON/OFF | 0:ON  1:OFF |  | NO | Number |  |
| zeroExportFunction | Zero Export Mode | 1:To load  2:To CT |  | NO | Number | "The feed power is limited according to the setting of ""grid connection power limit"".  1) To load:  The inverter can supply power to the backup load and sell power to the grid but the selling power will not exceed the setting value of ""grid connection power limit""  2) To CT:  The inverter can supply power to the backup load, household load and sell power to the grid, but the selling power will not exceed the setting value of ""grid connection power limit"".In this mode, a CT is needed." |
| zeroExportAdjustmentPower | Zero Export Power | -500~500 | W | NO | Number | When the grid-connected power is set to 0, it is used to calibrate the sampling deviation to ensure that the inverter will not feed power to the grid |
| clearEnergyStorageLog | Clear Energy Storage Log | 1:Clear |  | NO | Number |  |
| clearEventLog | Clear Event Log | 1:Clear |  | NO | Number |  |
| factoryReset | Factory Reset | 1:Reset |  | NO | Number |  |
| eventLogFunctionEnable | Event Log Function | 0:Disable  1:Charge  2:Discharge |  | NO | Number |  |
| faultLogFunctionEnable | Fault Log Function | 0:Disable  1:Charge  2:Discharge |  | NO | Number |  |
| gfciLevel1ProtectionEnable | GFCI One-level Protection | 0:Disable  1:Charge  2:Discharge |  | NO | Number |  |
| gfciLevel2ProtectionEnable | GFCI Two-level Protection | 0:Disable  1:Charge  2:Discharge |  | NO | Number |  |
| gfciLevel3ProtectionEnable | GFCI Three-level Protection | 0:Disable  1:Charge  2:Discharge |  | NO | Number |  |
| isoDetectionEnable | ISO Detection | 0:Disable  1:Charge  2:Discharge |  | NO | Number |  |
| antiIslandingDetectionEnable | Anti-Islanding Detection | 0:Disable  1:Charge  2:Discharge |  | NO | Number |  |
| pvParallelSetting | PV Parallel Set | 0:Stand Alone  1:Parallel |  | NO | Number |  |
| fixQPencent | FixQ Pencent | -60~60 | % | NO | Number |  |
| bmsHeartbeat | BMS Heartbeat | 0:Disable  1:Charge  2:Discharge |  | NO | Number | After enabling, if the battery type is lithium battery and BMS communication fails, it will report BMS communication failure |
| operatedMode | Operated Mode | 0:General Mode  1:Backup Mode  2:Eco Mode  3:Gen Mode |  | NO | Number | "Set inverter operation mode:  1) General mode:  In this mode, the load is mainly powered by PV and battery.  2) Backup mode:  In this mode, PV gives priority to charging the battery to ensure that the battery is always full.  3) ECO mode:  In this mode, you can set a specific time to take power from the grid to charge the battery or use the power of the grid to charge the battery, and operate in general mode outside the set time.  4) Generator mode:  In this mode, the load is mainly powered by PV and battery." |
| ecoRule1.ruleMode | ECO Mode 1 | 0:Disable  1:Charge  2:Discharge   3:AC Couple |  | NO | Number | "Economic model rules:  1) Disable: No charging and discharging  2) Charge: Charge the battery from the grid  3) Discharge: Selling power from battery to the grid  4)AC Couple:Spontaneous self-use, waste electricity Internet access" |
| ecoRule1.startTime | Start Time1 | HH:023 mm:059 |  | NO | String | Starting time, Format: HH:mm |
| ecoRule1.stopTime | Stop Time1 | HH:023 mm:059 |  | NO | String | Stop time, Format: HH:mm |
| ecoRule1.startDay | Start Day1 | MM:112 dd:131 |  | NO | String | Starting day, Format: MM:dd |
| ecoRule1.stopDay | Stop Day1 | MM:112 dd:131 |  | NO | String | Stop day, Format: MM:dd |
| ecoRule1.daysOfEffectiveWeek | Effective Week1 | MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY |  | NO | Array | Week Of Use: Time Of Use Effective Week,Valuable：MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY，Multiple Choice |
| ecoRule1.soc | SOC1 | 0~100 | % | NO | Number |  |
| ecoRule1.voltage | Voltage1 | 48~60 | V | NO | Number | "1) Charging: Stop charging voltage. Battery voltage above this value stops charging (usually set to 57.6v for a single battery).  2) Discharge: Stop discharge voltage. If the battery voltage is lower than this value, it will stop discharging." |
| ecoRule1.power | Power1 | "Slave Version <203 : 05000  Slave Version ≥203 : -50005000" | W | NO | Number | "1) Charging: Battery charging power  2) Discharge: Battery discharge power  3)Dispatched power: Grid power supply or intake power" |
| ecoRule2.ruleMode | ECO Mode 2 | 0:Disable  1:Charge  2:Discharge   3:AC Couple |  | NO | Number | "Economic model rules:  1) Disable: No charging and discharging  2) Charge: Charge the battery from the grid  3) Discharge: Selling power from battery to the grid  4)AC Couple:Spontaneous self-use, waste electricity Internet access" |
| ecoRule2.startTime | Start Time2 | HH:023 mm:059 |  | NO | String | Starting time, Format: HH:mm |
| ecoRule2.stopTime | Stop Time2 | HH:023 mm:059 |  | NO | String | Stop time, Format: HH:mm |
| ecoRule2.startDay | Start Day2 | MM:112 dd:131 |  | NO | String | Starting day, Format: MM:dd |
| ecoRule2.stopDay | Stop Day2 | MM:112 dd:131 |  | NO | String | Stop day, Format: MM:dd |
| ecoRule2.voltage | Voltage2 | 48~60 | V | NO | Number | "1) Charging: Stop charging voltage. Battery voltage above this value stops charging (usually set to 57.6v for a single battery).  2) Discharge: Stop discharge voltage. If the battery voltage is lower than this value, it will stop discharging." |
| ecoRule2.power | Power2 | "Slave Version <203 : 0~5000 |  |  |  |  |
| Slave Version ≥203 : -5000~5000" | W | NO | Number | "1) Charging: Battery charging power  2) Discharge: Battery discharge power  3)Dispatched power: Grid power supply or intake power" |  |  |
| ecoRule2.daysOfEffectiveWeek | Effective Week2 | MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY |  | NO | Array | Week Of Use: Time Of Use Effective Week,Valuable：MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY，Multiple Choice |
| ecoRule2.soc | SOC2 | 0~100 | % | NO | Number |  |
| ecoRule3.ruleMode | ECO Mode 3 | 0:Disable  1:Charge  2:Discharge   3:AC Couple |  | NO | Number | "Economic model rules:  1) Disable: No charging and discharging  2) Charge: Charge the battery from the grid  3) Discharge: Selling power from battery to the grid  4)AC Couple:Spontaneous self-use, waste electricity Internet access" |
| ecoRule3.startTime | Start Time3 | HH:023 mm:059 |  | NO | String | Starting time, Format: HH:mm |
| ecoRule3.stopTime | Stop Time3 | HH:023 mm:059 |  | NO | String | Stop time, Format: HH:mm |
| ecoRule3.startDay | Start Day3 | MM:112 dd:131 |  | NO | String | Starting day, Format: MM:dd |
| ecoRule3.stopDay | Stop Day3 | MM:112 dd:131 |  | NO | String | Stop day, Format: MM:dd |
| ecoRule3.daysOfEffectiveWeek | Effective Week3 | MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY |  | NO | Array | Week Of Use: Time Of Use Effective Week,Valuable：MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY，Multiple Choice |
| ecoRule3.soc | SOC3 | 0~100 | % | NO | Number |  |
| ecoRule3.voltage | Voltage3 | 48~60 | V | NO | Number | "1) Charging: Stop charging voltage. Battery voltage above this value stops charging (usually set to 57.6v for a single battery).  2) Discharge: Stop discharge voltage. If the battery voltage is lower than this value, it will stop discharging." |
| ecoRule3.power | Power3 | "Slave Version <203 : 05000  Slave Version ≥203 : -50005000" | W | NO | Number | "1) Charging: Battery charging power  2) Discharge: Battery discharge power |
| 3)Dispatched power: Grid power supply or intake power" |  |  |  |  |  |  |
| ecoRule4.ruleMode | ECO Mode 4 | 0:Disable  1:Charge  2:Discharge   3:AC Couple |  | NO | Number | "Economic model rules:  1) Disable: No charging and discharging  2) Charge: Charge the battery from the grid  3) Discharge: Selling power from battery to the grid  4)AC Couple:Spontaneous self-use, waste electricity Internet access" |
| ecoRule4.startTime | Start Time4 | HH:023 mm:059 |  | NO | String | Starting time, Format: HH:mm |
| ecoRule4.stopTime | Stop Time4 | HH:023 mm:059 |  | NO | String | Stop time, Format: HH:mm |
| ecoRule4.startDay | Start Day4 | MM:112 dd:131 |  | NO | String | Starting day, Format: MM:dd |
| ecoRule4.stopDay | Stop Day4 | MM:112 dd:131 |  | NO | String | Stop day, Format: MM:dd |
| ecoRule4.voltage | Voltage4 | 48~60 | V | NO | Number | "1) Charging: Stop charging voltage. Battery voltage above this value stops charging (usually set to 57.6v for a single battery).  2) Discharge: Stop discharge voltage. If the battery voltage is lower than this value, it will stop discharging." |
| ecoRule4.power | Power4 | "Slave Version <203 : 05000  Slave Version ≥203 : -50005000" | W | NO | Number | "1) Charging: Battery charging power  2) Discharge: Battery discharge power  3)Dispatched power: Grid power supply or intake power" |
| ecoRule4.daysOfEffectiveWeek | Effective Week4 | MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY |  | NO | Array | Week Of Use: Time Of Use Effective Week,Valuable：MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY，Multiple Choice |
| ecoRule4.soc | SOC4 | 0~100 | % | NO | Number |  |
| additionalEcoEnable | ECO 10 enable | 0:Disable  1:Enable |  | NO | Number | Only when Master Version ≥ 2204，parameter can be used, ecoRule5 ~ecoRule10 also.After enabling, there will be 10 economic rules that can be set.Only trial on some devices. If there is no value displayed or it cannot run, please use the old 4-segment mode. |
| ecoRule5.ruleMode | ECO Mode 5 | 0:Disable  1:Charge  2:Discharge |  | NO | Number | "Economic model rules:  1) Disable: No charging and discharging  2) Charge: Charge the battery from the grid  3) Discharge: Selling power from battery to the grid  4)AC Couple:Spontaneous self-use, waste electricity Internet access" |
| ecoRule5.startTime | Start Time5 | HH:023 mm:059 |  | NO | String | Starting time, Format: HH:mm |
| ecoRule5.stopTime | Stop Time5 | HH:023 mm:059 |  | NO | String | Stop time, Format: HH:mm |
| ecoRule5.startDay | Start Day5 | MM:112 dd:131 |  | NO | String | Starting day, Format: MM:dd |
| ecoRule5.stopDay | Stop Day5 | MM:112 dd:131 |  | NO | String | Stop day, Format: MM:dd |
| ecoRule5.voltage | Voltage5 | 48~60 | V | NO | Number |  |
| ecoRule5.power | Power5 | 0~5000 | W | NO | Number |  |
| ecoRule5.daysOfEffectiveWeek | Effective Week5 | MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY |  | NO | Array | Week Of Use: Time Of Use Effective Week,Valuable：MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY，Multiple Choice |
| ecoRule5.soc | SOC5 | 0~100 | % | NO | Number |  |
| ecoRule6.ruleMode | ECO Mode 6 | 0:Disable  1:Charge  2:Discharge |  | NO | Number | "Economic model rules:  1) Disable: No charging and discharging  2) Charge: Charge the battery from the grid  3) Discharge: Selling power from battery to the grid  4)AC Couple:Spontaneous self-use, waste electricity Internet access" |
| ecoRule6.startTime | Start Time6 | HH:023 mm:059 |  | NO | String | Starting time, Format: HH:mm |
| ecoRule6.stopTime | Stop Time6 | HH:023 mm:059 |  | NO | String | Stop time, Format: HH:mm |
| ecoRule6.startDay | Start Day6 | MM:112 dd:131 |  | NO | String | Starting day, Format: MM:dd |
| ecoRule6.stopDay | Stop Day6 | MM:112 dd:131 |  | NO | String | Stop day, Format: MM:dd |
| ecoRule6.voltage | Voltage6 | 48~60 | V | NO | Number |  |
| ecoRule6.power | Power6 | 0~5000 | W | NO | Number |  |
| ecoRule6.daysOfEffectiveWeek | Effective Week6 | MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY |  | NO | Array | Week Of Use: Time Of Use Effective Week,Valuable：MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY，Multiple Choice |
| ecoRule6.soc | SOC6 | 0~100 | % | NO | Number |  |
| ecoRule7.ruleMode | ECO Mode 7 | 0:Disable  1:Charge  2:Discharge |  | NO | Number | "Economic model rules:  1) Disable: No charging and discharging  2) Charge: Charge the battery from the grid  3) Discharge: Selling power from battery to the grid  4)AC Couple:Spontaneous self-use, waste electricity Internet access" |
| ecoRule7.startTime | Start Time7 | HH:023 mm:059 |  | NO | String | Starting time, Format: HH:mm |
| ecoRule7.stopTime | Stop Time7 | HH:023 mm:059 |  | NO | String | Stop time, Format: HH:mm |
| ecoRule7.startDay | Start Day7 | MM:112 dd:131 |  | NO | String | Starting day, Format: MM:dd |
| ecoRule7.stopDay | Stop Day7 | MM:112 dd:131 |  | NO | String | Stop day, Format: MM:dd |
| ecoRule7.voltage | Voltage7 | 48~60 | V | NO | Number |  |
| ecoRule7.power | Power7 | 0~5000 | W | NO | Number |  |
| ecoRule7.daysOfEffectiveWeek | Effective Week7 | MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY |  | NO | Array | Week Of Use: Time Of Use Effective Week,Valuable：MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY，Multiple Choice |
| ecoRule7.soc | SOC7 | 0~100 | % | NO | Number |  |
| ecoRule8.ruleMode | ECO Mode 8 | 0:Disable  1:Charge  2:Discharge |  | NO | Number | "Economic model rules:  1) Disable: No charging and discharging  2) Charge: Charge the battery from the grid  3) Discharge: Selling power from battery to the grid  4)AC Couple:Spontaneous self-use, waste electricity Internet access" |
| ecoRule8.startTime | Start Time8 | HH:023 mm:059 |  | NO | String | Starting time, Format: HH:mm |
| ecoRule8.stopTime | Stop Time8 | HH:023 mm:059 |  | NO | String | Stop time, Format: HH:mm |
| ecoRule8.startDay | Start Day8 | MM:112 dd:131 |  | NO | String | Starting day, Format: MM:dd |
| ecoRule8.stopDay | Stop Day8 | MM:112 dd:131 |  | NO | String | Stop day, Format: MM:dd |
| ecoRule8.voltage | Voltage8 | 48~60 | V | NO | Number |  |
| ecoRule8.power | Power8 | 0~5000 | W | NO | Number |  |
| ecoRule8.daysOfEffectiveWeek | Effective Week8 | MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY |  | NO | Array | Week Of Use: Time Of Use Effective Week,Valuable：MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY，Multiple Choice |
| ecoRule8.soc | SOC8 | 0~100 | % | NO | Number |  |
| ecoRule9.ruleMode | ECO Mode 9 | 0:Disable  1:Charge  2:Discharge |  | NO | Number | "Economic model rules:  1) Disable: No charging and discharging  2) Charge: Charge the battery from the grid  3) Discharge: Selling power from battery to the grid  4)AC Couple:Spontaneous self-use, waste electricity Internet access" |
| ecoRule9.startTime | Start Time9 | HH:023 mm:059 |  | NO | String | Starting time, Format: HH:mm |
| ecoRule9.stopTime | Stop Time9 | HH:023 mm:059 |  | NO | String | Stop time, Format: HH:mm |
| ecoRule9.startDay | Start Day9 | MM:112 dd:131 |  | NO | String | Starting day, Format: MM:dd |
| ecoRule9.stopDay | Stop Day9 | MM:112 dd:131 |  | NO | String | Stop day, Format: MM:dd |
| ecoRule9.voltage | Voltage9 | 48~60 | V | NO | Number |  |
| ecoRule9.power | Power9 | 0~5000 | W | NO | Number |  |
| ecoRule9.daysOfEffectiveWeek | Effective Week9 | MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY |  | NO | Array | Week Of Use: Time Of Use Effective Week,Valuable：MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY，Multiple Choice |
| ecoRule9.soc | SOC9 | 0~100 | % | NO | Number |  |
| ecoRule10.ruleMode | ECO Mode 10 | 0:Disable  1:Charge  2:Discharge |  | NO | Number | "Economic model rules:  1) Disable: No charging and discharging  2) Charge: Charge the battery from the grid  3) Discharge: Selling power from battery to the grid  4)AC Couple:Spontaneous self-use, waste electricity Internet access" |
| ecoRule10.startTime | Start Time10 | HH:023 mm:059 |  | NO | String | Starting time, Format: HH:mm |
| ecoRule10.stopTime | Stop Time10 | HH:023 mm:059 |  | NO | String | Stop time, Format: HH:mm |
| ecoRule10.startDay | Start Day10 | MM:112 dd:131 |  | NO | String | Starting day, Format: MM:dd |
| ecoRule10.stopDay | Stop Day10 | MM:112 dd:131 |  | NO | String | Stop day, Format: MM:dd |
| ecoRule10.voltage | Voltage10 | 48~60 | V | NO | Number |  |
| ecoRule10.power | Power10 | 0~5000 | W | NO | Number |  |
| ecoRule10.daysOfEffectiveWeek | Effective Week10 | MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY |  | NO | Array | Week Of Use: Time Of Use Effective Week,Valuable：MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY，Multiple Choice |
| ecoRule10.soc | SOC10 | 0~100 | % | NO | Number |  |
| batteryModules | Battery Modules | 1~1 |  | NO | Number |  |
| batteryChargedVoltage | Battery Charged Voltage | 48~60 | V | NO | Number |  |
| batteryFloatingChargedVoltage | Bat float voltage | 48~60 | V | NO | Number |  |
| noBmsOnGridBatteryCutOffVoltage | Battery Cut-Off Voltage(On-Grid, No Bms) | 40~60 | V | NO | Number |  |
| noBmsOffGridBatteryCutOffVoltage | Battery Cut-Off Voltage(Off-Grid, No Bms) | 40~60 | V | NO | Number |  |
| noBmsOffGridBatteryRestartVoltage | Battery Restart Voltage(Off-Grid, No Bms) | 40~60 | V | NO | Number |  |
| batteryMaxChargedCurrent | Battery Max. Charged Current | 1~100 | A | NO | Number |  |
| batteryMaxDischargeCurrent | Battery Max. Discharged Current | 5~100 | A | NO | Number |  |
| parallelEnable | Parallel Enable | 0:Stand-Alone  1:Single Phase Parallel  2:Triphase Parallel-L1  3:Triphase Parallel-L2  4:Triphase Parallel-L3 |  | NO | Number | "Ensure that the inverter is operating in standby mode before setting it, Otherwise, it will cause machine malfunction." |
| --- | --- | --- | --- | --- | --- | --- |
| gridStandardCode | Standard | 0:Germany  1:Warehouse  2:50Hz grid default  3:60Hz grid default  4:Italy  5:Britain  6:Australia  7:New Zealand  8:South African  9:Netherland  10:Brazil  11:Europe  12:Poland  13:Czech |  | No | Number | Set the on-grid regulations in the current region |
| overVoltageStage1TripTime | OV Stage1 Trip Time | 0.02~1000 | Sec | No | Number |  |
| underVoltageStage1TripTime | UV Stage1 Trip Time | 0.02~1000 | Sec | No | Number |  |
| overVoltageStage2TripTime | OV Stage2 Trip Time | 0.02~1000 | Sec | No | Number |  |
| underVoltageStage2TripTime | UV Stage2 Trip Time | 0.02~1000 | Sec | No | Number |  |
| overVoltage10mTriggerValue | OV 10Min Mean Value | 230~300 | V | No | Number |  |
| overFrequencyStage1TripTime | OF Stage1 Trip Time | 0.02~1000 | Sec | No | Number |  |
| underFrequencyStage1TripTime | UF Stage1 Trip Time | 0.02~1000 | Sec | No | Number |  |
| overFrequencyStage2TripTime | OF Stage2 Trip Time | 0.02~1000 | Sec | No | Number |  |
| underFrequencyStage2TripTime | UF Stage2 Trip Time | 0.02~1000 | Sec | No | Number |  |
| onGridObservationTime | Observation Time | 1~3000 | Sec | No | Number |  |
| onGridPowerSlope | Grid Power Slope | 0~65535 | Sec | No | Number |  |
| onGridPowerLimit | Grid Power Limit | 0~100 | % | No | Number |  |
| pfPowerCurveFunctionEnable | PF-Power Curve Function | 0:Disable  1:Enable |  | No | Number |  |
| pfPowerCurvePointAPower | Point A Power | 0~100 | % | No | Number |  |
| pfPowerCurvePointAPowerFactor | Point A Power Factor | -0.99-0.8,0.81 |  | No | Number |  |
| pfPowerCurvePointBPower | Point B Power | 0~100 | % | No | Number |  |
| pfPowerCurvePointBPowerFactor | Point B Power Factor | -0.99-0.8,0.81 |  | No | Number |  |
| pfPowerCurvePointCPower | Point C Power | 0~100 | % | No | Number |  |
| pfPowerCurvePointCPowerFactor | Point C Power Factor | -0.99-0.8,0.81 |  | No | Number |  |
| pfPowerCurveLockoutPower | Lockout Power | 0~100 | % | No | Number |  |
| puCurveFunctionEnable | P(U) Curve Function | 0:Disable  1:Enable |  | No | Number |  |
| puCurvePointAActivePower | Point A  Active Power | -100~100 | % | No | Number |  |
| puCurvePointBActivePower | Point B  Active Power | -100~100 | % | No | Number |  |
| puCurvePointCActivePower | Point C  Active Power | -100~100 | % | No | Number |  |
| puCurvePointDActivePower | Point D  Active Power | -100~100 | % | No | Number |  |
| quCurveFunctionEnable | Q(U) Curve Function | 0:Disable  1:Enable |  | No | Number |  |
| quCurvePointAReactivePower | Point A  Reactive Power | -100~100 | % | No | Number |  |
| quCurvePointBReactivePower | Point B  Reactive Power | -100~100 | % | No | Number |  |
| quCurvePointCReactivePower | Point C  Reactive Power | -100~100 | % | No | Number |  |
| quCurvePointDReactivePower | Point D  Reactive Power | -100~100 | % | No | Number |  |
| quCurveLockInPower | Lock In Power | -100~100 | % | No | Number |  |
| quCurveLockOutPower | Lock Out Power | -100~100 | % | No | Number |  |
| fpCurveFunctionEnable | FP Curve Function | 0:Disable  1:Enable |  | No | Number |  |
| fpCurveOverFrequencyLowerLimit | Over Frequency Start Point | 30~80 | Hz | No | Number |  |
| fpUnderFrequencyLowerLimit | Under Frequency Start Point | 30~80 | Hz | No | Number |  |
| fpOverFrequencyUpperLimit | Over Frequency End Point | 30~80 | Hz | No | Number |  |
| fpUnderFrequencyUpperLimit | Under Frequency End Point | 30~80 | Hz | No | Number |  |
| fpRestoreFrequencyUperLimit | F(Stop) Upper | 30~80 | Hz | No | Number |  |
| fpRestoreFrequencyLowerLimit | F(Stop) Lower | 30~80 | Hz | No | Number |  |
| fpRestoreFrequencyWaitingTime | Restore Waiting Time | 1~65535 | Sec | No | Number |  |
| fpRestoreFrequencyPowerSlope | Reconnection Power Slope | 1~65535 | Sec | No | Number |  |
| fpOverFrequencyPowerSlope | Over Frequency Power Slope | 0~100 | % | No | Number |  |
| fpUnderFrequencyPowerSlope | Under Frequency Power Slope | 0~100 | % | No | Number |  |
| fpRecoveryPowerSlope | Recovery Power Slope | 0~100 | % | No | Number |  |
| fpChargeCurveFunctionEnable | FP Charge Curve Function | 0:Disable  1:Enable |  | No | Number |  |
| fpUnderFrequencyPowerSlopeForCharge | Under Frequency Power Slope For Charge | 0~100 | % | No | Number |  |
| lowVoltageRideThroughFunctionEnable | Low Voltage Ride Through | 0:Disable  1:Enable |  | No | Number |  |
| lowVoltageStartPointTripTime | Start Point Of Protection Time | 0.02~1000 | Sec | No | Number |  |
| lowVoltageEndPointTripTime | End Point Of Protection Time | 0.02~1000 | Sec | No | Number |  |
| highVoltageRideThroughFunctionEnable | High Voltage Ride Through Function | 0:Disable  1:Enable |  | No | Number |  |
| highVoltageStartPointTripTime | Start Point Of Protection Time | 0.02~1000 | Sec | No | Number |  |
| highVoltageEndPointTripTime | End Point Of Protection Time | 0.02~1000 | Sec | No | Number |  |
| overVoltageStage1TripValue | OV Stage1 Trip Value | 230~300 | V | No | Number |  |
| underVoltageStage1TripValue | UV Stage1 Trip Value | 0.1~300 | V | No | Number |  |
| overVoltageStage2TripValue | OV Stage2 Trip Value | 230~300 | V | No | Number |  |
| underVoltageStage2TripValue | UV Stage2 Trip Value | 0.1~300 | V | No | Number |  |
| overFrequencyStage1TripValue | OF Stage1 Trip Value | 30~80 | Hz | No | Number |  |
| underFrequencyStage1TripValue | UF Stage1 Trip Value | 30~80 | Hz | No | Number |  |
| overFrequencyStage2TripValue | OF Stage2 Trip Value | 30~80 | Hz | No | Number |  |
| underFrequencyStage2TripValue | UF Stage2 Trip Value | 30~80 | Hz | No | Number |  |
| pfPowerCurveLockinVoltage | Lockin Voltage | 60~300 | V | No | Number |  |
| pfPowerCurveLockoutVoltage | Lockout Voltage | 60~300 | V | No | Number |  |
| puCurvePointAVoltage | Point A Voltage | 60~300 | V | No | Number |  |
| puCurvePointBVoltage | Point B  Voltage | 60~300 | V | No | Number |  |
| puCurvePointCVoltage | Point C  Voltage | 60~300 | V | No | Number |  |
| puCurvePointDVoltage | Point D  Voltage | 60~300 | V | No | Number |  |
| quCurvePointAVoltage | Point A Voltage | 60~300 | V | No | Number |  |
| quCurvePointBVoltage | Point B  Voltage | 60~300 | V | No | Number |  |
| quCurvePointCVoltage | Point C  Voltage | 60~300 | V | No | Number |  |
| quCurvePointDVoltage | Point D  Voltage | 60~300 | V | No | Number |  |
| lowVoltageStartPointTripValue | Start Point Of Ride Through | 0~230 | V | No | Number |  |
| lowVoltageEndPointTripValue | End Point Of Ride Through | 0~230 | V | No | Number |  |
| lowVoltageCrossingTripThreshold | Low Voltage Limit Of Ride Through | 0~230 | V | No | Number |  |
| highVoltageStartPointTripValue | Start Point Of Ride Through | 230~300 | V | No | Number |  |
| highVoltageEndPointTripValue | End Point Of Ride Through | 230~300 | V | No | Number |  |
| highVoltageCrossingTripThreshold | High Voltage Limit Of Ride Through | 230~300 | V | No | Number |  |
| commOffLineEnable | CommOffLine | 0:Disable  1:Enable |  | No | Number |  |
| autoTestEnable | AutoTestEnable | 0:Disable  1:Enable |  | No | Number |  |
| deratingByVoltageEnable | DeratingByVoltage | 0:Disable  1:Enable |  | No | Number |  |
| deviceSn | 013548202500010000 |  |  | Yes | String | Device serial number |

**Response return Example.**

```json
{
  "code": 200,
  "message": "Success",
  "data": {
    "isoCheckThreshold": "33",
    "batteryMaxDischargeCurrent": "50",
    "genUnderVoltageVoltage2": "65534",
    "genAutoStartChargeVoltage": "470",
    "genUnderVoltageVoltage1": "65534",
    "smartLoadOpenBatteryVoltage": "500",
    "gridChargeEnable": "1",
    "gridUnderVoltageVoltage1": "85",
    "batteryCapacity": "100",
    "fpUnderFrequencyDeratingRatio": "200",
    "uqReactivePowerDropStart": "40",
    "fpUnderFrequencyDeratingStart": "49.8",
    "genMaxRunTime": "24",
    "clearEnergyStorageLog": "0",
    "ppfActivePowerLockIn": "30",
    "machineId": "1",
    "fgOverFrequencyToChargePercentage": "65535",
    "uqReactivePowerDropEnd": "90",
    "batteryShutdownVoltage": "430",
    "fgUnderFrequencyToDischargeFrequency": "49.5",
    "gridOverFrequencyFrequency1": "52",
    "gridOverFrequencyFrequency3": "52.1",
    "gridOverFrequencyFrequency2": "52.1",
    "gridOverFrequencyFrequency5": "52.1",
    "upfWorkModeEnable": "0",
    "gridOverFrequencyFrequency4": "52.1",
    "energyPriority": "0",
    "ppfActivePowerLockOut": "5",
    "genUnderVoltageTime2": "655.34",
    "genUnderVoltageTime1": "655.34",
    "acOutputRatedFrequency": "0",
    "offGridVoltageCompensation": "0",
    "fgUnderFrequencyToDischargePercentage": "1",
    "lvrtVoltage5": "20",
    "zeroExportHysteresisPower": "0",
    "lvrtVoltage4": "20",
    "lvrtVoltage3": "20",
    "lvrtVoltage2": "20",
    "remoteOnOffEnable": "0",
    "upfPowerFactorDropEnd": "50",
    "ecoRule10": {},
    "fpOverFrequencyDeratingEnd": "51.5",
    "upDeratingWorkModeEnable": "0",
    "uqVoltageDropStart": "91",
    "gridUnderVoltageTime2": "0.1",
    "gridUnderVoltageTime1": "2",
    "gridUnderVoltageTime4": "0.1",
    "gridUnderVoltageTime3": "0.1",
    "gridUnderVoltageTime5": "0.1",
    "fpExitRate": "0.33",
    "leakageCurrentGfciProtectionThreshold": "500",
    "genUnderFrequencyFrequency1": "655.34",
    "genUnderFrequencyFrequency2": "655.34",
    "genChargeCurrent": "25",
    "ppfActivePowerD": "100",
    "ppfActivePowerC": "90",
    "ppfActivePowerB": "70",
    "runningActivePowerRampRate": "100",
    "ppfActivePowerA": "50",
    "uqReactivePowerRiseStart": "40",
    "ecoRule4": {
      "gridChangingEnable": "0",
      "genChangingEnable": "0",
      "soc": "50",
      "startTime": "14:00",
      "power": "50",
      "endTime": "18:00",
      "voltage": "481"
    },
    "ecoRule3": {
      "gridChangingEnable": "0",
      "genChangingEnable": "0",
      "soc": "50",
      "startTime": "12:00",
      "power": "50",
      "endTime": "14:00",
      "voltage": "481"
    },
    "ecoRule2": {
      "gridChangingEnable": "0",
      "genChangingEnable": "0",
      "soc": "50",
      "startTime": "08:00",
      "power": "50",
      "endTime": "12:00",
      "voltage": "481"
    },
    "ecoRule1": {
      "gridChangingEnable": "0",
      "genChangingEnable": "0",
      "soc": "100",
      "startTime": "00:00",
      "endTime": "08:00",
      "power": "25",
      "voltage": "481"
    },
    "ecoRule8": {},
    "ecoRule7": {},
    "ecoRule6": {
      "gridChangingEnable": "0",
      "genChangingEnable": "0",
      "soc": "50",
      "startTime": "21:00",
      "endTime": "00:00",
      "power": "25",
      "voltage": "481"
    },
    "ecoRule5": {
      "gridChangingEnable": "0",
      "genChangingEnable": "0",
      "soc": "50",
      "startTime": "18:00",
      "power": "25",
      "endTime": "21:00",
      "voltage": "481"
    },
    "ecoRule9": {},
    "gridUnderFrequencyFrequency2": "47",
    "gridUnderFrequencyFrequency3": "47",
    "uqReactivePowerLockIn": "10",
    "gridUnderFrequencyFrequency4": "47",
    "gridUnderFrequencyFrequency5": "47",
    "zeroExportToLoadEnable": "0",
    "batteryFloatingChargedVoltage": "564",
    "genAutoExitChargeSoc": "10",
    "uqVoltageRiseStart": "109",
    "gridUnderFrequencyFrequency1": "47.5",
    "uqReactivePowerRiseEnd": "90",
    "pqReactiveActivePowerA": "0",
    "pqReactiveActivePowerB": "0",
    "pqReactiveActivePowerC": "0",
    "pqReactiveActivePowerD": "0",
    "fpExitDelay": "3000",
    "turnOffRampRate": "100",
    "ppfPowerFactorC": "92",
    "ppfPowerFactorB": "96",
    "ppfPowerFactorD": "92",
    "gridUnderVoltageVoltage4": "50",
    "gridUnderVoltageVoltage5": "50",
    "ppfPowerFactorA": "100",
    "gridUnderVoltageVoltage2": "50",
    "gridUnderVoltageVoltage3": "50",
    "lvrtTime4": "1",
    "bmsCommunicationFailureEnabled": "0",
    "lvrtTime3": "1",
    "batteryLowVoltageAlarmSoc": "7",
    "lvrtTime2": "1",
    "lvrtTime1": "3",
    "lvrtTime5": "1",
    "turnOnRampRate": "100",
    "dspParallelEnable": "0",
    "fpOverFrequencyDeratingStart": "50.2",
    "gridOverFrequencyTime1": "2",
    "acOutputRatedVoltage": "400",
    "gridOverFrequencyTime2": "0.16",
    "gridChargeCurrent": "50",
    "gridOverFrequencyTime5": "0.16",
    "gridOverFrequencyTime3": "0.16",
    "gridOverFrequencyTime4": "0.16",
    "smartLoadCloseBatterySoc": "90",
    "drmEnable": "0",
    "lvrtDynamicReactivePowerKfFactor": "1.5",
    "powerFactorGiven": "1",
    "ppfWorkModeEnable": "0",
    "gridOverVoltageVoltage1": "130",
    "gridOverVoltageVoltage2": "130",
    "gridOverVoltageVoltage3": "130",
    "gridOverVoltageVoltage4": "130",
    "gridOverVoltageVoltage5": "130",
    "activeIslandingProtectionEnable": "0",
    "gridUnbalanceProtectionVoltage": "5",
    "timeOfUseEnable": "0",
    "operatedMode": "3",
    "gridConnectionWaitTime": "5",
    "upDeratingRecoveryRate": "2",
    "pqActivePowerA": "0",
    "pqActivePowerD": "0",
    "pqActivePowerB": "0",
    "pqActivePowerC": "0",
    "hvrtVoltage1": "110",
    "reactivePowerControlMode": "0",
    "hvrtVoltage2": "130",
    "hvrtVoltage3": "130",
    "genOverFrequencyFrequency2": "655.34",
    "hvrtVoltage4": "130",
    "genOverFrequencyFrequency1": "655.34",
    "hvrtVoltage5": "130",
    "fpOverFrequencyDeratingExit": "50.2",
    "maxSellingPower": "55",
    "upDeratingActivePowerA": "100",
    "isoCheckEnable": "1",
    "upfVoltageRiseStart": "80",
    "upDeratingActivePowerD": "40",
    "batteryActivationEnable": "0",
    "upDeratingActivePowerB": "80",
    "upDeratingActivePowerC": "60",
    "batteryRestartOutputSoc": "8",
    "genInputPowerLimitEnable": "0",
    "zeroExportToCtEnable": "0",
    "gridPeakShavingEnable": "0",
    "masterSlaverSetting": "1",
    "factoryReset": "0",
    "pqWorkModeEnable": "0",
    "asymmetricPhaseFeedingEnable": "0",
    "deviceSn": "013548202500010000",
    "leakageCurrentGfciProtectionEnable": "1",
    "fpOverFrequencyDeratingRatio": "154",
    "smartPortModeEnable": "0",
    "uqWorkModeEnable": "1",
    "genRatePower": "50",
    "dispatchActivePowerGiven": "7.9",
    "genStartSignalEnable": "1",
    "reactivePowerGiven": "0",
    "smartLoadNormalCloseEnable": "0",
    "uqVoltageDropEnd": "90",
    "upfVoltageRiseEnd": "100",
    "fpResponseWorkModeEnable": "0",
    "gridOverVoltageTime1": "2",
    "genAutoExitChargeVoltage": "480",
    "gridOverVoltageTime2": "0.1",
    "gridOverVoltageTime3": "0.1",
    "highVoltageRideThroughEnable": "0",
    "gridOverVoltageTime4": "0.1",
    "fpUnderFrequencyDeratingEnd": "49.1",
    "upDeratingDropRate": "2",
    "gridOverVoltageTime5": "0.1",
    "genOverVoltageVoltage2": "65534",
    "genOverVoltageVoltage1": "65534",
    "batteryRestartOutputVoltage ": "512",
    "runningReactivePowerRampRate": "100",
    "lvrtVoltage1": "90",
    "fpResponseDelay": "0",
    "fpUnderFrequencyDeratingExit": "51.5",
    "uqReactivePowerLockOut": "5",
    "batteryMaxChargedCurrent": "26",
    "smartLoadCloseBatteryVoltage": "540",
    "genOverVoltageTime1": "655.34",
    "genOverVoltageTime2": "655.34",
    "batteryLowVoltageAlarmVoltage": "450",
    "genUnderFrequencyTime1": "655.34",
    "genUnderFrequencyTime2": "655.34",
    "upDeratingVoltageC": "112",
    "upDeratingVoltageD": "114",
    "upDeratingVoltageA": "108",
    "upDeratingVoltageB": "110",
    "upfPowerFactorDropStart": "100",
    "batteryParallelEnable": "0",
    "genOverFrequencyTime1": "655.34",
    "ctRatio": "0",
    "genOverFrequencyTime2": "655.34",
    "gridUnbalanceProtectionTime": "30",
    "genForceRunningEnable": null,
    "smartLoadOpenBatterySoc": "80",
    "hvrtDynamicReactivePowerKfFactor": "1.5",
    "batteryMode": "0",
    "genAutoStartChargeSoc": "5",
    "touEffectiveWeek": "127",
    "fgWorkModeEnable": "0",
    "gridPeakShavingPower": "0",
    "gridUnderFrequencyTime2": "0.16",
    "uqVoltageRiseEnd": "110",
    "gridUnderFrequencyTime1": "2",
    "gridUnderFrequencyTime4": "0.16",
    "gridUnderFrequencyTime3": "0.16",
    "gridUnderFrequencyTime5": "0.16",
    "fgOverFrequencyToCchargeFrequency": "50.2",
    "batteryShutdownSoc": "6",
    "genConnectGridEnable": "0",
    "gridStandardCode": "2",
    "fpResponseRate": "500",
    "hvrtTime2": "0.5",
    "hvrtTime1": "1",
    "hvrtTime4": "0.5",
    "genChargeEnable": "1",
    "hvrtTime3": "0.5",
    "lowVoltageRideThroughEnable": "0",
    "hvrtTime5": "0.5"
  }
}
```

**Query**

# Economic Model Strategy Template Management

> Created by: Timesup

> Updated by: Timesup

> Created at: 2024-06-24 08:54:36

> Updated at: 2024-06-26 14:34:33

**The economic model strategy template is a mandatory field when creating economic model tasks. The economic mode strategy template actually applies to the economic mode rules on the machine, and the common template is extracted to facilitate batch setting of devices**

**Directory Header Parameters**

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| No parameters |

**Directory Query Parameters**

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| No parameters |

**Directory Body Parameters**

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| No parameters |

**Directory Authentication Info**

> Inherit from parent

**Query**

## Add Economic Model Strategy Template

> Created by: Timesup

> Updated by: Timesup

> Created at: 2024-06-24 08:54:36

> Updated at: 2024-07-22 09:46:06

**The application server can call this interface to add economic mode strategy templates through the Fsolar platform.**

**Interface Status**

> Completed

**Interface URL**

> /openApi/ecoStrategyTemplate/save

**Request Method**

> POST

**Content-Type**

> json

**Request Header Parameters**

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| Content-Type | application/json | string | Yes | - |
| Authorization | Bearer_eyJhbGciOiJIUzI1NiJ9.eyJkZW1vVXNlciI6ZmFsc2UsInN1YiI6IueuoeeQhuWRmCIsImF1ZCI6Ik56TTNORFF4TkRrd01UVTFPREUwTkE9PSIsIm5iZiI6MTcxMTY3NjY4NiwiaXNzIjoiRkxTLVNPTEFSLVNFUlZFUiIsImlkIjo3Mzc0NDE0OTAxNTU4MTQ0LCJleHAiOjE3MTQyNjg2ODYsImlhdCI6MTcxMTY3NjY4Nn0._l5VIYevtyv2Xc66S9w6fqmkECBFvLZPJYqjU07pObE | string | Yes | User token, which can be obtained from authentication and refreshing tokens. |
| Lang | en_US | string | Yes | Language, currently supports English en_US. |

**Request Body Parameters**

```javascript
{
	"strategy1": {
		"backupReserve": "",
		"daysOfEffectiveWeek": [
			""
		],
		"power": 0,
		"soc": 0,
		"startDay": "",
		"startTime": "",
		"stopDay": "",
		"stopTime": "",
		"strategy": 0
	},
	"strategy2": {
		"backupReserve": "",
		"daysOfEffectiveWeek": [
			""
		],
		"power": 0,
		"soc": 0,
		"startDay": "",
		"startTime": "",
		"stopDay": "",
		"stopTime": "",
		"strategy": 0
	},
	"strategy3": {
		"backupReserve": "",
		"daysOfEffectiveWeek": [
			""
		],
		"power": 0,
		"soc": 0,
		"startDay": "",
		"startTime": "",
		"stopDay": "",
		"stopTime": "",
		"strategy": 0
	},
	"strategy4": {
		"backupReserve": "",
		"daysOfEffectiveWeek": [
			""
		],
		"power": 0,
		"soc": 0,
		"startDay": "",
		"startTime": "",
		"stopDay": "",
		"stopTime": "",
		"strategy": 0
	},
	"templateName": ""
}
```

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| strategy1 | - | object | Yes | strategy1 |
| strategy1.backupReserve | - | string | No | backupReserve |
| strategy1.daysOfEffectiveWeek | - | array | No | Days Of Effective Week,Valuable：MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY，Multiple Choice |
| strategy1.power | 0 | number | No | Battery charging or discharging power,Unit：W，The range of values is 0~100% inverter rated power |
| strategy1.soc | 0 | number | No | Battery charging or discharging soc，Unit：%，The range of values is 0~100% |
| strategy1.startDay | - | string | No | Starting date, Format: mm:dd |
| strategy1.startTime | - | string | No | Starting time, Format: HH:ss |
| strategy1.stopDay | - | string | No | Stop date, Format: mm:dd |
| strategy1.stopTime | - | string | No | Stop time, Format: HH:ss |
| strategy1.strategy | 0 | number | Yes | strategy : 0=Disable，1=Charge,2=Discharge |
| strategy2 | - | object | No | strategy2 |
| strategy2.backupReserve | - | string | No | backupReserve |
| strategy2.daysOfEffectiveWeek | - | array | No | Days Of Effective Week,Valuable：MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY，Multiple Choice |
| strategy2.power | 0 | number | No | Battery charging or discharging power,Unit：W，The range of values is 0~100% inverter rated power |
| strategy2.soc | 0 | number | No | Battery charging or discharging soc，Unit：%，The range of values is 0~100% |
| strategy2.startDay | - | string | No | Starting date, Format: mm:dd |
| strategy2.startTime | - | string | No | Starting time, Format: HH:ss |
| strategy2.stopDay | - | string | No | Stop date, Format: mm:dd |
| strategy2.stopTime | - | string | No | Stop time, Format: HH:ss |
| strategy2.strategy | 0 | number | Yes | strategy : 0=Disable，1=Charge,2=Discharge |
| strategy3 | - | object | No | strategy3 |
| strategy3.backupReserve | - | string | No | backupReserve |
| strategy3.daysOfEffectiveWeek | - | array | No | Days Of Effective Week,Valuable：MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY，Multiple Choice |
| strategy3.power | 0 | number | No | Battery charging or discharging power,Unit：W，The range of values is 0~100% inverter rated power |
| strategy3.soc | 0 | number | No | Battery charging or discharging soc，Unit：%，The range of values is 0~100% |
| strategy3.startDay | - | string | No | Starting date, Format: mm:dd |
| strategy3.startTime | - | string | No | Starting time, Format: HH:ss |
| strategy3.stopDay | - | string | No | Stop date, Format: mm:dd |
| strategy3.stopTime | - | string | No | Stop time, Format: HH:ss |
| strategy3.strategy | 0 | number | Yes | strategy : 0=Disable，1=Charge,2=Discharge |
| strategy4 | - | object | No | strategy4 |
| strategy4.backupReserve | - | string | No | backup Reserve |
| strategy4.daysOfEffectiveWeek | - | array | No | Days Of Effective Week,Valuable：MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY，Multiple Choice |
| strategy4.power | 0 | number | No | Battery charging or discharging power,Unit：W，The range of values is 0~100% inverter rated power |
| strategy4.soc | 0 | number | No | Battery charging or discharging soc，Unit：%，The range of values is 0~100% |
| strategy4.startDay | - | string | No | Starting date, Format: mm:dd |
| strategy4.startTime | - | string | No | Starting time, Format: HH:ss |
| strategy4.stopDay | - | string | No | Stop date, Format: mm:dd |
| strategy4.stopTime | - | string | No | Stop time, Format: HH:ss |
| strategy4.strategy | 0 | number | Yes | strategy : 0=Disable，1=Charge,2=Discharge |
| templateName | - | object | No | template Name |
| strategy5 | - | object | No | strategy5 , refer to strategy1 |
| strategy6 | - | object | No | strategy6 , refer to strategy1 |
| strategy7 | - | object | No | strategy7 , refer to strategy1 |
| strategy8 | - | object | No | strategy8 , refer to strategy1 |
| strategy9 | - | object | No | strategy9 , refer to strategy1 |
| strategy10 | - | object | No | strategy10 , refer to strategy1 |

**Authentication Method**

> Inherit from parent

**Response Example**

* OK(200)

```javascript
{
  "code": 200,
  "message": "Success",
  "data": {
    "templateName": "sdfsd",
    "id": "9803372250529216"
  }
}
```

| Parameter Name | Example Value | Parameter Type | Description |
| --- | --- | ---- | ---- |
| code | - | integer | code |
| message | - | string | message |
| data | - | object | data |

* token expired(200)

```javascript
{
  "code": 998,
  "message": "The token has expired, please log in again",
  "data": {}
}
```

**Request Header Parameters**

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| Content-Type | application/json | string | Yes | - |
| Authorization | Bearer_eyJhbGciOiJIUzI1NiJ9.eyJkZW1vVXNlciI6ZmFsc2UsInN1YiI6IueuoeeQhuWRmCIsImF1ZCI6Ik56TTNORFF4TkRrd01UVTFPREUwTkE9PSIsIm5iZiI6MTcxMTY3NjY4NiwiaXNzIjoiRkxTLVNPTEFSLVNFUlZFUiIsImlkIjo3Mzc0NDE0OTAxNTU4MTQ0LCJleHAiOjE3MTQyNjg2ODYsImlhdCI6MTcxMTY3NjY4Nn0._l5VIYevtyv2Xc66S9w6fqmkECBFvLZPJYqjU07pObE | string | Yes | User token, which can be obtained from authentication and refreshing tokens. |
| Lang | en_US | string | Yes | Language, currently supports English en_US. |

**Query**

## Pagination query economic mode strategy template

> Created by: Timesup

> Updated by: Timesup

> Created at: 2024-06-24 08:54:36

> Updated at: 2024-07-22 09:50:14

**The application server can call this interface to page query the economic mode strategy template through the Fsolar platform.**

**Interface Status**

> Completed

**Interface URL**

> /openApi/ecoStrategyTemplate/list

**Request Method**

> POST

**Content-Type**

> json

**Request Header Parameters**

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| Content-Type | application/json | string | Yes | - |
| Authorization | Bearer_eyJhbGciOiJIUzI1NiJ9.eyJkZW1vVXNlciI6ZmFsc2UsInN1YiI6IueuoeeQhuWRmCIsImF1ZCI6Ik56TTNORFF4TkRrd01UVTFPREUwTkE9PSIsIm5iZiI6MTcxMTY3NjY4NiwiaXNzIjoiRkxTLVNPTEFSLVNFUlZFUiIsImlkIjo3Mzc0NDE0OTAxNTU4MTQ0LCJleHAiOjE3MTQyNjg2ODYsImlhdCI6MTcxMTY3NjY4Nn0._l5VIYevtyv2Xc66S9w6fqmkECBFvLZPJYqjU07pObE | string | Yes | User token, which can be obtained from authentication and refreshing tokens. |
| Lang | en_US | string | Yes | Language, currently supports English en_US. |

**Request Body Parameters**

```javascript
{
	
	"id": 0,
	"pageNum": 1,
	"pageSize": 10,
	"templateName": ""
}
```

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| id | - | integer | No | id |
| pageNum | 1 | integer | Yes | Page numbers, starting from 1 |
| pageSize | 10 | integer | Yes | Number of entries per page, maximum of 300 |
| templateName | - | string | No | Template Name |

**Authentication Method**

> Inherit from parent

**Response Example**

* OK(200)

```javascript
{
	"data": {},
	"total": 0,
	"totalPage": 0,
	"currentPage": 0,
	"pageSize": 0,
	"dataList": [
		{
			"createTime": "",
			"id": 0,
			"modifyTime": "",
			"strategy1": {
				"backupReserve": "",
				"daysOfEffectiveWeek": [
					""
				],
				"power": 0,
				"soc": 0,
				"startDay": "",
				"startTime": "",
				"stopDay": "",
				"stopTime": "",
				"strategy": 0
			},
			"strategy2": {
				"backupReserve": "",
				"daysOfEffectiveWeek": [
					""
				],
				"power": 0,
				"soc": 0,
				"startDay": "",
				"startTime": "",
				"stopDay": "",
				"stopTime": "",
				"strategy": 0
			},
			"strategy3": {
				"backupReserve": "",
				"daysOfEffectiveWeek": [
					""
				],
				"power": 0,
				"soc": 0,
				"startDay": "",
				"startTime": "",
				"stopDay": "",
				"stopTime": "",
				"strategy": 0
			},
			"strategy4": {
				"backupReserve": "",
				"daysOfEffectiveWeek": [
					""
				],
				"power": 0,
				"soc": 0,
				"startDay": "",
				"startTime": "",
				"stopDay": "",
				"stopTime": "",
				"strategy": 0
			},
			
			"templateName": ""
		}
	]
}
```

| Parameter Name | Example Value | Parameter Type | Description |
| --- | --- | ---- | ---- |
| data | - | object | Additional data |
| total | - | integer | Total number of records |
| totalPage | - | integer | total Page |
| currentPage | - | integer | current Page |
| pageSize | - | integer | page Size |
| dataList.createTime | - | string | Creation time |
| dataList.id | - | integer | Template id |
| dataList.modifyTime | - | string | Modification time |
| dataList.strategy1.backupReserve | - | number | backupReserve |
| dataList.strategy1.daysOfEffectiveWeek.0 | - | array | Days Of Effective Week,Valuable：MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY，Multiple Choice |
| dataList.strategy1.power | - | integer | Battery charging or discharging power,Unit：W，The range of values is 0~inverter rated power |
| dataList.strategy1.soc | - | integer | Battery charging or discharging soc，Unit：%，The range of values is 0~100% |
| dataList.strategy1.startDay | - | string | Starting date, Format: mm:dd |
| dataList.strategy1.startTime | - | string | Starting time, Format: HH:ss |
| dataList.strategy1.stopDay | - | string | Stop date, Format: mm:dd |
| dataList.strategy1.stopTime | - | string | Stop time, Format: HH:ss |
| dataList.strategy1.strategy | - | integer | strategy : 0=Disable，1=Charge,2=Discharge |
| dataList.strategy1 | - | object | - |
| dataList.strategy2.backupReserve | - | number | backupReserve |
| dataList.strategy2.daysOfEffectiveWeek.0 | - | array | Days Of Effective Week,Valuable：MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY，Multiple Choice |
| dataList.strategy2.power | - | integer | Battery charging or discharging power,Unit：W，The range of values is 0~inverter rated power |
| dataList.strategy2.soc | - | integer | Battery charging or discharging soc，Unit：%，The range of values is 0~100% |
| dataList.strategy2.startDay | - | string | Starting date, Format: mm:dd |
| dataList.strategy2.startTime | - | string | Starting time, Format: HH:ss |
| dataList.strategy2.stopDay | - | string | Stop date, Format: mm:dd |
| dataList.strategy2.stopTime | - | string | Stop time, Format: HH:ss |
| dataList.strategy2.strategy | - | integer | strategy : 0=Disable，1=Charge,2=Discharge |
| dataList.strategy2 | - | object | - |
| dataList.strategy3.backupReserve | - | number | backupReserve |
| dataList.strategy3.daysOfEffectiveWeek.0 | - | array | Days Of Effective Week,Valuable：MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY，Multiple Choice |
| dataList.strategy3.power | - | integer | Battery charging or discharging power,Unit：W，The range of values is 0~inverter rated power |
| dataList.strategy3.soc | - | integer | Battery charging or discharging soc，Unit：%，The range of values is 0~100% |
| dataList.strategy3.startDay | - | string | Starting date, Format: mm:dd |
| dataList.strategy3.startTime | - | string | Starting time, Format: HH:ss |
| dataList.strategy3.stopDay | - | string | Stop date, Format: mm:dd |
| dataList.strategy3.stopTime | - | string | Stop time, Format: HH:ss |
| dataList.strategy3.strategy | - | integer | strategy : 0=Disable，1=Charge,2=Discharge |
| dataList.strategy3 | - | object | - |
| dataList.strategy4.backupReserve | - | number | backupReserve |
| dataList.strategy4.daysOfEffectiveWeek.0 | - | array | Days Of Effective Week,Valuable：MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY，Multiple Choice |
| dataList.strategy4.power | - | integer | Battery charging or discharging power,Unit：W，The range of values is 0~inverter rated power |
| dataList.strategy4.soc | - | integer | Battery charging or discharging soc，Unit：%，The range of values is 0~100% |
| dataList.strategy4.startDay | - | string | Starting date, Format: mm:dd |
| dataList.strategy4.startTime | - | string | Starting time, Format: HH:ss |
| dataList.strategy4.stopDay | - | string | Stop date, Format: mm:dd |
| dataList.strategy4.stopTime | - | string | Stop time, Format: HH:ss |
| dataList.strategy4.strategy | - | integer | strategy : 0=Disable，1=Charge,2=Discharge |
| dataList.templateName | - | string | template name |
| dataList.strategy4 | - | object | dataList.strategy4 , refer to dataList.strategy1 |
| dataList.strategy5 | - | object | dataList.strategy5 , refer to dataList.strategy1 |
| dataList.strategy6 | - | object | dataList.strategy6 , refer to dataList.strategy1 |
| dataList.strategy7 | - | object | dataList.strategy7 , refer to dataList.strategy1 |
| dataList.strategy8 | - | object | dataList.strategy8 , refer to dataList.strategy1 |
| dataList.strategy9 | - | object | dataList.strategy9 , refer to dataList.strategy1 |
| dataList.strategy10 | - | object | dataList.strategy10 , refer to dataList.strategy1 |

* Created(201)

```javascript
No data
```

* Unauthorized(401)

```javascript
No data
```

* Forbidden(403)

```javascript
No data
```

* Not Found(404)

```javascript
No data
```

* token expire(200)

```javascript
{
  "code": 998,
  "message": "The token has expired, please log in again",
  "data": {}
}
```

**Request Header Parameters**

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| Content-Type | application/json | string | Yes | - |
| Authorization | Bearer_eyJhbGciOiJIUzI1NiJ9.eyJkZW1vVXNlciI6ZmFsc2UsInN1YiI6IueuoeeQhuWRmCIsImF1ZCI6Ik56TTNORFF4TkRrd01UVTFPREUwTkE9PSIsIm5iZiI6MTcxMTY3NjY4NiwiaXNzIjoiRkxTLVNPTEFSLVNFUlZFUiIsImlkIjo3Mzc0NDE0OTAxNTU4MTQ0LCJleHAiOjE3MTQyNjg2ODYsImlhdCI6MTcxMTY3NjY4Nn0._l5VIYevtyv2Xc66S9w6fqmkECBFvLZPJYqjU07pObE | string | Yes | User token, which can be obtained from authentication and refreshing tokens. |
| Lang | en_US | string | Yes | Language, currently supports English en_US. |

**Query**

## Update Economic Model Strategy Template

> Created by: Timesup

> Updated by: Timesup

> Created at: 2024-06-24 08:54:36

> Updated at: 2024-07-22 09:59:41

**The application server can call this interface to modify the economic mode policy template through the Fsolar platform.**

**Interface Status**

> Completed

**Interface URL**

> /openApi/ecoStrategyTemplate/update

**Request Method**

> POST

**Content-Type**

> json

**Request Header Parameters**

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| Content-Type | application/json | string | Yes | - |
| Authorization | Bearer_eyJhbGciOiJIUzI1NiJ9.eyJkZW1vVXNlciI6ZmFsc2UsInN1YiI6IueuoeeQhuWRmCIsImF1ZCI6Ik56TTNORFF4TkRrd01UVTFPREUwTkE9PSIsIm5iZiI6MTcxMTY3NjY4NiwiaXNzIjoiRkxTLVNPTEFSLVNFUlZFUiIsImlkIjo3Mzc0NDE0OTAxNTU4MTQ0LCJleHAiOjE3MTQyNjg2ODYsImlhdCI6MTcxMTY3NjY4Nn0._l5VIYevtyv2Xc66S9w6fqmkECBFvLZPJYqjU07pObE | string | Yes | User token, which can be obtained from authentication and refreshing tokens. |
| Lang | en_US | string | Yes | Language, currently supports English en_US. |

**Request Body Parameters**

```javascript
{
	"id": 0,
	"strategy1": {
		"backupReserve": "",
		"daysOfEffectiveWeek": [
			""
		],
		"power": 0,
		"soc": 0,
		"startDay": "",
		"startTime": "",
		"stopDay": "",
		"stopTime": "",
		"strategy": 0
	},
	"strategy2": {
		"backupReserve": "",
		"daysOfEffectiveWeek": [
			""
		],
		"power": 0,
		"soc": 0,
		"startDay": "",
		"startTime": "",
		"stopDay": "",
		"stopTime": "",
		"strategy": 0
	},
	"strategy3": {
		"backupReserve": "",
		"daysOfEffectiveWeek": [
			""
		],
		"power": 0,
		"soc": 0,
		"startDay": "",
		"startTime": "",
		"stopDay": "",
		"stopTime": "",
		"strategy": 0
	},
	"strategy4": {
		"backupReserve": "",
		"daysOfEffectiveWeek": [
			""
		],
		"power": 0,
		"soc": 0,
		"startDay": "",
		"startTime": "",
		"stopDay": "",
		"stopTime": "",
		"strategy": 0
	},
	"templateName": ""
}
```

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| id | - | integer | Yes | template id |
| strategy1.backupReserve | - | number | No | backupReserve |
| strategy1.daysOfEffectiveWeek.0 | - | array | No | Days Of Effective Week,Valuable：MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY，Multiple Choice |
| strategy1.power | - | integer | No | Battery charging or discharging power,Unit：W，The range of values is 0~inverter rated power |
| strategy1.soc | - | integer | No | Battery charging or discharging soc，Unit：%，The range of values is 0~100% |
| strategy1.startDay | - | string | No | Starting date, Format: mm:dd |
| strategy1.startTime | - | string | No | Starting time, Format: HH:ss |
| strategy1.stopDay | - | string | No | Stop date, Format: mm:dd |
| strategy1.stopTime | - | string | No | Stop time, Format: HH:ss |
| strategy1.strategy | - | integer | Yes | strategy: 0=Disable，1=Charge,2=Discharge |
| strategy1 | - | object | No | - |
| strategy2.backupReserve | - | number | No | backupReserve |
| strategy2.daysOfEffectiveWeek.0 | - | array | No | Days Of Effective Week,Valuable：MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY，Multiple Choice |
| strategy2.power | - | integer | No | Battery charging or discharging power,Unit：W，The range of values is 0~inverter rated power |
| strategy2.soc | - | integer | No | Battery charging or discharging soc，Unit：%，The range of values is 0~100% |
| strategy2.startDay | - | string | No | Starting date, Format: mm:dd |
| strategy2.startTime | - | string | No | Starting time, Format: HH:ss |
| strategy2.stopDay | - | string | No | Stop date, Format: mm:dd |
| strategy2.stopTime | - | string | No | Stop time, Format: HH:ss |
| strategy2.strategy | - | integer | Yes | strategy: 0=Disable，1=Charge,2=Discharge |
| strategy2 | - | object | No | - |
| strategy3.backupReserve | - | number | No | backupReserve |
| strategy3.daysOfEffectiveWeek.0 | - | array | No | Days Of Effective Week,Valuable：MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY，Multiple Choice |
| strategy3.power | - | integer | No | Battery charging or discharging power,Unit：W，The range of values is 0~inverter rated power |
| strategy3.soc | - | integer | No | Battery charging or discharging soc，Unit：%，The range of values is 0~100% |
| strategy3.startDay | - | string | No | Starting date, Format: mm:dd |
| strategy3.startTime | - | string | No | Starting time, Format: HH:ss |
| strategy3.stopDay | - | string | No | Stop date, Format: mm:dd |
| strategy3.stopTime | - | string | No | Stop time, Format: HH:ss |
| strategy3.strategy | - | integer | Yes | strategy: 0=Disable，1=Charge,2=Discharge |
| strategy3 | - | object | No | - |
| strategy4.backupReserve | - | number | No | backupReserve |
| strategy4.daysOfEffectiveWeek.0 | - | array | No | Days Of Effective Week,Valuable：MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY，Multiple Choice |
| strategy4.power | - | integer | No | Battery charging or discharging power,Unit：W，The range of values is 0~inverter rated power |
| strategy4.soc | - | integer | No | Battery charging or discharging soc，Unit：%，The range of values is 0~100% |
| strategy4.startDay | - | string | No | Starting date, Format: mm:dd |
| strategy4.startTime | - | string | No | Starting time, Format: HH:ss |
| strategy4.stopDay | - | string | No | Stop date, Format: mm:dd |
| strategy4.stopTime | - | string | No | Stop time, Format: HH:ss |
| strategy4.strategy | - | integer | Yes | strategy: 0=Disable，1=Charge,2=Discharge |
| strategy4 | - | object | No | - |
| templateName | - | string | No | template name |
| strategy5 | - | string | No | strategy5 , refer to strategy1 |
| strategy6 | - | string | No | strategy6 , refer to strategy1 |
| strategy7 | - | string | No | strategy7 , refer to strategy1 |
| strategy8 | - | string | No | strategy8 , refer to strategy1 |
| strategy9 | - | string | No | strategy9 , refer to strategy1 |
| strategy10 | - | string | No | strategy10 , refer to strategy1 |

**Authentication Method**

> Inherit from parent

**Response Example**

* OK(200)

```javascript
{
  "code": 998,
  "message": "The token has expired, please log in again",
  "data": {}
}
```

| Parameter Name | Example Value | Parameter Type | Description |
| --- | --- | ---- | ---- |
| code | - | integer | code |
| message | - | string | message |
| data | - | object | data |

* Created(201)

```javascript
No data
```

* Unauthorized(401)

```javascript
No data
```

* Forbidden(403)

```javascript
No data
```

* Not Found(404)

```javascript
No data
```

* token expire(200)

```javascript
No data
```

**Request Header Parameters**

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| Content-Type | application/json | string | Yes | - |
| Authorization | Bearer_eyJhbGciOiJIUzI1NiJ9.eyJkZW1vVXNlciI6ZmFsc2UsInN1YiI6IueuoeeQhuWRmCIsImF1ZCI6Ik56TTNORFF4TkRrd01UVTFPREUwTkE9PSIsIm5iZiI6MTcxMTY3NjY4NiwiaXNzIjoiRkxTLVNPTEFSLVNFUlZFUiIsImlkIjo3Mzc0NDE0OTAxNTU4MTQ0LCJleHAiOjE3MTQyNjg2ODYsImlhdCI6MTcxMTY3NjY4Nn0._l5VIYevtyv2Xc66S9w6fqmkECBFvLZPJYqjU07pObE | string | Yes | User token, which can be obtained from authentication and refreshing tokens. |
| Lang | en_US | string | Yes | Language, currently supports English en_US. |

**Query**

## Query detail

> Created by: Timesup

> Updated by: Timesup

> Created at: 2024-06-24 08:54:36

> Updated at: 2024-07-22 09:58:58

**The application server can call this interface to query the details of the economic mode strategy template through the Fsolar platform.**

**Interface Status**

> Completed

**Interface URL**

> /openApi/ecoStrategyTemplate/detail/{id}

**Request Method**

> GET

**Content-Type**

> form-data

**Request Header Parameters**

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| Content-Type | application/x-www-form-urlencoded | string | Yes | - |
| Authorization | Bearer_eyJhbGciOiJIUzI1NiJ9.eyJkZW1vVXNlciI6ZmFsc2UsInN1YiI6IueuoeeQhuWRmCIsImF1ZCI6Ik56TTNORFF4TkRrd01UVTFPREUwTkE9PSIsIm5iZiI6MTcxMTY3NjY4NiwiaXNzIjoiRkxTLVNPTEFSLVNFUlZFUiIsImlkIjo3Mzc0NDE0OTAxNTU4MTQ0LCJleHAiOjE3MTQyNjg2ODYsImlhdCI6MTcxMTY3NjY4Nn0._l5VIYevtyv2Xc66S9w6fqmkECBFvLZPJYqjU07pObE | string | Yes | User token, which can be obtained from authentication and refreshing tokens. |
| Lang | en_US | string | Yes | Language, currently supports English en_US. |

**Path Variables**

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| id | 123 | integer | Yes | Templateid |

**Request Body Parameters**

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| id | - | string | Yes | template id |

**Authentication Method**

> Inherit from parent

**Response Example**

* OK(200)

```javascript
{
	"code": 0,
	"message": "",
	"data": {
		"createTime": "",
		"id": 0,
		"modifyTime": "",
		"strategy1": {
			"backupReserve": "",
			"daysOfEffectiveWeek": [
				""
			],
			"power": 0,
			"soc": 0,
			"startDay": "",
			"startTime": "",
			"stopDay": "",
			"stopTime": "",
			"strategy": 0
		},
		"strategy2": {
			"backupReserve": "",
			"daysOfEffectiveWeek": [
				""
			],
			"power": 0,
			"soc": 0,
			"startDay": "",
			"startTime": "",
			"stopDay": "",
			"stopTime": "",
			"strategy": 0
		},
		"strategy3": {
			"backupReserve": "",
			"daysOfEffectiveWeek": [
				""
			],
			"power": 0,
			"soc": 0,
			"startDay": "",
			"startTime": "",
			"stopDay": "",
			"stopTime": "",
			"strategy": 0
		},
		"strategy4": {
			"backupReserve": "",
			"daysOfEffectiveWeek": [
				""
			],
			"power": 0,
			"soc": 0,
			"startDay": "",
			"startTime": "",
			"stopDay": "",
			"stopTime": "",
			"strategy": 0
		},
		
		"templateName": ""
	}
}
```

| Parameter Name | Example Value | Parameter Type | Description |
| --- | --- | ---- | ---- |
| code | - | integer | code |
| message | - | string | message |
| data.createTime | - | string | create Time |
| data.id | - | integer | template id |
| data.modifyTime | - | string | modify Time |
| data.strategy1.backupReserve | - | number | backupReserve |
| data.strategy1.daysOfEffectiveWeek.0 | - | array | Days Of Effective Week,Valuable：MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY，Multiple Choice |
| data.strategy1.power | - | integer | Battery charging or discharging power,Unit：W，The range of values is 0~inverter rated power |
| data.strategy1.soc | - | integer | Battery charging or discharging soc，Unit：%，The range of values is 0~100% |
| data.strategy1.startDay | - | string | Starting date, Format: mm:dd |
| data.strategy1.startTime | - | string | Starting time, Format: HH:ss |
| data.strategy1.stopDay | - | string | Stop date, Format: mm:dd |
| data.strategy1.stopTime | - | string | Stop time, Format: HH:ss |
| data.strategy1.strategy | - | integer | strategy: 0=Disable，1=Charge,2=Discharge |
| data.strategy1 | - | object | - |
| data.strategy2.backupReserve | - | number | backupReserve |
| data.strategy2.daysOfEffectiveWeek.0 | - | array | Days Of Effective Week,Valuable：MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY，Multiple Choice |
| data.strategy2.power | - | integer | Battery charging or discharging power,Unit：W，The range of values is 0~inverter rated power |
| data.strategy2.soc | - | integer | Battery charging or discharging soc，Unit：%，The range of values is 0~100% |
| data.strategy2.startDay | - | string | Starting date, Format: mm:dd |
| data.strategy2.startTime | - | string | Starting time, Format: HH:ss |
| data.strategy2.stopDay | - | string | Stop date, Format: mm:dd |
| data.strategy2.stopTime | - | string | Stop time, Format: HH:ss |
| data.strategy2.strategy | - | integer | strategy: 0=Disable，1=Charge,2=Discharge |
| data.strategy2 | - | object | - |
| data.strategy3.backupReserve | - | number | backupReserve |
| data.strategy3.daysOfEffectiveWeek.0 | - | array | Days Of Effective Week,Valuable：MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY，Multiple Choice |
| data.strategy3.power | - | integer | Battery charging or discharging power,Unit：W，The range of values is 0~inverter rated power |
| data.strategy3.soc | - | integer | Battery charging or discharging soc，Unit：%，The range of values is 0~100% |
| data.strategy3.startDay | - | string | Starting date, Format: mm:dd |
| data.strategy3.startTime | - | string | Starting time, Format: HH:ss |
| data.strategy3.stopDay | - | string | Stop date, Format: mm:dd |
| data.strategy3.stopTime | - | string | Stop time, Format: HH:ss |
| data.strategy3.strategy | - | integer | strategy: 0=Disable，1=Charge,2=Discharge |
| data.strategy3 | - | object | - |
| data.strategy4.backupReserve | - | number | backupReserve |
| data.strategy4.daysOfEffectiveWeek.0 | - | array | Days Of Effective Week,Valuable：MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY，Multiple Choice |
| data.strategy4.power | - | integer | Battery charging or discharging power,Unit：W，The range of values is 0~inverter rated power |
| data.strategy4.soc | - | integer | Battery charging or discharging soc，Unit：%，The range of values is 0~100% |
| data.strategy4.startDay | - | string | Starting date, Format: mm:dd |
| data.strategy4.startTime | - | string | Starting time, Format: HH:ss |
| data.strategy4.stopDay | - | string | Stop date, Format: mm:dd |
| data.strategy4.stopTime | - | string | Stop time, Format: HH:ss |
| data.strategy4.strategy | - | integer | strategy: 0=Disable，1=Charge,2=Discharge |
| data.strategy4 | - | object | - |
| data.templateName | - | string | template Name |
| data | - | object | - |
| data.strategy5 | data.strategy5, refer to data.strategy1 | object | - |
| data.strategy6 | data.strategy6, refer to data.strategy1 | object | - |
| data.strategy7 | data.strategy7, refer to data.strategy1 | string | - |
| data.strategy8 | data.strategy8, refer to data.strategy1 | string | - |
| data.strategy9 | data.strategy9, refer to data.strategy1 | string | - |
| data.strategy10 | data.strategy10, refer to data.strategy1 | string | - |

* Unauthorized(401)

```javascript
No data
```

* Forbidden(403)

```javascript
No data
```

* Not Found(404)

```javascript
No data
```

* token expire(200)

```javascript
{
  "code": 998,
  "message": "The token has expired, please log in again",
  "data": {}
}
```

**Request Header Parameters**

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| Content-Type | application/x-www-form-urlencoded | string | Yes | - |
| Authorization | Bearer_eyJhbGciOiJIUzI1NiJ9.eyJkZW1vVXNlciI6ZmFsc2UsInN1YiI6IueuoeeQhuWRmCIsImF1ZCI6Ik56TTNORFF4TkRrd01UVTFPREUwTkE9PSIsIm5iZiI6MTcxMTY3NjY4NiwiaXNzIjoiRkxTLVNPTEFSLVNFUlZFUiIsImlkIjo3Mzc0NDE0OTAxNTU4MTQ0LCJleHAiOjE3MTQyNjg2ODYsImlhdCI6MTcxMTY3NjY4Nn0._l5VIYevtyv2Xc66S9w6fqmkECBFvLZPJYqjU07pObE | string | Yes | User token, which can be obtained from authentication and refreshing tokens. |
| Lang | en_US | string | Yes | Language, currently supports English en_US. |

**Query**

## Delete Economic Model Strategy Template

> Created by: Timesup

> Updated by: Timesup

> Created at: 2024-06-24 08:54:36

> Updated at: 2024-06-26 15:35:09

**The application server can call this interface to delete the economic mode policy template through the Fsolar platform.**

**Interface Status**

> Completed

**Interface URL**

> /openApi/ecoStrategyTemplate/delete/{id}

**Request Method**

> GET

**Content-Type**

> form-data

**Request Header Parameters**

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| Content-Type | application/x-www-form-urlencoded | string | Yes | - |
| Authorization | Bearer_eyJhbGciOiJIUzI1NiJ9.eyJkZW1vVXNlciI6ZmFsc2UsInN1YiI6IueuoeeQhuWRmCIsImF1ZCI6Ik56TTNORFF4TkRrd01UVTFPREUwTkE9PSIsIm5iZiI6MTcxMTY3NjY4NiwiaXNzIjoiRkxTLVNPTEFSLVNFUlZFUiIsImlkIjo3Mzc0NDE0OTAxNTU4MTQ0LCJleHAiOjE3MTQyNjg2ODYsImlhdCI6MTcxMTY3NjY4Nn0._l5VIYevtyv2Xc66S9w6fqmkECBFvLZPJYqjU07pObE | string | Yes | User token, which can be obtained from authentication and refreshing tokens. |
| Lang | en_US | string | Yes | Language, currently supports English en_US. |

**Path Variables**

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| id | 123 | integer | Yes | template id |

**Request Body Parameters**

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| id | - | string | Yes | template id |

**Authentication Method**

> Inherit from parent

**Response Example**

* OK(200)

```javascript
{
	"code": 0,
	"message": "",
	"data": {}
}
```

| Parameter Name | Example Value | Parameter Type | Description |
| --- | --- | ---- | ---- |
| code | - | integer | code |
| message | - | string | message |
| data | - | object | data |

* Unauthorized(401)

```javascript
No data
```

* Forbidden(403)

```javascript
No data
```

* Not Found(404)

```javascript
No data
```

* token expire(200)

```javascript
{
  "code": 998,
  "message": "The token has expired, please log in again",
  "data": {}
}
```

**Request Header Parameters**

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| Content-Type | application/x-www-form-urlencoded | string | Yes | - |
| Authorization | Bearer_eyJhbGciOiJIUzI1NiJ9.eyJkZW1vVXNlciI6ZmFsc2UsInN1YiI6IueuoeeQhuWRmCIsImF1ZCI6Ik56TTNORFF4TkRrd01UVTFPREUwTkE9PSIsIm5iZiI6MTcxMTY3NjY4NiwiaXNzIjoiRkxTLVNPTEFSLVNFUlZFUiIsImlkIjo3Mzc0NDE0OTAxNTU4MTQ0LCJleHAiOjE3MTQyNjg2ODYsImlhdCI6MTcxMTY3NjY4Nn0._l5VIYevtyv2Xc66S9w6fqmkECBFvLZPJYqjU07pObE | string | Yes | User token, which can be obtained from authentication and refreshing tokens. |
| Lang | en_US | string | Yes | Language, currently supports English en_US. |

**Query**

# Economic Model Task Management

> Created by: Timesup

> Updated by: Timesup

> Created at: 2024-06-22 04:19:50

> Updated at: 2024-06-27 03:12:13

**Economic mode task management is mainly aimed at scenarios where multiple devices are set in the same economic mode in batches, which can enable dealers to conveniently control the equipment.**

**Directory Header Parameters**

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| No parameters |

**Directory Query Parameters**

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| No parameters |

**Directory Body Parameters**

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| No parameters |

**Directory Authentication Info**

> Inherit from parent

**Query**

## Add Economic Mode Task

> Created by: Timesup

> Updated by: Timesup

> Created at: 2024-06-22 04:19:50

> Updated at: 2024-06-27 03:16:51

**The application server can call this interface to add economy mode tasks on the Fsolar platform.**

**Interface Status**

> Completed

**Interface URL**

> /openApi/ecoTask/save

**Request Method**

> POST

**Content-Type**

> json

**Request Header Parameters**

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| Content-Type | application/json | string | Yes | - |
| Authorization | Bearer_eyJhbGciOiJIUzI1NiJ9.eyJkZW1vVXNlciI6ZmFsc2UsInN1YiI6IueuoeeQhuWRmCIsImF1ZCI6Ik56TTNORFF4TkRrd01UVTFPREUwTkE9PSIsIm5iZiI6MTcxMTY3NjY4NiwiaXNzIjoiRkxTLVNPTEFSLVNFUlZFUiIsImlkIjo3Mzc0NDE0OTAxNTU4MTQ0LCJleHAiOjE3MTQyNjg2ODYsImlhdCI6MTcxMTY3NjY4Nn0._l5VIYevtyv2Xc66S9w6fqmkECBFvLZPJYqjU07pObE | string | Yes | User token, which can be obtained from authentication and refreshing tokens. |
| Lang | en_US | string | Yes | Language, currently supports English en_US. |

**Request Body Parameters**

```javascript
{
	"targetList": [
		{
			"deviceId": 0
		}
	],
	"taskName": "",
	"taskType": "",
	"templateId": 0
}
```

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| targetList.deviceId | 020505004821130001 | integer | Yes | Device ID，Required, will be returned when adding devices |
| taskName | batch west region setting | string | Yes | Task Nmae |
| taskType | device | string | Yes | Task Type：device |
| templateId | 123 | integer | Yes | Template ID |

**Authentication Method**

> Inherit from parent

**Response Example**

* OK(200)

```javascript
{
	"code": 200,
	"message": "",
	"data": {}
}
```

| Parameter Name | Example Value | Parameter Type | Description |
| --- | --- | ---- | ---- |
| code | - | integer | code |
| message | - | string | message |
| data | - | object | data |

* token expired(200)

```javascript
{
  "code": 998,
  "message": "The token has expired, please log in again",
  "data": {}
}
```

**Request Header Parameters**

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| Content-Type | application/json | string | Yes | - |
| Authorization | Bearer_eyJhbGciOiJIUzI1NiJ9.eyJkZW1vVXNlciI6ZmFsc2UsInN1YiI6IueuoeeQhuWRmCIsImF1ZCI6Ik56TTNORFF4TkRrd01UVTFPREUwTkE9PSIsIm5iZiI6MTcxMTY3NjY4NiwiaXNzIjoiRkxTLVNPTEFSLVNFUlZFUiIsImlkIjo3Mzc0NDE0OTAxNTU4MTQ0LCJleHAiOjE3MTQyNjg2ODYsImlhdCI6MTcxMTY3NjY4Nn0._l5VIYevtyv2Xc66S9w6fqmkECBFvLZPJYqjU07pObE | string | Yes | User token, which can be obtained from authentication and refreshing tokens. |
| Lang | en_US | string | Yes | Language, currently supports English en_US. |

**Query**

## Modify Economic Mode Task

> Created by: Timesup

> Updated by: Timesup

> Created at: 2024-06-22 04:19:50

> Updated at: 2024-06-27 03:21:42

**The application server can call this interface to modify economic mode tasks on the Fsolar platform.**

**Interface Status**

> Completed

**Interface URL**

> /openApi/ecoTask/update

**Request Method**

> POST

**Content-Type**

> json

**Request Header Parameters**

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| Content-Type | application/json | string | Yes | - |
| Authorization | Bearer_eyJhbGciOiJIUzI1NiJ9.eyJkZW1vVXNlciI6ZmFsc2UsInN1YiI6IueuoeeQhuWRmCIsImF1ZCI6Ik56TTNORFF4TkRrd01UVTFPREUwTkE9PSIsIm5iZiI6MTcxMTY3NjY4NiwiaXNzIjoiRkxTLVNPTEFSLVNFUlZFUiIsImlkIjo3Mzc0NDE0OTAxNTU4MTQ0LCJleHAiOjE3MTQyNjg2ODYsImlhdCI6MTcxMTY3NjY4Nn0._l5VIYevtyv2Xc66S9w6fqmkECBFvLZPJYqjU07pObE | string | Yes | User token, which can be obtained from authentication and refreshing tokens. |
| Lang | en_US | string | Yes | Language, currently supports English en_US. |

**Request Body Parameters**

```javascript
{
	"id": 0,
	"targetList": [
		{
			"deviceId": 0
		}
	],
	"taskName": "",
	"taskType": "",
	"templateId": 0
}
```

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| id | 1 | integer | Yes | Task Id |
| targetList.deviceId | 2 | integer | Yes | Device ID |
| taskName | testTask | string | Yes | Task Nmae |
| taskType | device | string | Yes | Task Type，Default device |
| templateId | - | integer | Yes | Template ID |

**Authentication Method**

> Inherit from parent

**Response Example**

* OK(200)

```javascript
{
	"code": 200,
	"message": "",
	"data": {}
}
```

| Parameter Name | Example Value | Parameter Type | Description |
| --- | --- | ---- | ---- |
| code | - | integer | code |
| message | - | string | message |
| data | - | object | data |

* token expired(200)

```javascript
{
  "code": 998,
  "message": "The token has expired, please log in again",
  "data": {}
}
```

**Request Header Parameters**

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| Content-Type | application/json | string | Yes | - |
| Authorization | Bearer_eyJhbGciOiJIUzI1NiJ9.eyJkZW1vVXNlciI6ZmFsc2UsInN1YiI6IueuoeeQhuWRmCIsImF1ZCI6Ik56TTNORFF4TkRrd01UVTFPREUwTkE9PSIsIm5iZiI6MTcxMTY3NjY4NiwiaXNzIjoiRkxTLVNPTEFSLVNFUlZFUiIsImlkIjo3Mzc0NDE0OTAxNTU4MTQ0LCJleHAiOjE3MTQyNjg2ODYsImlhdCI6MTcxMTY3NjY4Nn0._l5VIYevtyv2Xc66S9w6fqmkECBFvLZPJYqjU07pObE | string | Yes | User token, which can be obtained from authentication and refreshing tokens. |
| Lang | en_US | string | Yes | Language, currently supports English en_US. |

**Query**

## Paging economic mode query task

> Created by: Timesup

> Updated by: Timesup

> Created at: 2024-06-22 04:19:50

> Updated at: 2024-06-27 03:30:15

**The application server can call this interface to page query economic mode tasks on the Fsolar platform.**

**Interface Status**

> Completed

**Interface URL**

> /openApi/ecoTask/list

**Request Method**

> POST

**Content-Type**

> json

**Request Header Parameters**

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| Content-Type | application/json | string | Yes | - |
| Authorization | Bearer_eyJhbGciOiJIUzI1NiJ9.eyJkZW1vVXNlciI6ZmFsc2UsInN1YiI6IueuoeeQhuWRmCIsImF1ZCI6Ik56TTNORFF4TkRrd01UVTFPREUwTkE9PSIsIm5iZiI6MTcxMTY3NjY4NiwiaXNzIjoiRkxTLVNPTEFSLVNFUlZFUiIsImlkIjo3Mzc0NDE0OTAxNTU4MTQ0LCJleHAiOjE3MTQyNjg2ODYsImlhdCI6MTcxMTY3NjY4Nn0._l5VIYevtyv2Xc66S9w6fqmkECBFvLZPJYqjU07pObE | string | Yes | User token, which can be obtained from authentication and refreshing tokens. |
| Lang | en_US | string | Yes | Language, currently supports English en_US. |

**Request Body Parameters**

```javascript
{

	"pageNum": 1,
	"pageSize": 10,
	"taskName": "",
	"taskType": "",
	"templateId": 0
}
```

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| pageNum | 1 | integer | Yes | Page numbers, starting from 1 |
| pageSize | 10 | integer | Yes | Number of entries per page, maximum of 300 |
| taskName | - | string | No | Task Nmae |
| taskType | - | string | No | Task Type，Default device |
| templateId | - | integer | No | Template ID |

**Authentication Method**

> Inherit from parent

**Response Example**

* OK(200)

```javascript
{
	"data": {},
	"total": 0,
	"totalPage": 0,
	"currentPage": 0,
	"pageSize": 0,
	"dataList": [
		{
			"createTime": "",
			"detailListVOList": [
				{
					"alias": "",
					"commandId": 0,
					"commandStatus": 0,
					"deviceId": 0,
					"deviceSn": "",
					"id": 0,
					
					"taskId": 0
				}
			],
			"failCount": 0,
			"id": 0,
			"modifyTime": "",
			"runTaskRecordId": 0,
			"runType": 0,
			"successCount": 0,
			"taskName": "",
			"taskStatus": 0,
			"taskType": "",
			"templateId": 0,
			"templateName": ""
		}
	]
}
```

| Parameter Name | Example Value | Parameter Type | Description |
| --- | --- | ---- | ---- |
| data | - | object | Data |
| total | - | integer | Total number of records |
| totalPage | - | integer | Total Page |
| currentPage | - | integer | Current Page |
| pageSize | - | integer | Page Size |
| dataList.createTime | - | string | Creation time |
| dataList.detailListVOList.alias | - | string | Device Alias |
| dataList.detailListVOList.commandId | - | integer | Command Id |
| dataList.detailListVOList.commandStatus | - | integer | Command status, 2=issued, waiting for reply, 1=device received and responded successfully, 0=device failed response result or device did not respond within 2 minutes after sending |
| dataList.detailListVOList.deviceId | - | integer | Device ID |
| dataList.detailListVOList.deviceSn | - | string | Device serial number |
| dataList.detailListVOList.id | - | integer | Task detail ID |
| dataList.detailListVOList.taskId | - | integer | Task Id |
| dataList.failCount | - | integer | Number of failures |
| dataList.id | - | integer | Task Id |
| dataList.modifyTime | - | string | Modification time |
| dataList.runTaskRecordId | - | integer | Run Task Record ID |
| dataList.runType | - | integer | Run type: 0=default type, 1=failed resend |
| dataList.successCount | - | integer | Number of successes |
| dataList.taskName | - | string | Task Nmae |
| dataList.taskStatus | - | integer | Running status: 0=Running, 1=Done |
| dataList.taskType | - | string | task Type, Default: device |
| dataList.templateId | - | integer | Template ID |
| dataList.templateName | - | string | Template Name |

* token expired(200)

```javascript
{
  "code": 998,
  "message": "The token has expired, please log in again",
  "data": {}
}
```

**Request Header Parameters**

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| Content-Type | application/json | string | Yes | - |
| Authorization | Bearer_eyJhbGciOiJIUzI1NiJ9.eyJkZW1vVXNlciI6ZmFsc2UsInN1YiI6IueuoeeQhuWRmCIsImF1ZCI6Ik56TTNORFF4TkRrd01UVTFPREUwTkE9PSIsIm5iZiI6MTcxMTY3NjY4NiwiaXNzIjoiRkxTLVNPTEFSLVNFUlZFUiIsImlkIjo3Mzc0NDE0OTAxNTU4MTQ0LCJleHAiOjE3MTQyNjg2ODYsImlhdCI6MTcxMTY3NjY4Nn0._l5VIYevtyv2Xc66S9w6fqmkECBFvLZPJYqjU07pObE | string | Yes | User token, which can be obtained from authentication and refreshing tokens. |
| Lang | en_US | string | Yes | Language, currently supports English en_US. |

**Query**

## Delete Economic Mode Task

> Created by: Timesup

> Updated by: Timesup

> Created at: 2024-06-22 04:19:50

> Updated at: 2024-06-27 03:31:53

**The application server can call this interface to delete economic mode tasks on the Fsolar platform.**

**Interface Status**

> Completed

**Interface URL**

> /openApi/ecoTask/delete/{id}

**Request Method**

> GET

**Content-Type**

> none

**Request Header Parameters**

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| Content-Type | application/x-www-form-urlencoded | string | Yes | - |
| Authorization | Bearer_eyJhbGciOiJIUzI1NiJ9.eyJkZW1vVXNlciI6ZmFsc2UsInN1YiI6IueuoeeQhuWRmCIsImF1ZCI6Ik56TTNORFF4TkRrd01UVTFPREUwTkE9PSIsIm5iZiI6MTcxMTY3NjY4NiwiaXNzIjoiRkxTLVNPTEFSLVNFUlZFUiIsImlkIjo3Mzc0NDE0OTAxNTU4MTQ0LCJleHAiOjE3MTQyNjg2ODYsImlhdCI6MTcxMTY3NjY4Nn0._l5VIYevtyv2Xc66S9w6fqmkECBFvLZPJYqjU07pObE | string | Yes | User token, which can be obtained from authentication and refreshing tokens. |
| Lang | en_US | string | Yes | Language, currently supports English en_US. |

**Path Variables**

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| id | - | integer | Yes | id |

**Authentication Method**

> Inherit from parent

**Response Example**

* OK(200)

```javascript
{
	"code": 0,
	"message": "",
	"data": {}
}
```

| Parameter Name | Example Value | Parameter Type | Description |
| --- | --- | ---- | ---- |
| code | - | integer | code |
| message | - | string | message |
| data | - | object | data |

* token expire(200)

```javascript
{
  "code": 998,
  "message": "The token has expired, please log in again",
  "data": {}
}
```

**Request Header Parameters**

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| Content-Type | application/x-www-form-urlencoded | string | Yes | - |
| Authorization | Bearer_eyJhbGciOiJIUzI1NiJ9.eyJkZW1vVXNlciI6ZmFsc2UsInN1YiI6IueuoeeQhuWRmCIsImF1ZCI6Ik56TTNORFF4TkRrd01UVTFPREUwTkE9PSIsIm5iZiI6MTcxMTY3NjY4NiwiaXNzIjoiRkxTLVNPTEFSLVNFUlZFUiIsImlkIjo3Mzc0NDE0OTAxNTU4MTQ0LCJleHAiOjE3MTQyNjg2ODYsImlhdCI6MTcxMTY3NjY4Nn0._l5VIYevtyv2Xc66S9w6fqmkECBFvLZPJYqjU07pObE | string | Yes | User token, which can be obtained from authentication and refreshing tokens. |
| Lang | en_US | string | Yes | Language, currently supports English en_US. |

**Query**

## Running Economic Mode Tasks

> Created by: Timesup

> Updated by: Timesup

> Created at: 2024-06-22 04:19:50

> Updated at: 2024-06-27 03:35:32

**The application server can call this interface to run economy mode tasks through the Fsolar platform. The task of running the economic mode is actually to set the economic mode parameters corresponding to the associated template to the machine. The task will be completed within two minutes. The status during operation can be queried through the "Query Economic Mode Task Runtime Details" API**

**Interface Status**

> Completed

**Interface URL**

> /openApi/ecoTask/run

**Request Method**

> POST

**Content-Type**

> json

**Request Header Parameters**

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| Content-Type | application/json | string | Yes | - |
| Authorization | Bearer_eyJhbGciOiJIUzI1NiJ9.eyJkZW1vVXNlciI6ZmFsc2UsInN1YiI6IueuoeeQhuWRmCIsImF1ZCI6Ik56TTNORFF4TkRrd01UVTFPREUwTkE9PSIsIm5iZiI6MTcxMTY3NjY4NiwiaXNzIjoiRkxTLVNPTEFSLVNFUlZFUiIsImlkIjo3Mzc0NDE0OTAxNTU4MTQ0LCJleHAiOjE3MTQyNjg2ODYsImlhdCI6MTcxMTY3NjY4Nn0._l5VIYevtyv2Xc66S9w6fqmkECBFvLZPJYqjU07pObE | string | Yes | User token, which can be obtained from authentication and refreshing tokens. |
| Lang | en_US | string | Yes | Language, currently supports English en_US. |

**Request Body Parameters**

```javascript
{
	"runTaskRecordId": 0,
	"runType": 0,
	"taskId": 0
}
```

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| runTaskRecordId | 1213 | integer | No | Run Task Record ID，runType=1 Required for failed resend |
| runType | 1 | integer | Yes | Run type: 0=default type, 1=failed resend |
| taskId | 23 | integer | Yes | Task Id |

**Authentication Method**

> Inherit from parent

**Response Example**

* OK(200)

```javascript
{
	"code": 0,
	"message": "",
	"data": {
		"createTime": "",
		"detailListVOList": [
			{
				"alias": "",
				"commandId": 0,
				"commandStatus": 0,
				"deviceId": 0,
				"deviceSn": "",
				"id": 0,
				"taskId": 0
			}
		],
		"failCount": 0,
		"id": 0,
		"modifyTime": "",
		"runTaskRecordId": 0,
		"runType": 0,
		"successCount": 0,
		"taskName": "",
		"taskStatus": 0,
		"taskType": "",
		"templateId": 0,
		"templateName": ""
	}
}
```

| Parameter Name | Example Value | Parameter Type | Description |
| --- | --- | ---- | ---- |
| code | - | integer | Response code |
| message | - | string | Response message |
| data.createTime | - | string | Creation time |
| data.detailListVOList.alias | - | string | Device Alias |
| data.detailListVOList.commandId | - | integer | Command Id |
| data.detailListVOList.commandStatus | - | integer | Command status, 2=issued, waiting for reply, 1=device received and responded successfully, 0=device failed response result or device did not respond within 2 minutes after sending |
| data.detailListVOList.deviceId | - | integer | Device ID |
| data.detailListVOList.deviceSn | - | string | Device SN Code |
| data.detailListVOList.id | - | integer | Task Detail ID |
| data.detailListVOList.taskId | - | integer | Task Id |
| data.failCount | - | integer | Number of failures |
| data.id | - | integer | Task id |
| data.modifyTime | - | string | Modification time |
| data.runTaskRecordId | - | integer | Run Record ID |
| data.runType | - | integer | Run type: 0=default type, 1=failed resend |
| data.successCount | - | integer | Number of successes |
| data.taskName | - | string | Task Name |
| data.taskStatus | - | integer | Running status: 0=Running, 1=Done |
| data.taskType | - | string | - |
| data.templateId | - | integer | Template id |
| data.templateName | - | string | Template Name |
| data | - | object | - |

* token expired(200)

```javascript
{
  "code": 998,
  "message": "The token has expired, please log in again",
  "data": {}
}
```

**Request Header Parameters**

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| Content-Type | application/json | string | Yes | - |
| Authorization | Bearer_eyJhbGciOiJIUzI1NiJ9.eyJkZW1vVXNlciI6ZmFsc2UsInN1YiI6IueuoeeQhuWRmCIsImF1ZCI6Ik56TTNORFF4TkRrd01UVTFPREUwTkE9PSIsIm5iZiI6MTcxMTY3NjY4NiwiaXNzIjoiRkxTLVNPTEFSLVNFUlZFUiIsImlkIjo3Mzc0NDE0OTAxNTU4MTQ0LCJleHAiOjE3MTQyNjg2ODYsImlhdCI6MTcxMTY3NjY4Nn0._l5VIYevtyv2Xc66S9w6fqmkECBFvLZPJYqjU07pObE | string | Yes | User token, which can be obtained from authentication and refreshing tokens. |
| Lang | en_US | string | Yes | Language, currently supports English en_US. |

**Query**

## Query economic mode task runtime details

> Created by: Timesup

> Updated by: Timesup

> Created at: 2024-06-22 04:19:50

> Updated at: 2024-06-27 03:36:26

**The application server can call this interface to view the runtime status of economic mode tasks。**

**Interface Status**

> Completed

**Interface URL**

> /openApi/ecoTask/getRunningDetail

**Request Method**

> POST

**Content-Type**

> json

**Request Header Parameters**

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| Content-Type | application/json | string | Yes | - |
| Authorization | Bearer_eyJhbGciOiJIUzI1NiJ9.eyJkZW1vVXNlciI6ZmFsc2UsInN1YiI6IueuoeeQhuWRmCIsImF1ZCI6Ik56TTNORFF4TkRrd01UVTFPREUwTkE9PSIsIm5iZiI6MTcxMTY3NjY4NiwiaXNzIjoiRkxTLVNPTEFSLVNFUlZFUiIsImlkIjo3Mzc0NDE0OTAxNTU4MTQ0LCJleHAiOjE3MTQyNjg2ODYsImlhdCI6MTcxMTY3NjY4Nn0._l5VIYevtyv2Xc66S9w6fqmkECBFvLZPJYqjU07pObE | string | Yes | User token, which can be obtained from authentication and refreshing tokens. |
| Lang | en_US | string | Yes | Language, currently supports English en_US. |

**Request Body Parameters**

```javascript
{
	"runTaskRecordId": 0,
	"taskId": 0
}
```

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| runTaskRecordId | 123 | integer | No | The task record ID is required to view the completed running result. When calling the "Run Economy Mode Task", the task record ID will be returned |
| taskId | 1234 | integer | No | Task Id |

**Authentication Method**

> Inherit from parent

**Response Example**

* OK(200)

```javascript
{
	"code": 0,
	"message": "",
	"data": {
		"createTime": "",
		"detailListVOList": [
			{
				"alias": "",
				"commandId": 0,
				"commandStatus": 0,
				"deviceId": 0,
				"deviceSn": "",
				"id": 0,
				"taskId": 0
			}
		],
		"failCount": 0,
		"id": 0,
		"modifyTime": "",
		"runTaskRecordId": 0,
		"runType": 0,
		"successCount": 0,
		"taskName": "",
		"taskStatus": 0,
		"taskType": "",
		"templateId": 0,
		"templateName": ""
	}
}
```

| Parameter Name | Example Value | Parameter Type | Description |
| --- | --- | ---- | ---- |
| code | - | integer | Response code |
| message | - | string | Response message |
| data.createTime | - | string | Returned data |
| data.detailListVOList.alias | - | string | Device Alias |
| data.detailListVOList.commandId | - | integer | Command Id |
| data.detailListVOList.commandStatus | - | integer | Command status, 2=issued, waiting for reply, 1=device received and responded successfully, 0=device failed response result or device did not respond within 2 minutes after sending |
| data.detailListVOList.deviceId | - | integer | Device id |
| data.detailListVOList.deviceSn | - | string | Device SN |
| data.detailListVOList.id | - | integer | Detail id |
| data.detailListVOList.taskId | - | integer | Task id |
| data.failCount | - | integer | Number of failures |
| data.id | - | integer | Taskid |
| data.modifyTime | - | string | Modification time |
| data.runTaskRecordId | - | integer | Task Record Id |
| data.runType | - | integer | Run type: 0=default type, 1=failed resend |
| data.successCount | - | integer | Number of successes |
| data.taskName | - | string | Task Name |
| data.taskStatus | - | integer | Running status: 0=Running, 1=Done |
| data.taskType | - | string | - |
| data.templateId | - | integer | Template id |
| data.templateName | - | string | Template Name |
| data | - | object | - |

* token expired(200)

```javascript
{
  "code": 998,
  "message": "The token has expired, please log in again",
  "data": {}
}
```

**Request Header Parameters**

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| Content-Type | application/json | string | Yes | - |
| Authorization | Bearer_eyJhbGciOiJIUzI1NiJ9.eyJkZW1vVXNlciI6ZmFsc2UsInN1YiI6IueuoeeQhuWRmCIsImF1ZCI6Ik56TTNORFF4TkRrd01UVTFPREUwTkE9PSIsIm5iZiI6MTcxMTY3NjY4NiwiaXNzIjoiRkxTLVNPTEFSLVNFUlZFUiIsImlkIjo3Mzc0NDE0OTAxNTU4MTQ0LCJleHAiOjE3MTQyNjg2ODYsImlhdCI6MTcxMTY3NjY4Nn0._l5VIYevtyv2Xc66S9w6fqmkECBFvLZPJYqjU07pObE | string | Yes | User token, which can be obtained from authentication and refreshing tokens. |
| Lang | en_US | string | Yes | Language, currently supports English en_US. |

**Query**

## Query economic mode task details

> Created by: Timesup

> Updated by: Timesup

> Created at: 2024-06-22 04:19:50

> Updated at: 2024-06-27 03:38:22

**Query economic mode task details**

**Interface Status**

> Completed

**Interface URL**

> /openApi/ecoTask/getDetail

**Request Method**

> POST

**Content-Type**

> json

**Request Header Parameters**

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| Content-Type | application/json | string | Yes | - |
| Authorization | Bearer_eyJhbGciOiJIUzI1NiJ9.eyJkZW1vVXNlciI6ZmFsc2UsInN1YiI6IueuoeeQhuWRmCIsImF1ZCI6Ik56TTNORFF4TkRrd01UVTFPREUwTkE9PSIsIm5iZiI6MTcxMTY3NjY4NiwiaXNzIjoiRkxTLVNPTEFSLVNFUlZFUiIsImlkIjo3Mzc0NDE0OTAxNTU4MTQ0LCJleHAiOjE3MTQyNjg2ODYsImlhdCI6MTcxMTY3NjY4Nn0._l5VIYevtyv2Xc66S9w6fqmkECBFvLZPJYqjU07pObE | string | Yes | User token, which can be obtained from authentication and refreshing tokens. |
| Lang | en_US | string | Yes | Language, currently supports English en_US. |

**Request Body Parameters**

```javascript
{
	"taskId": 0
}
```

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| taskId | - | integer | No | Task ID |

**Authentication Method**

> Inherit from parent

**Response Example**

* OK(200)

```javascript
{
	"code": 0,
	"message": "",
	"data": [
		{
			"deviceId": 0,
			"deviceSn": "",
			"id": 0,
			"taskId": 0
		}
	]
}
```

| Parameter Name | Example Value | Parameter Type | Description |
| --- | --- | ---- | ---- |
| code | - | integer | Response code |
| message | - | string | Response message |
| data.deviceId | - | integer | Device ID |
| data.deviceSn | - | string | Device SN |
| data.id | - | integer | Detail ID |
| data.taskId | - | integer | Task ID |

* Created(200)

```javascript
{
  "code": 998,
  "message": "The token has expired, please log in again",
  "data": {}
}
```

**Request Header Parameters**

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| Content-Type | application/json | string | Yes | - |
| Authorization | Bearer_eyJhbGciOiJIUzI1NiJ9.eyJkZW1vVXNlciI6ZmFsc2UsInN1YiI6IueuoeeQhuWRmCIsImF1ZCI6Ik56TTNORFF4TkRrd01UVTFPREUwTkE9PSIsIm5iZiI6MTcxMTY3NjY4NiwiaXNzIjoiRkxTLVNPTEFSLVNFUlZFUiIsImlkIjo3Mzc0NDE0OTAxNTU4MTQ0LCJleHAiOjE3MTQyNjg2ODYsImlhdCI6MTcxMTY3NjY4Nn0._l5VIYevtyv2Xc66S9w6fqmkECBFvLZPJYqjU07pObE | string | Yes | User token, which can be obtained from authentication and refreshing tokens. |
| Lang | en_US | string | Yes | Language, currently supports English en_US. |

**Query**

# Economic mode task operation record

> Created by: Timesup

> Updated by: typhoon

> Created at: 2024-06-22 04:19:50

> Updated at: 2024-06-27 03:10:44

**Economic mode task operation record**

**Directory Header Parameters**

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| No parameters |

**Directory Query Parameters**

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| No parameters |

**Directory Body Parameters**

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| No parameters |

**Directory Authentication Info**

> Inherit from parent

**Query**

## Pagination query of economic mode task operation record table data

> Created by: Timesup

> Updated by: Timesup

> Created at: 2024-06-22 04:19:50

> Updated at: 2024-06-27 03:59:58

**The application server can call this interface to view the running records of economic mode tasks in a paginated manner**

**Interface Status**

> Completed

**Interface URL**

> /openApi/ecoTaskRunRecord/list

**Request Method**

> POST

**Content-Type**

> json

**Request Header Parameters**

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| Content-Type | application/json | string | Yes | - |
| Authorization | Bearer_eyJhbGciOiJIUzI1NiJ9.eyJkZW1vVXNlciI6ZmFsc2UsInN1YiI6IueuoeeQhuWRmCIsImF1ZCI6Ik56TTNORFF4TkRrd01UVTFPREUwTkE9PSIsIm5iZiI6MTcxMTY3NjY4NiwiaXNzIjoiRkxTLVNPTEFSLVNFUlZFUiIsImlkIjo3Mzc0NDE0OTAxNTU4MTQ0LCJleHAiOjE3MTQyNjg2ODYsImlhdCI6MTcxMTY3NjY4Nn0._l5VIYevtyv2Xc66S9w6fqmkECBFvLZPJYqjU07pObE | string | Yes | User token, which can be obtained from authentication and refreshing tokens. |
| Lang | en_US | string | Yes | Language, currently supports English en_US. |

**Request Body Parameters**

```javascript
{
	
	"pageNum": 1,
	"pageSize": 10,
	"runType": 0,
	"taskId": 0,
	"taskName": 0,
	"taskStatus": 0
}
```

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| pageNum | 1 | integer | Yes | Page number, starting from 1 |
| pageSize | 10 | integer | Yes | Number of entries per page, maximum of 1000 |
| runType | - | integer | No | Operation type: 0=normal operation, 1=failed resend |
| taskId | - | integer | No | Task Id |
| taskName | - | integer | No | Task name |
| taskStatus | - | integer | No | Running status: 0=running, 1=done |

**Authentication Method**

> Inherit from parent

**Response Example**

* OK(200)

```javascript
{
	"data": {},
	"total": 0,
	"totalPage": 0,
	"currentPage": 0,
	"pageSize": 0,
	"dataList": [
		{
			"createTime": "",
			"failCount": 0,
			"id": 0,
			"modifyTime": "",
			"runType": 0,
			"successCount": 0,
			"taskId": 0,
			"taskName": "",
			"taskStatus": 0,
			"taskType": "",
			"templateId": 0
		}
	]
}
```

| Parameter Name | Example Value | Parameter Type | Description |
| --- | --- | ---- | ---- |
| data | - | object | Response code |
| total | - | integer | Total number of records |
| totalPage | - | integer | Total Page |
| currentPage | - | integer | Current Page |
| pageSize | - | integer | Page Size |
| dataList.createTime | - | string | Creation time |
| dataList.failCount | - | integer | Number of failures |
| dataList.id | - | integer | ID |
| dataList.modifyTime | - | string | Modification time |
| dataList.runType | - | integer | Operation type: 0=normal operation, 1=failed resend |
| dataList.successCount | - | integer | Number of successes |
| dataList.taskId | - | integer | Task Id |
| dataList.taskName | - | string | Task Name |
| dataList.taskStatus | - | integer | Running status: 0=Running, 1=Done |
| dataList.taskType | - | string | Task Type，Default device |
| dataList.templateId | - | integer | Template Id |

* token expired(200)

```javascript
{
  "code": 998,
  "message": "The token has expired, please log in again",
  "data": {}
}
```

**Request Header Parameters**

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| Content-Type | application/json | string | Yes | - |
| Authorization | Bearer_eyJhbGciOiJIUzI1NiJ9.eyJkZW1vVXNlciI6ZmFsc2UsInN1YiI6IueuoeeQhuWRmCIsImF1ZCI6Ik56TTNORFF4TkRrd01UVTFPREUwTkE9PSIsIm5iZiI6MTcxMTY3NjY4NiwiaXNzIjoiRkxTLVNPTEFSLVNFUlZFUiIsImlkIjo3Mzc0NDE0OTAxNTU4MTQ0LCJleHAiOjE3MTQyNjg2ODYsImlhdCI6MTcxMTY3NjY4Nn0._l5VIYevtyv2Xc66S9w6fqmkECBFvLZPJYqjU07pObE | string | Yes | User token, which can be obtained from authentication and refreshing tokens. |
| Lang | en_US | string | Yes | Language, currently supports English en_US. |

**Query**

## Obtain detailed data from the economic mode task operation record table

> Created by: Timesup

> Updated by: Timesup

> Created at: 2024-06-22 04:19:50

> Updated at: 2024-06-27 03:41:28

**The application server can call this interface to view the details of the running records of economic mode tasks.**

**Interface Status**

> Completed

**Interface URL**

> /openApi/ecoTaskRunRecord/getDetail

**Request Method**

> POST

**Content-Type**

> json

**Request Header Parameters**

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| Content-Type | application/json | string | Yes | - |
| Authorization | Bearer_eyJhbGciOiJIUzI1NiJ9.eyJkZW1vVXNlciI6ZmFsc2UsInN1YiI6IueuoeeQhuWRmCIsImF1ZCI6Ik56TTNORFF4TkRrd01UVTFPREUwTkE9PSIsIm5iZiI6MTcxMTY3NjY4NiwiaXNzIjoiRkxTLVNPTEFSLVNFUlZFUiIsImlkIjo3Mzc0NDE0OTAxNTU4MTQ0LCJleHAiOjE3MTQyNjg2ODYsImlhdCI6MTcxMTY3NjY4Nn0._l5VIYevtyv2Xc66S9w6fqmkECBFvLZPJYqjU07pObE | string | Yes | User token, which can be obtained from authentication and refreshing tokens. |
| Lang | en_US | string | Yes | Language, currently supports English en_US. |

**Request Body Parameters**

```javascript
{

	"id": 0
}
```

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| id | - | integer | No | Task ID |

**Authentication Method**

> Inherit from parent

**Response Example**

* OK(200)

```javascript
{
	"code": 0,
	"message": "",
	"data": {
		"createTime": "",
		"detailListVOList": [
			{
				"alias": "",
				"commandId": 0,
				"commandStatus": 0,
				"deviceId": 0,
				"deviceSn": "",
				"id": 0,
				"taskId": 0
			}
		],
		"failCount": 0,
		"id": 0,
		"modifyTime": "",
		"runTaskRecordId": 0,
		"runType": 0,
		"successCount": 0,
		"taskName": "",
		"taskStatus": 0,
		"taskType": "",
		"templateId": 0,
		"templateName": ""
	}
}
```

| Parameter Name | Example Value | Parameter Type | Description |
| --- | --- | ---- | ---- |
| code | - | integer | Response code |
| message | - | string | Response message |
| data | - | object | Returned data |
| createTime | - | string | Creation time |
| detailListVOList.alias | - | string | Alias |
| detailListVOList.commandId | - | integer | Command Id |
| detailListVOList.commandStatus | - | integer | Command status, 2=issued, waiting for reply, 1=device received and responded successfully, 0=device failed response result or device did not respond within 2 minutes after sending |
| detailListVOList.deviceId | - | integer | Device Id |
| detailListVOList.deviceSn | - | string | Device SN Code |
| detailListVOList.id | - | integer | - |
| detailListVOList.taskId | - | integer | Task ID |
| failCount | - | integer | Number of failures |
| successCount | - | integer | - |
| runType | - | integer | Run type: 0=default type, 1=failed |
| taskName | - | string | Task Name |
| taskType | - | string | Plant Or Device |
| templateId | - | integer | - |
| templateName | - | string | - |

* token expired(200)

```javascript
{
  "code": 998,
  "message": "The token has expired, please log in again",
  "data": {}
}
```

**Request Header Parameters**

| Parameter Name | Example Value | Parameter Type | Required | Description |
| --- | --- | ---- | ---- | ---- |
| Content-Type | application/json | string | Yes | - |
| Authorization | Bearer_eyJhbGciOiJIUzI1NiJ9.eyJkZW1vVXNlciI6ZmFsc2UsInN1YiI6IueuoeeQhuWRmCIsImF1ZCI6Ik56TTNORFF4TkRrd01UVTFPREUwTkE9PSIsIm5iZiI6MTcxMTY3NjY4NiwiaXNzIjoiRkxTLVNPTEFSLVNFUlZFUiIsImlkIjo3Mzc0NDE0OTAxNTU4MTQ0LCJleHAiOjE3MTQyNjg2ODYsImlhdCI6MTcxMTY3NjY4Nn0._l5VIYevtyv2Xc66S9w6fqmkECBFvLZPJYqjU07pObE | string | Yes | User token, which can be obtained from authentication and refreshing tokens. |
| Lang | en_US | string | Yes | Language, currently supports English en_US. |

**Query**
