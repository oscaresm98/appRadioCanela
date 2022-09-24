$('#data_table').DataTable({
    "destroy": true,
    "ajax": {
        'method' : "GET",
        'url' :'/api/torneos',
        "dataSrc": "",
        "error": function(xhr, status, error) {
            console.log("readyState: " + xhr.readyState);
            console.log("responseText: "+ xhr.responseText);
            console.log("status: " + xhr.status);
            console.log("text status: " + status);
            console.log("error: " + error);
        },
    },
    "columns": [
        { data: "id"},
        { data: "nombre"},
        { data: "lugar"},
        { data: "estado"},
        { data: "id"}
    ],
    columnDefs: [
        { width: 10, targets: 0},
        { width: 250, targets: 1},
        { width: 200, targets: 2},
        { width: 100, targets: 3, render: function(data) {
            return data ? 'Activo' : 'No Activo';
        }},        
        { width: 100, targets: 4, render: function(data){
            return `<a href="/torneos/` + data + `/editar" class="btn btn-success btn-sm" role="button"><i class="fas fa-pen mx-auto"></i></a>
                    <a href="#" onclick="showWarning(` + data + `)" class="btn btn-danger btn-sm" role="button"><i class="fas fa-times mx-auto"></i></a>`
        }},
    ],
});
