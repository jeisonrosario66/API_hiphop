const btnUpdate = document.getElementById("button_edit_artist");
const btnVerify = document.getElementById("btn_verify");
const btnConfirm = document.getElementById("btn_confirm");

const responseOutput = document.getElementById("response_output");

const inputBorn = document.getElementById("input_born");
const inputDeath = document.getElementById("input_death");
const cellBorn = document.getElementById("artist_date_born");
const cellDeath = document.getElementById("artist_date_death");

const rowCell = document.getElementsByClassName("artist_td");
const dateCell = document.getElementsByClassName("artist_td_date");



let btnEditState = false;
let jsonDataOriginal = {};
let jsonDataUpdate = {};

function isEmtpy(obj) {
    return Object.keys(obj).length === 0;
}

function createJsonData() {
    let artist_dateborn_data = rowCell[3].children[0].value;
    let artist_deathdate_data = rowCell[4].children[0].value;

    jsonData = {
        artist_key: rowCell[0].textContent,
        artist_aka: rowCell[1].textContent,
        artist_name: rowCell[2].textContent,
        artist_dateborn: artist_dateborn_data,
        artist_deathdate: artist_deathdate_data,
        artist_country: rowCell[5].textContent,
    };
    return jsonData;
};

function createInputElement(idTdDate, idInputElementCreated, elemtToRempalce) {
    let cell = document.getElementById(idTdDate);

    // create a new input element
    let inputElement = document.createElement("input");
    let tdElement = document.createElement("td");

    // configure the property 
    inputElement.id = idInputElementCreated
    inputElement.type = "date";
    inputElement.value = elemtToRempalce.textContent // Replace this content
    
    tdElement.classList.add("artist_td");
    tdElement.appendChild(inputElement)
    
    cell.parentElement.replaceChild(tdElement, cell);
};

function btnConfirmFunction(responseServidor){
    let hasChanged = false;
    let resultMessage = '';

    jsonDataUpdate = createJsonData();

    for (let property in jsonDataOriginal) {
        if (jsonDataOriginal.hasOwnProperty(property) && jsonDataUpdate.hasOwnProperty(property)) {
            if (jsonDataOriginal[property] !== jsonDataUpdate[property]) {
                resultMessage += `${property}: ${jsonDataOriginal[property]} ----> ${jsonDataUpdate[property]}<br>`;
                hasChanged = true;
            }
        }
    };

    if (hasChanged) {
        resultMessage = "detected changes:<br>" + resultMessage + responseServidor; 
    } else {
        resultMessage = "no changes detected.<br>";
    };

    document.getElementById("result_changes").innerHTML = resultMessage;
};

function ajax_btnConfirm(){
    $.ajax({
        headers: {'Content-Type': 'application/json'},
        url: "/artist_updaste",
        type: "PUT",
        data: JSON.stringify(jsonDataUpdate),
        success: function(response) {
            let responseMessage = "Update artist OK";
            btnConfirmFunction(responseMessage);
        },
        error: function(error) {
            btnConfirmFunction("Error in the PUT request");
        }
    })
};

btnUpdate.addEventListener("click", function() {
    if (!btnEditState) {
        // create inputs type data inside table cell
       createInputElement(cellBorn.id, "input_date_born", cellBorn);
       createInputElement(cellDeath.id, "input_date_death", cellDeath);
        
        let artistKeyRowTable = document.getElementById("artistKey");

        // Add new styles
        btnUpdate.classList.add("button_active");
        for (let i = 0; i < rowCell.length; i++) {
                // Add new style and attributes in each cell 
                rowCell[i].classList.add("td_editable");
                rowCell[i].contentEditable = "true";
        };
        
        // Delete styles
        btnVerify.classList.remove("none"); // Show the button "Verify changes"
        btnConfirm.classList.remove("none"); // Show the button "Confirm update"
        responseOutput.classList.remove("none"); // Show the window outout
        artistKeyRowTable.contentEditable = "false"; // This is not a content editable

        // create an object Json whith the data
        let artist_dateborn_data = rowCell[3].children[0].value
        let artist_datedeath_data = rowCell[4].children[0].value

        jsonDataOriginal = {
            artist_key: rowCell[0].textContent,
            artist_aka: rowCell[1].textContent,
            artist_name: rowCell[2].textContent,
            artist_dateborn: artist_dateborn_data,
            artist_deathdate:artist_datedeath_data,
            artist_country: rowCell[5].textContent
        };

        btnEditState = true;
    }
});

btnVerify.addEventListener("click", function() {
    btnConfirmFunction("");
});

btnConfirm.addEventListener("click", function() {
    if (isEmtpy(jsonDataUpdate)) {
        jsonDataUpdate = createJsonData();
        ajax_btnConfirm();
    }else {
        ajax_btnConfirm();
    }
});