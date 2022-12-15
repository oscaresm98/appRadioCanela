$("#emisoraSelect").change(function () {
    var id_emisora = $("#emisoraSelect option:selected").val();
    getSegmentos(id_emisora);
});

function getSegmentos(emisora) {
    $('#data_table').DataTable({
        "destroy": true,
        "ajax": {
            "method": "GET",
            "url": "/api/emisora/"+ emisora +"/encuestas",
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
            { data: "descripcion"},
            { data: "fecha_hora_inicio"},
            { data: "fecha_hora_fin"},
            { data: "estado"},
            { data: "id"},
        ],
        columnDefs: [
            { width: 10, targets: 0},
            { 
                width: 180, 
                targets: 1, 
                render: function(data){
                    return data ? `<img src="${data}" width="100%"></img>` : '<img src="/static/webAdminRadio/images/redonda.jpg" width="100%">';
                }
            },
            { width: 150, targets: 2},
            { width: 250, targets: 3},
            { 
                width: 150, 
                targets: 4,
                render: function(data){
                    return (new Date(data)).toLocaleString();
                }
            },
            { 
                width: 150, 
                targets: 5,
                render: function(data){
                    return (new Date(data)).toLocaleString();
                }
            },
            { 
                width: 100, 
                targets: 6,
                render: function(data){
                    return data ? 'Activo': 'No activo'
                }
            },
            { 
                width: 200, 
                className: "text-center", 
                targets: 7,
                render: function(data, type, row){
                    let permitirEdicion = (new Date(row.fecha_hora_inicio)) > (new Date());

                    // let botones = `
                    //     <a href="/encuestas/${data}" class="btn btn-primary btn-sm me-1" role="button"><i class="fas fa-eye mx-auto"></i></a>
                    //     <a href="/encuestas/${data}/editar" aria-disabled=${permitirEdicion}
                    //         class="btn btn-sm me-1 ${permitirEdicion ? 'btn-success' : 'btn-secondary disabled'}"
                    //         title="${permitirEdicion ? 'Editar': 'No se puede editar ya que ha sido publicado'}"
                    //         role="button"><i class="fas fa-pen mx-auto"></i></a>
                    //     <a href="#" onclick="showWarning(${data})" class="btn btn-danger btn-sm me-1" role="button"><i class="fas fa-times mx-auto"></i></a>
                    // `;

                    let botones = `
                        <a href="/encuestas/${data}" class="btn btn-primary btn-sm me-1" role="button"><i class="fas fa-eye mx-auto"></i></a>
                        <a href="/encuestas/${data}/editar" class="btn btn-sm me-1 btn-success" title="Editar" role="button"><i class="fas fa-pen mx-auto"></i></a>
                        <a href="#" onclick="showWarning(${data})" class="btn btn-danger btn-sm me-1" role="button"><i class="fas fa-times mx-auto"></i></a>
                    `;

                    return botones;
                }
            },
        ],
    });
}