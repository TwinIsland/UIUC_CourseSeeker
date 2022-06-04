## Dev Doc
> 2022/6/24

`course`: variable that storage course info, dictionary with keys:`url` and `crn`


### Tools
```
get_course_info(course_name: str, crn: str) -> dict: 
```

from course name (e.g. cs225), and crn to `course`

---
```
is_valid_course(course: dict[str, str]) -> bool
```
return if `course` is valid, need internet

---

### IpLib
class to provide ip pool and header, new an instance to use


```
get_ip()
```
get a random ip from pool

---

```
iplib.get_header()
```
get the header, static function

### Encryption
provide simple encryption method, need init to generate key, new an instance to use

```
dec(self, ciphertext: str) -> str:
```
decryption method

---
```
enc(self, plaintext: str) -> str:
```
encryption method