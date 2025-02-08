//script de carregar o municipios
// Adicione seu JavaScript aqui
document.getElementById('regiao').addEventListener('change', function() {
    const regiaoId = this.value;
    const municipioSelect = document.getElementById('municipio');

    if (regiaoId) {
        fetch(`/carregar-municipios/?regiao_id=${regiaoId}`)
            .then(response => response.json())
            .then(data => {
                municipioSelect.innerHTML = '';
                data.forEach(municipio => {
                    const option = document.createElement('option');
                    option.value = municipio.municipio;
                    option.textContent = municipio.municipio;
                    municipioSelect.appendChild(option);
                });
                municipioSelect.disabled = false;
            });
    } else {
        municipioSelect.innerHTML = '<option value="">Selecione um município</option>';
        municipioSelect.disabled = true;
    }
});

//script de carregar os mbps

document.addEventListener("DOMContentLoaded", function() {
    let radios = document.querySelectorAll('input[name="servico"]');
    let extraInput = document.getElementById("extraInput");
    let extraInput2 = document.getElementById("extraInput2"); // Novo elemento H3
    let extraInput3 = document.getElementById("extraInput3");
    let extraInput4 = document.getElementById("extraInput4");

    radios.forEach(radio => {
        radio.addEventListener("change", function() {
            if (this.value === "Internet") {
                extraInput.style.display = "block";
                extraInput2.style.display = "block";
                extraInput3.style.display = "none";
                extraInput4.style.display = "none"
                
            
            }
            
            else if (this.value === "Link de Dados") {
                extraInput3.style.display = "block";
                extraInput4.style.display = "block"
                extraInput.style.display = "none";
                extraInput2.style.display = "none"
          
          }

            else {
                extraInput.style.display = "block";
                extraInput2.style.display = "block";
                extraInput3.style.display = "block";
                extraInput4.style.display = "block";
            }
        });
    });
});