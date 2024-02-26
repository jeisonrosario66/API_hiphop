const btnVerifyAdd = document.getElementById("btn_verify_add");
const btnConfirmAdd = document.getElementById("btn_confirm_add");
const rowCell = document.getElementsByClassName("artist_td");

// create data original = data empy
let jsonDataOriginal = {
      artist_key: "",
      artist_aka: rowCell[1].textContent,
      artist_name: rowCell[2].textContent,
      artist_dateborn: "",
      artist_deathdate: "",
      artist_country: rowCell[5].textContent,
    };
let jsonDataUpdate = {};

function createJsonData() {
  let artist_dateborn_data = rowCell[3].children[0].value;
  let artist_deathdate_data = rowCell[4].children[0].value;

  jsonData = {
    artist_key: "",
    artist_aka: rowCell[1].textContent,
    artist_name: rowCell[2].textContent,
    artist_dateborn: artist_dateborn_data,
    artist_deathdate: artist_deathdate_data,
    artist_country: rowCell[5].textContent,
  };
  return jsonData;
}

function ajaxQuery(type, dataSent, param){
    let hasChanged = false;
    let resultMessage = "";
    $.ajax({
        headers: {
            "Content-Type": "application/json",
            "X-Requested-With": param
            // "X-Requested-With": "popstate_event",
        },
        url: "add_artist",
        type: type,
        data: JSON.stringify({ artistData: dataSent }),
        success: function(response) {
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
                resultMessage = "detected changes:<br>" + resultMessage + "<br>" + response;
              } else {
                resultMessage = "no changes detected.<br>" + "<br>" + response;
              }

              document.getElementById("result_changes").innerHTML = resultMessage;
        },

    });
};

btnVerifyAdd.addEventListener("click", function () {
  jsonDataUpdate = createJsonData();
  
  let artistName = jsonDataUpdate["artist_aka"]

  response = ajaxQuery("GET", artistName, "popstate_event")
});


btnConfirmAdd.addEventListener("click", function() {
    jsonDataUpdate = createJsonData();

    let artistName = jsonDataUpdate["artist_aka"]

    response = ajaxQuery("POST", jsonDataUpdate, "popstate_event")
});