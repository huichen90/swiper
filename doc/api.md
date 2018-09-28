前后端接口
==========

## 接口格式

1. 所有获取数据的 HTTP 接口, 参数均由 GET 方法传递
2. 所有修改数据的 HTTP 接口, 参数均由 POST 方法传递
3. 返回值均为 JSON 格式, 必须包含两个字段: "status", "data"
    1. status 字段为状态码, int 类型, 为 0 时表示返回值正常, 其他任何值时均表示异常, 需客户端根据状态码为用户提供不同的错误提示
    2. data 字段为返回的数据, 字典类型. 详情见下面具体接口. 当一个接口仅需状态码确认时, data 可以为空
    3. 示例
       ```json
       {
           "status": 0,
           "data": {
               "user": {"uid": 11, "username": "Hello World"},
               "data": "2018-09-12"
           }
       }
       ```


## 基础数据格式

1. User
    ```json
    {
        "uid": 123,                  // 用户 id
        "nickname": "Miao",          // 用户名
        "age": 21,                   // 年龄
        "sex": "M",                  // 性别
        "location": "中国/北京/北京",  // 常居地
        "avatars": [                 // 头像 URL 列表, 最多为 6 张
            "http://xxx.com/user/avatar/123/1.jpg",
            "http://xxx.com/user/avatar/123/2.jpg",
            "http://xxx.com/user/avatar/123/3.jpg",
            ...
        ]
    }
    ```

## User 接口

1. 提交手机号
    * **Description**: 提交手机号，根据结果判断下一步需要提交的数据
    * **Method**: POST
    * **Path**: /user/verify/phone
    * **Params**:
        field | required | type | description
        ------|----------|------|-----------------------
        phone |        Y |  str | 手机号, "+8618888888888"

    * **Return**: None

2. 提交验证码
    * **Description**: 根据上一步的结果提交需要的数据
    * **Method**: POST
    * **Path**: /user/verify/code
    * **Params**:
        field | required | type | description
        ------|----------|------|-----------------------
         code |        Y |  int | 验证码

    * **Return**:
        field | required | type | description
        ------|----------|------|-----------------------
         user |        Y | User | 用户数据

3. get profile (获取配置信息)
    * **Description**: -
    * **Method**: GET
    * **Path**: /user/verification/code
    * **Params**:
        field | required | type | description
        ------|----------|------|-----------------------
              |        Y |    - | -

    * **Return**:
        field | required | type | description
        ------|----------|------|-----------------------
              |        Y |    - | -

4. set profile (修改配置)
    * **Description**: -
    * **Method**: POST
    * **Path**: /user/profile/setup
    * **Params**:
        field | required | type | description
        ------|----------|------|-----------------------
              |        Y |    - | -

    * **Return**:
        field | required | type | description
        ------|----------|------|-----------------------
              |        Y |    - | -

5. upload avatar (上传头像)
    * **Description**: -
    * **Method**: POST
    * **Path**: /user/avatar/upload
    * **Params**:
        field | required | type | description
        ------|----------|------|-----------------------
              |        Y |    - | -

    * **Return**:
        field | required | type | description
        ------|----------|------|-----------------------
              |        Y |    - | -


## Social 接口

1. 获取推荐用户
    * **Description**:
    * **Method**: GET
    * **Path**: /social/recommend
    * **Params**:
        field | required | type | description
        ------|----------|------|-----------------------
              |        Y |    - | -

    * **Return**:
        field | required | type | description
        ------|----------|------|-----------------------
              |        Y |    - | -

2. 喜欢
    * **Description**:
    * **Method**: POST
    * **Path**: /social/like
    * **Params**:
        field | required | type | description
        ------|----------|------|-----------------------
              |        Y |    - | -

    * **Return**:
        field | required | type | description
        ------|----------|------|-----------------------
              |        Y |    - | -

3. 超级喜欢
    * **Description**:
    * **Method**: POST
    * **Path**: /social/superlike
    * **Params**:
        field | required | type | description
        ------|----------|------|-----------------------
              |        Y |    - | -

    * **Return**:
        field | required | type | description
        ------|----------|------|-----------------------
              |        Y |    - | -

4. 不喜欢
    * **Description**:
    * **Method**: POST
    * **Path**: /social/dislike
    * **Params**:
        field | required | type | description
        ------|----------|------|-----------------------
              |        Y |    - | -

    * **Return**:
        field | required | type | description
        ------|----------|------|-----------------------
              |        Y |    - | -

5. 反悔
    * **Description**:
    * **Method**: POST
    * **Path**: /social/rewind
    * **Params**:
        field | required | type | description
        ------|----------|------|-----------------------
              |        Y |    - | -

    * **Return**:
        field | required | type | description
        ------|----------|------|-----------------------
              |        Y |    - | -

6. 曝光
    * **Description**:
    * **Method**: POST
    * **Path**: /social/stepup
    * **Params**:
        field | required | type | description
        ------|----------|------|-----------------------
              |        Y |    - | -

    * **Return**:
        field | required | type | description
        ------|----------|------|-----------------------
              |        Y |    - | -


## status 状态码

code | description
-----|-------------
   0 | 正常
1000 | 用户不存在
