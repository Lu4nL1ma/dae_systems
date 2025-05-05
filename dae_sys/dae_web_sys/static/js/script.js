document.addEventListener("DOMContentLoaded", function () {
    // Filtro: Mesorregião / Região
    const radios_filter = document.querySelectorAll('input[name="filter"]');
    const mesor = document.getElementById('mesor');
    const regiao = document.getElementById('regiao');
    const municipioSelect = document.getElementById('municipio');

    function atualizarExibicao() {
        const filtroSelecionado = document.querySelector('input[name="filter"]:checked');
        if (!filtroSelecionado) {
            mesor.style.display = "none";
            regiao.style.display = "none";
        } else if (filtroSelecionado.value === "Mesorregião") {
            mesor.style.display = "block";
            regiao.style.display = "none";
        } else if (filtroSelecionado.value === "Região de Integração") {
            regiao.style.display = "block";
            mesor.style.display = "none";
        }
    }

    radios_filter.forEach(radio => {
        radio.addEventListener("change", atualizarExibicao);
    });

    atualizarExibicao();

    // Carregar municípios por região
    regiao.addEventListener('change', function () {
        const regiaoId = this.value;
        if (regiaoId) {
            fetch(`/carregar_por_regiao/?regiao_id=${regiaoId}`)
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

    // Carregar municípios por mesorregião
    mesor.addEventListener('change', function () {
        const mesorId = this.value;
        if (mesorId) {
            fetch(`/carregar_por_mesorregiao/?meso_id=${mesorId}`)
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

    // Mostrar Mbps conforme o serviço selecionado
    const radiosServico = document.querySelectorAll('input[name="servico"]');
    const extraInput = document.getElementById("extraInput");
    const extraInput2 = document.getElementById("extraInput2");
    const extraInput3 = document.getElementById("extraInput3");
    const extraInput4 = document.getElementById("extraInput4");

    radiosServico.forEach(radio => {
        radio.addEventListener("change", function () {
            if (this.value === "Internet") {
                extraInput.style.display = "block";
                extraInput2.style.display = "block";
                extraInput3.style.display = "none";
                extraInput4.style.display = "none";
            } else if (this.value === "Link de Dados") {
                extraInput3.style.display = "block";
                extraInput4.style.display = "block";
                extraInput.style.display = "none";
                extraInput2.style.display = "none";
            } else {
                extraInput.style.display = "block";
                extraInput2.style.display = "block";
                extraInput3.style.display = "block";
                extraInput4.style.display = "block";
            }
        });
    });
});
