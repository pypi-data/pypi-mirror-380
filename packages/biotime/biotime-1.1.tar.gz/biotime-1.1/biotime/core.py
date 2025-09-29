import json

import requests
from .exceptions import AuthenticationError, APIRequestError
from .utils import logger



class BIOT:
    def __init__(self, host: str, username: str, password: str):
        self.base_url = host.rstrip("/")
        self.username = username
        self.password = password
        self.token = None

        self.login()


    def _headers(self):
        headers = {"Content-Type": "application/json"}
        if self.token:
            headers["Authorization"] = f"JWT {self.token}"
        return headers


    def login(self):
        url = f"{self.base_url}/jwt-api-token-auth/"
        data = {"username": self.username, "password": self.password}

        response = requests.post(url, json=data, headers=self._headers())
        if response.status_code == 200:
            self.token = response.json()["token"]
            logger.info("Token olindi ✅")
        else:
            raise AuthenticationError("Login muvaffaqiyatsiz bo‘ldi")


    def request(self, method: str, endpoint: str, retried: bool = False, **kwargs):
        url = f"{self.base_url}/{endpoint}"
        response = requests.request(method=method, url=url, headers=self._headers(), **kwargs)

        if response.status_code == 401 and not retried:
            self.login()
            return self.request(method, endpoint, retried=True, **kwargs)

        if response.status_code in (200, 201):
            return response.json()
        if response.status_code == 204:
            return {"status": True, "detail": "No content"}

        raise APIRequestError(f"Xatolik: {response.status_code} - {response.text}")


    # Area methods
    def get_all_area(self, page=None, page_size=None, area_code=None, area_name=None, area_code_icontains=None, area_name_icontains=None, ordering=None) -> json:
        """The ordering field can be filled in: id, dept_code, dept_name"""
        params = {
            "page": page,
            "page_size": page_size,
            "area_code": area_code,
            "area_name": area_name,
            "area_code_icontains": area_code_icontains,
            "area_name_icontains": area_name_icontains,
            "ordering": ordering
        }
        response = self.request(method="GET", endpoint="personnel/api/areas/", params=params)
        return response


    def create_area(self, area_name: str, area_code: str, parent_area: int | None = None) -> json:
        data = {
            "area_code": area_code,
            "area_name": area_name,
            "parent_area": parent_area
        }
        return self.request(method="POST", endpoint="personnel/api/areas/", data=json.dumps(data))


    def get_area(self, area_id: int) -> json:
        return self.request(method="GET", endpoint=f"personnel/api/areas/{area_id}/")
    

    def update_area(self, area_id: int, area_name: str, area_code: str, parent_area: int | None = None) -> json:
        data = {
            "area_code": area_code,
            "area_name": area_name,
            "parent_area": parent_area
        }
        return self.request(method="PUT", endpoint=f"personnel/api/areas/{area_id}/", data=json.dumps(data))
    

    def delete_area(self, area_id: int) -> json:
        return self.request(method="DELETE", endpoint=f"personnel/api/areas/{area_id}/")
    

    # Department methods
    def get_all_department(self, page=None, page_size=None, dept_code=None, dept_name=None, dept_code_icontains=None, dept_name_icontains=None, ordering=None) -> json:
        """The ordering field can be filled in: id, dept_code, dept_name"""
        params = {
            "page": page,
            "page_size": page_size,
            "dept_code": dept_code,
            "dept_name": dept_name,
            "dept_code_icontains": dept_code_icontains,
            "dept_name_icontains": dept_name_icontains,
            "ordering": ordering
        }
        response = self.request(method="GET", endpoint="personnel/api/departments/", params=params)
        return response

    def get_department(self, department_id: int) -> json:
        return self.request(method="GET", endpoint=f"personnel/api/departments/{department_id}/")

    def create_department(self, dept_name: str, dept_code: str, parent_dept: int | None = None) -> json:
        data = {
            "dept_code": dept_code,
            "dept_name": dept_name,
            "parent_dept": parent_dept
        }
        return self.request(method="POST", endpoint="personnel/api/departments/", data=json.dumps(data))

    def update_department(self, department_id: int, dept_name: str, dept_code: str, parent_dept: int | None = None) -> json:
        data = {
            "dept_code": dept_code,
            "dept_name": dept_name,
            "parent_dept": parent_dept
        }
        return self.request(method="PUT", endpoint=f"personnel/api/departments/{department_id}/", data=json.dumps(data))
    
    def delete_department(self, department_id: int) -> json:
        return self.request(method="DELETE", endpoint=f"personnel/api/departments/{department_id}/")
    

    # Position methods
    def get_all_position(self, page=None, page_size=None, position_code=None, position_name=None, position_code_icontains=None, position_name_icontains=None, ordering=None) -> json:
        """The ordering field can be filled in: id, position_code, position_name"""
        params = {
            "page": page,
            "page_size": page_size,
            "position_code": position_code,
            "position_name": position_name,
            "position_code_icontains": position_code_icontains,
            "position_name_icontains": position_name_icontains,
            "ordering": ordering
        }
        response = self.request(method="GET", endpoint="personnel/api/positions/", params=params)
        return response
    
    def get_position(self, position_id: int) -> json:
        return self.request(method="GET", endpoint=f"personnel/api/positions/{position_id}/")
    
    def create_position(self, position_name: str, position_code: str, parent_position: int | None=None) -> json:
        data = {
            "position_code": position_code,
            "position_name": position_name,
            "parent_position": parent_position
        }
        return self.request(method="POST", endpoint="personnel/api/positions/", data=json.dumps(data))

    def update_position(self, position_id: int, position_name: str, position_code: str, parent_position: int | None=None) -> json:
        data = {
            "position_code": position_code,
            "position_name": position_name,
            "parent_position": parent_position
        }
        return self.request(method="PUT", endpoint=f"personnel/api/positions/{position_id}/", data=json.dumps(data))
    
    def delete_position(self, position_id: int) -> json:
        return self.request(method="DELETE", endpoint=f"personnel/api/positions/{position_id}/")
    
    
    # Employee methods
    def get_all_employee(
            self, 
            page=None, 
            page_size=None, 
            emp_code=None, 
            emp_code_icontains=None, 
            first_name=None, 
            first_name_icontains=None, 
            last_name=None, 
            last_name_icontains=None, 
            department=None, 
            areas=None
        ) -> json:
        params = {
            "page": page,
            "page_size": page_size,
            "emp_code": emp_code,
            "emp_code_icontains": emp_code_icontains,
            "first_name": first_name,
            "first_name_icontains": first_name_icontains,
            "last_name": last_name,
            "last_name_icontains": last_name_icontains,
            "department": department,
            "areas": areas
        }
        return self.request(method="GET", endpoint="personnel/api/employees/", params=params)
    

    def get_employee(self, employee_id: int):
        return self.request(method="GET", endpoint=f"personnel/api/employees/{employee_id}/")
    

    def create_employee(
            self,
            emp_code: str,
            department: int,
            area: list,
            hire_date: str | None = None, 
            first_name: str | None = None, 
            last_name: str | None = None,
            gender: str | None = None,
            mobile: str | None = None,
            national: str | None = None,
            address: str | None = None,
            email: str | None = None,
            app_status: str | None = None,
            birthday: str | None = None
        ) -> json:
        data = {
            "emp_code": emp_code,
            "department": department,
            "area": area,
            "hire_date": hire_date,
            "first_name": first_name,
            "last_name": last_name,
            "gender": gender,
            "mobile": mobile,
            "national": national,
            "address": address,
            "email": email,
            "app_status": app_status,
            "birthday": birthday
        }
        return self.request(method="POST", endpoint="personnel/api/employees/", data=json.dumps(data))
    

    def update_employee(
            self,
            employee_id: int,
            emp_code: str,
            department: int,
            area: list,
            hire_date: str | None = None, 
            first_name: str | None = None, 
            last_name: str | None = None,
            gender: str | None = None,
            mobile: str | None = None,
            national: str | None = None,
            address: str | None = None,
            email: str | None = None,
            app_status: str | None = None,
            birthday: str | None = None
        ) -> json:
        data = {
            "emp_code": emp_code,
            "department": department,
            "area": area,
            "hire_date": hire_date,
            "first_name": first_name,
            "last_name": last_name,
            "gender": gender,
            "mobile": mobile,
            "national": national,
            "address": address,
            "email": email,
            "app_status": app_status,
            "birthday": birthday
        }
        return self.request(method="PUT", endpoint=f"personnel/api/employees/{employee_id}/", data=json.dumps(data))
    

    def delete_employee(self, employee_id: int) -> json:
        return self.request(method="DELETE", endpoint=f"personnel/api/employees/{employee_id}/")


    # Work reports
    def get_work_report(self, emp_id: int, start_date: str | None = None, end_date: str | None = None, page_size=None, page=None, departments=None, areas=None, groups=None,) -> json:
        params = {
            "page": page,
            "page_size": page_size,
            "departments": departments,
            "areas": areas,
            "groups": groups,
            "start_date": start_date,
            "end_date": end_date,
            "employees": emp_id
        }
        return self.request(method="GET", endpoint="att/api/firstLastReport/", params=params)
