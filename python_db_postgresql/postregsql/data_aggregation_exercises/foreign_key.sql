CREATE TABLE employees_projects(
	id serial PRIMARY KEY,
	employee_id INT,
	project_id INT,
		CONSTRAINT fk_employee
			FOREIGN KEY (employee_id)
				REFERENCES employees(id),
		CONSTRAINT fk_project
			FOREIGN KEY (project_id)
				REFERENCES projects(id)
)
;