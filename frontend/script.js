const API = "http://127.0.0.1:5000/departments";

function loadDepartments() {
  fetch(API)
    .then(res => res.json())
    .then(data => {
      const table = document.getElementById("tableBody");
      table.innerHTML = "";

      data.forEach(dep => {
        table.innerHTML += `
          <tr>
            <td>${dep.id}</td>
            <td>${dep.name}</td>
            <td>${dep.description}</td>
            <td>${dep.created_at}</td>
            <td>${dep.updated_at}</td>
            <td>
              <button class="edit" onclick="editDepartment(${dep.id}, '${dep.name}', '${dep.description}')">Edit</button>
              <button class="delete" onclick="deleteDepartment(${dep.id})">Delete</button>
            </td>
          </tr>
        `;
      });
    });
}

function addDepartment() {
  const name = document.getElementById("deptName").value;
  const description = document.getElementById("deptDesc").value;

  fetch(API, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ name, description })
  }).then(() => {
    document.getElementById("deptName").value = "";
    document.getElementById("deptDesc").value = "";
    loadDepartments();
  });
}

function deleteDepartment(id) {
  if (!confirm("Are you sure?")) return;

  fetch(`${API}/${id}`, { method: "DELETE" })
    .then(() => loadDepartments());
}

function editDepartment(id, oldName, oldDesc) {
  const newName = prompt("Edit Name:", oldName);
  const newDesc = prompt("Edit Description:", oldDesc);

  fetch(`${API}/${id}`, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ name: newName, description: newDesc })
  }).then(() => loadDepartments());
}

loadDepartments();