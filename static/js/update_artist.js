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
}

function createInputElement(idTdDate, idInputElementCreated, elemtToRempalce) {
  let cell = document.getElementById(idTdDate);

  // create a new input element
  let inputElement = document.createElement("input");
  let tdElement = document.createElement("td");

  // configure the property
  inputElement.id = idInputElementCreated;
  inputElement.type = "date";
  inputElement.value = elemtToRempalce.textContent; // Replace this content

  tdElement.classList.add("artist_td");
  tdElement.id = idTdDate;
  tdElement.appendChild(inputElement);

  cell.parentElement.replaceChild(tdElement, cell);
}

function deteleteInputElement(idTdBorn, idTdDeath, jsonDataOriginal) {
  let cellBorn = document.getElementById(idTdBorn);
  let cellDeath = document.getElementById(idTdDeath);

  let dataBorn = jsonDataOriginal["artist_dateborn"];
  if (dataBorn === "") {
    dataBorn = "None";
  }

  let dataDeath = jsonDataOriginal["artist_deathdate"];
  if (dataDeath === "") {
    dataDeath = "None";
  }

  // create a new td element
  let tdElementBorn = document.createElement("td");
  let tdElementDeath = document.createElement("td");

  // configure the property | BORN DATE
  tdElementBorn.classList.add("artist_td");
  tdElementBorn.id = idTdBorn;
  tdElementBorn.textContent = dataBorn;
  // configure the property | DEATH DATE
  tdElementDeath.classList.add("artist_td");
  tdElementDeath.id = idTdDeath;
  tdElementDeath.textContent = dataDeath;

  cellBorn.parentElement.replaceChild(tdElementBorn, cellBorn);
  cellDeath.parentElement.replaceChild(tdElementDeath, cellDeath);
}

function btnConfirmFunction(responseServidor) {
  let hasChanged = false;
  let resultMessage = "";

  jsonDataUpdate = createJsonData();

  for (let property in jsonDataOriginal) {
    if (
      // If the properties have the same name
      jsonDataOriginal.hasOwnProperty(property) &&
      jsonDataUpdate.hasOwnProperty(property)
    ) {
      if (jsonDataOriginal[property] !== jsonDataUpdate[property]) {
        resultMessage += `${property}: ${jsonDataOriginal[property]} ----> ${jsonDataUpdate[property]}<br>`;
        hasChanged = true;
      }
    }
  }

  if (hasChanged) {
    resultMessage = "detected changes:<br>" + resultMessage + responseServidor;
  } else {
    resultMessage = "no changes detected.<br>";
  }

  document.getElementById("result_changes").innerHTML = resultMessage;
}

function ajax_btnConfirm() {
  $.ajax({
    headers: { "Content-Type": "application/json" },
    url: "/artist_update",
    type: "PUT",
    data: JSON.stringify(jsonDataUpdate),

    success: function (response) {
      let responseMessage = "Update artist OK";
      btnConfirmFunction(response);
    },
    error: function (error) {
      btnConfirmFunction("Error in the PUT request");
    },
  });
}

btnUpdate.addEventListener("click", function () {
  let artistKeyRowTable = document.getElementById("artistKey");
  if (!btnEditState) {
    // Create inputs type data inside table cell
    createInputElement(cellBorn.id, "input_date_born", cellBorn);
    createInputElement(cellDeath.id, "input_date_death", cellDeath);

    // Add new styles
    btnUpdate.classList.add("button_active");
    for (let i = 0; i < rowCell.length; i++) {
      // Add new style and attributes in each cell
      rowCell[i].classList.add("td_editable");
      rowCell[i].contentEditable = "true";
    }

    // Delete styles None
    btnVerify.classList.remove("none"); // Show the button "Verify changes"
    btnConfirm.classList.remove("none"); // Show the button "Confirm update"
    responseOutput.classList.remove("none"); // Show the window outout
    artistKeyRowTable.contentEditable = "false"; // This is not a content editable

    // create an object Json whith the data
    let artist_dateborn_data = rowCell[3].children[0].value;
    let artist_datedeath_data = rowCell[4].children[0].value;

    jsonDataOriginal = {
      artist_key: rowCell[0].textContent,
      artist_aka: rowCell[1].textContent,
      artist_name: rowCell[2].textContent,
      artist_dateborn: artist_dateborn_data,
      artist_deathdate: artist_datedeath_data,
      artist_country: rowCell[5].textContent,
    };
    btnUpdate.textContent = "Cancel edit";
    jsonDataUpdate = createJsonData(); // create json data
    btnEditState = true;
  } else {
    // Delete inputs type data inside table cell
    deteleteInputElement(cellBorn.id, cellDeath.id, jsonDataOriginal);

    // Delete styles
    btnUpdate.classList.remove("button_active");
    for (let i = 0; i < rowCell.length; i++) {
      // Add new style and attributes in each cell
      rowCell[i].classList.remove("td_editable");
      rowCell[i].contentEditable = "false";
    }

    // Add styles None
    btnVerify.classList.add("none"); // Show the button "Verify changes"
    btnConfirm.classList.add("none"); // Show the button "Confirm update"
    responseOutput.classList.add("none"); // Show the window outout

    btnUpdate.textContent = "Edit artist";
    btnEditState = false;
  }
});

btnVerify.addEventListener("click", function () {
  btnConfirmFunction("");
});

btnConfirm.addEventListener("click", function () {
  jsonDataUpdate = createJsonData();
  ajax_btnConfirm();
});
