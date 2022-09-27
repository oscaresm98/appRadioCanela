// var minDate, maxDate;
 
//
// $.fn.dataTable.ext.search.push(
//     function( settings, data, dataIndex ) {
//         var min = minDate.val();
//         var max = maxDate.val();

//         // if(max){
//         //     max.setDate(max.getDate()+1);
//         //     console.log(max);
//         // }        

//         let fechaPrev =  moment(data[3], 'DD/MM/YYYY');
//         var date = fechaPrev.toDate();
        
//         if (
//             ( min === null && max === null ) ||
//             ( min === null && date <= max ) ||
//             ( min <= date   && max === null ) ||
//             ( min <= date   && date <= max )
//         ) {
//             return true;
//         }
//         return false;
//     }
// );

var table = $('#data_table').DataTable({
    "destroy": true,
    "ajax": {
        'method' : "GET",
        'url' :'/api/partidos',
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
        { data: function(data){
            return `${data.id_equipo_local.equipo} vs ${data.id_equipo_visitante.equipo}`;
        }},
        { data: function(data){
            return data.id_torneo.nombre;
        }},
        { data: "fecha_evento"},
        { data: "emisoras"},
        { data: "id"}
    ],
    columnDefs: [
        { width: 10, targets: 0},
        { width: 250, targets: 1},
        { width: 125, targets: 2},
        { width: 100, targets: 3, render: function(data) {
            return data ? new Date(data).toLocaleDateString() : 'Fecha Nula'
        }},
        { width: 250, targets: 4, render: function(data) {
            let plantillaEmisoras = ``;
            Array.from(data).forEach(emisora => {
                plantillaEmisoras += `<li>${emisora.radio} - ${emisora.frecuencia_dial} ${emisora.tipo_frecuencia}</li>`
            });
            return `<ul>
                        ${plantillaEmisoras}
                    </ul>`;
        }},                
        { width: 150, targets: 5, render: function(data){
            return `<a href="/partidos/` + data + `" class="btn btn-primary btn-sm" role="button"><i class="fas fa-eye mx-auto"></i></a>
                    <a href="/partidos/` + data + `/editar" class="btn btn-success btn-sm" role="button"><i class="fas fa-pen mx-auto"></i></a>
                    <a href="#" onclick="showWarning(` + data + `)" class="btn btn-danger btn-sm" role="button"><i class="fas fa-times mx-auto"></i></a>`
        }},
    ],
});

//
// minDate = new DateTime($('#min'), {
//     format: 'DD/MM/YYYY'
// });
// maxDate = new DateTime($('#max'), {
//     format: 'DD/MM/YYYY'
// });

// // Refilter the table
// $('#min, #max').on('change', function () {
//     table.draw();
// });
