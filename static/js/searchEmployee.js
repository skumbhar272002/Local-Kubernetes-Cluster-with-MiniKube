const searchField = document.querySelector('#searchField')
const tableOutput = document.querySelector('.table-output')
const appTable = document.querySelector('.app-table')
const tbody = document.querySelector('.table-body')
const NoOutput = document.querySelector('.no-output')

tableOutput.style.display = 'none';

searchField.addEventListener('keyup', (e) => {
    const searchValue = e.target.value;
    if (searchValue.trim().length>0){
        tbody.innerHTML = " ";
        NoOutput.innerHTML = " ";
        console.log("searchValue", searchValue);

        fetch("/Dashboard/search_employee", {
            
            body: JSON.stringify({ searchText: searchValue }),
            method: "POST",
        })
            .then((res) => res.json())
            .then((data) => {
            console.log("data", data);
            appTable.style.display = 'none';
            tableOutput.style.display = 'block';
            
            
            if(data.length>0){
                data.forEach(item=>{
                    tbody.innerHTML += ` 
                    <tr>
                    
                    <input type="hidden" name="employee" value="${item.username}">
                      <td>${item.username}</td>
                      <td>${item.first_name}</td>
                      <td>${item.last_name}</td>                      
                  </tr>`
               

            })}
            else  {
                appTable.style.display = 'none';
                tableOutput.style.display = 'none';
                NoOutput.innerHTML = `<p style="color: red;">No results found.</p>`;
            }
               
            });
    }
    else{
        tableOutput.style.display = 'none';
        appTable.style.display = 'block';
    }
})