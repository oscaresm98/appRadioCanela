$('#data_table').DataTable({
    "destroy": true,
    "ajax": {
        'method' : "GET",
        'url' :'/api/auditorias',
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
        { data: "imagen"},
        { data: "titulo"},
        { data: "fecha_creado"},
        { data: "estado"},
        { data: "id"}
    ],
    columnDefs: [
        { width: 20, targets: 0},
        { 
            width: 300, 
            targets: 1, 
            render: function(data){
                return data ? `<img src="${data}" width="100%"></img>` : '<img src="/static/webAdminRadio/images/redonda.jpg" width="100%">';
            }
        },
        { 
            width: 400, 
            className: "text-center",
            targets: 2
        },
        { 
            width: 200,
            className: "text-center", 
            targets: 3, 
            render: function(data) {
                return data ? new Date(data).toLocaleDateString() : 'Fecha Nula'
            }
        },     
        { 
            width: 100, 
            targets: 4, 
            className: "text-center",
            render: function(data){
                return data ? 'Visible' : 'No visible';
            }
        },
        { 
            width: 150, 
            targets: 5, 
            className: "text-center",
            render: function(data){
                return `<a href="/auditorias/${data}" class="btn btn-primary btn-sm" role="button"><i class="fas fa-eye mx-auto"></i></a>
                        <a href="/auditorias/${data}/editar" class="btn btn-success btn-sm" role="button"><i class="fas fa-pen mx-auto"></i></a>
                        <a href="#" onclick="showWarning(${data})" class="btn btn-danger btn-sm" role="button"><i class="fas fa-times mx-auto"></i></a>`
            }
        },
    ],
});