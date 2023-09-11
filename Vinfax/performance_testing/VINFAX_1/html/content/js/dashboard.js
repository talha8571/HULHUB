/*
   Licensed to the Apache Software Foundation (ASF) under one or more
   contributor license agreements.  See the NOTICE file distributed with
   this work for additional information regarding copyright ownership.
   The ASF licenses this file to You under the Apache License, Version 2.0
   (the "License"); you may not use this file except in compliance with
   the License.  You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
*/
var showControllersOnly = false;
var seriesFilter = "";
var filtersOnlySampleSeries = true;

/*
 * Add header in statistics table to group metrics by category
 * format
 *
 */
function summaryTableHeader(header) {
    var newRow = header.insertRow(-1);
    newRow.className = "tablesorter-no-sort";
    var cell = document.createElement('th');
    cell.setAttribute("data-sorter", false);
    cell.colSpan = 1;
    cell.innerHTML = "Requests";
    newRow.appendChild(cell);

    cell = document.createElement('th');
    cell.setAttribute("data-sorter", false);
    cell.colSpan = 3;
    cell.innerHTML = "Executions";
    newRow.appendChild(cell);

    cell = document.createElement('th');
    cell.setAttribute("data-sorter", false);
    cell.colSpan = 7;
    cell.innerHTML = "Response Times (ms)";
    newRow.appendChild(cell);

    cell = document.createElement('th');
    cell.setAttribute("data-sorter", false);
    cell.colSpan = 1;
    cell.innerHTML = "Throughput";
    newRow.appendChild(cell);

    cell = document.createElement('th');
    cell.setAttribute("data-sorter", false);
    cell.colSpan = 2;
    cell.innerHTML = "Network (KB/sec)";
    newRow.appendChild(cell);
}

/*
 * Populates the table identified by id parameter with the specified data and
 * format
 *
 */
function createTable(table, info, formatter, defaultSorts, seriesIndex, headerCreator) {
    var tableRef = table[0];

    // Create header and populate it with data.titles array
    var header = tableRef.createTHead();

    // Call callback is available
    if(headerCreator) {
        headerCreator(header);
    }

    var newRow = header.insertRow(-1);
    for (var index = 0; index < info.titles.length; index++) {
        var cell = document.createElement('th');
        cell.innerHTML = info.titles[index];
        newRow.appendChild(cell);
    }

    var tBody;

    // Create overall body if defined
    if(info.overall){
        tBody = document.createElement('tbody');
        tBody.className = "tablesorter-no-sort";
        tableRef.appendChild(tBody);
        var newRow = tBody.insertRow(-1);
        var data = info.overall.data;
        for(var index=0;index < data.length; index++){
            var cell = newRow.insertCell(-1);
            cell.innerHTML = formatter ? formatter(index, data[index]): data[index];
        }
    }

    // Create regular body
    tBody = document.createElement('tbody');
    tableRef.appendChild(tBody);

    var regexp;
    if(seriesFilter) {
        regexp = new RegExp(seriesFilter, 'i');
    }
    // Populate body with data.items array
    for(var index=0; index < info.items.length; index++){
        var item = info.items[index];
        if((!regexp || filtersOnlySampleSeries && !info.supportsControllersDiscrimination || regexp.test(item.data[seriesIndex]))
                &&
                (!showControllersOnly || !info.supportsControllersDiscrimination || item.isController)){
            if(item.data.length > 0) {
                var newRow = tBody.insertRow(-1);
                for(var col=0; col < item.data.length; col++){
                    var cell = newRow.insertCell(-1);
                    cell.innerHTML = formatter ? formatter(col, item.data[col]) : item.data[col];
                }
            }
        }
    }

    // Add support of columns sort
    table.tablesorter({sortList : defaultSorts});
}

$(document).ready(function() {

    // Customize table sorter default options
    $.extend( $.tablesorter.defaults, {
        theme: 'blue',
        cssInfoBlock: "tablesorter-no-sort",
        widthFixed: true,
        widgets: ['zebra']
    });

    var data = {"OkPercent": 100.0, "KoPercent": 0.0};
    var dataset = [
        {
            "label" : "FAIL",
            "data" : data.KoPercent,
            "color" : "#FF6347"
        },
        {
            "label" : "PASS",
            "data" : data.OkPercent,
            "color" : "#9ACD32"
        }];
    $.plot($("#flot-requests-summary"), dataset, {
        series : {
            pie : {
                show : true,
                radius : 1,
                label : {
                    show : true,
                    radius : 3 / 4,
                    formatter : function(label, series) {
                        return '<div style="font-size:8pt;text-align:center;padding:2px;color:white;">'
                            + label
                            + '<br/>'
                            + Math.round10(series.percent, -2)
                            + '%</div>';
                    },
                    background : {
                        opacity : 0.5,
                        color : '#000'
                    }
                }
            }
        },
        legend : {
            show : true
        }
    });

    // Creates APDEX table
    createTable($("#apdexTable"), {"supportsControllersDiscrimination": true, "overall": {"data": [0.8495145631067961, 500, 1500, "Total"], "isController": false}, "titles": ["Apdex", "T (Toleration threshold)", "F (Frustration threshold)", "Label"], "items": [{"data": [1.0, 500, 1500, "https://vinfax-api.designitic.com/user/download-history-6"], "isController": false}, {"data": [1.0, 500, 1500, "https://vinfax-api.designitic.com/user/download-history-5"], "isController": false}, {"data": [1.0, 500, 1500, "https://vinfax-api.designitic.com/-9"], "isController": false}, {"data": [1.0, 500, 1500, "https://vinfax-api.designitic.com/user/download-history-4"], "isController": false}, {"data": [1.0, 500, 1500, "https://vinfax-api.designitic.com/-8"], "isController": false}, {"data": [1.0, 500, 1500, "https://vinfax-api.designitic.com/user/download-history-3"], "isController": false}, {"data": [0.5, 500, 1500, "https://vinfax-api.designitic.com/-7"], "isController": false}, {"data": [0.5, 500, 1500, "https://vinfax-api.designitic.com/-6"], "isController": false}, {"data": [1.0, 500, 1500, "https://vinfax-api.designitic.com/user/download-history-9"], "isController": false}, {"data": [0.0, 500, 1500, "https://vinfax-api.designitic.com/-5"], "isController": false}, {"data": [1.0, 500, 1500, "https://vinfax-api.designitic.com/user/download-history-8"], "isController": false}, {"data": [1.0, 500, 1500, "https://vinfax-api.designitic.com/-4"], "isController": false}, {"data": [1.0, 500, 1500, "https://vinfax-api.designitic.com/user/download-history-7"], "isController": false}, {"data": [1.0, 500, 1500, "https://vinfax-api.designitic.com/user/subscription-7"], "isController": false}, {"data": [1.0, 500, 1500, "https://vinfax-api.designitic.com/user/subscription-8"], "isController": false}, {"data": [1.0, 500, 1500, "https://vinfax-api.designitic.com/user/subscription-5"], "isController": false}, {"data": [1.0, 500, 1500, "https://vinfax-api.designitic.com/user/subscription-6"], "isController": false}, {"data": [1.0, 500, 1500, "https://vinfax-api.designitic.com/user/subscription-9"], "isController": false}, {"data": [0.5, 500, 1500, "https://vinfax-api.designitic.com/-3"], "isController": false}, {"data": [0.5, 500, 1500, "https://vinfax-api.designitic.com/-2"], "isController": false}, {"data": [0.5, 500, 1500, "https://vinfax-api.designitic.com/-1"], "isController": false}, {"data": [0.5, 500, 1500, "https://vinfax-api.designitic.com/-0"], "isController": false}, {"data": [1.0, 500, 1500, "https://vinfax-api.designitic.com/user/download-history-2"], "isController": false}, {"data": [1.0, 500, 1500, "https://vinfax-api.designitic.com/user/download-history-1"], "isController": false}, {"data": [0.5, 500, 1500, "https://vinfax-api.designitic.com/user/download-history-0"], "isController": false}, {"data": [0.0, 500, 1500, "https://vinfax-api.designitic.com/user/subscription"], "isController": false}, {"data": [1.0, 500, 1500, "https://vinfax-api.designitic.com/-10"], "isController": false}, {"data": [1.0, 500, 1500, "https://vinfax-api.designitic.com/-11"], "isController": false}, {"data": [0.0, 500, 1500, "https://vinfax-api.designitic.com/login"], "isController": false}, {"data": [1.0, 500, 1500, "https://vinfax-api.designitic.com/user/subscription-11"], "isController": false}, {"data": [1.0, 500, 1500, "https://vinfax-api.designitic.com/user/download-history-18"], "isController": false}, {"data": [1.0, 500, 1500, "https://vinfax-api.designitic.com/user/subscription-10"], "isController": false}, {"data": [1.0, 500, 1500, "https://vinfax-api.designitic.com/user/download-history-19"], "isController": false}, {"data": [1.0, 500, 1500, "https://vinfax-api.designitic.com/user/subscription-13"], "isController": false}, {"data": [1.0, 500, 1500, "https://vinfax-api.designitic.com/user/download-history-16"], "isController": false}, {"data": [1.0, 500, 1500, "https://vinfax-api.designitic.com/user/subscription-12"], "isController": false}, {"data": [1.0, 500, 1500, "https://vinfax-api.designitic.com/user/download-history-17"], "isController": false}, {"data": [1.0, 500, 1500, "https://vinfax-api.designitic.com/user/subscription-15"], "isController": false}, {"data": [1.0, 500, 1500, "https://vinfax-api.designitic.com/user/download-history-14"], "isController": false}, {"data": [1.0, 500, 1500, "https://vinfax-api.designitic.com/user/subscription-14"], "isController": false}, {"data": [1.0, 500, 1500, "https://vinfax-api.designitic.com/user/download-history-15"], "isController": false}, {"data": [1.0, 500, 1500, "https://vinfax-api.designitic.com/user/subscription-17"], "isController": false}, {"data": [1.0, 500, 1500, "https://vinfax-api.designitic.com/user/download-history-12"], "isController": false}, {"data": [1.0, 500, 1500, "https://vinfax-api.designitic.com/user/subscription-16"], "isController": false}, {"data": [1.0, 500, 1500, "https://vinfax-api.designitic.com/user/download-history-13"], "isController": false}, {"data": [1.0, 500, 1500, "https://vinfax-api.designitic.com/user/subscription-19"], "isController": false}, {"data": [1.0, 500, 1500, "https://vinfax-api.designitic.com/user/download-history-10"], "isController": false}, {"data": [1.0, 500, 1500, "https://vinfax-api.designitic.com/user/subscription-18"], "isController": false}, {"data": [1.0, 500, 1500, "https://vinfax-api.designitic.com/user/download-history-11"], "isController": false}, {"data": [0.5, 500, 1500, "https://vinfax-api.designitic.com/login-19"], "isController": false}, {"data": [0.5, 500, 1500, "https://vinfax-api.designitic.com/login-18"], "isController": false}, {"data": [1.0, 500, 1500, "https://vinfax-api.designitic.com/login-17"], "isController": false}, {"data": [1.0, 500, 1500, "https://vinfax-api.designitic.com/login-16"], "isController": false}, {"data": [1.0, 500, 1500, "https://vinfax-api.designitic.com/login-15"], "isController": false}, {"data": [1.0, 500, 1500, "https://vinfax-api.designitic.com/login-14"], "isController": false}, {"data": [1.0, 500, 1500, "https://vinfax-api.designitic.com/login-13"], "isController": false}, {"data": [1.0, 500, 1500, "https://vinfax-api.designitic.com/login-12"], "isController": false}, {"data": [1.0, 500, 1500, "https://vinfax-api.designitic.com/login-11"], "isController": false}, {"data": [1.0, 500, 1500, "https://vinfax-api.designitic.com/login-10"], "isController": false}, {"data": [1.0, 500, 1500, "https://vinfax-api.designitic.com/user/download-history-27"], "isController": false}, {"data": [1.0, 500, 1500, "https://vinfax-api.designitic.com/user/download-history-25"], "isController": false}, {"data": [1.0, 500, 1500, "https://vinfax-api.designitic.com/user/download-history-26"], "isController": false}, {"data": [1.0, 500, 1500, "https://vinfax-api.designitic.com/user/download-history-23"], "isController": false}, {"data": [1.0, 500, 1500, "https://vinfax-api.designitic.com/user/download-history-24"], "isController": false}, {"data": [0.5, 500, 1500, "https://vinfax-api.designitic.com/user/download-history-21"], "isController": false}, {"data": [1.0, 500, 1500, "https://vinfax-api.designitic.com/user/download-history-22"], "isController": false}, {"data": [1.0, 500, 1500, "https://vinfax-api.designitic.com/user/download-history-20"], "isController": false}, {"data": [1.0, 500, 1500, "https://vinfax-api.designitic.com/user/subscription-0"], "isController": false}, {"data": [1.0, 500, 1500, "https://vinfax-api.designitic.com/login-28"], "isController": false}, {"data": [1.0, 500, 1500, "https://vinfax-api.designitic.com/user/subscription-3"], "isController": false}, {"data": [1.0, 500, 1500, "https://vinfax-api.designitic.com/login-27"], "isController": false}, {"data": [1.0, 500, 1500, "https://vinfax-api.designitic.com/user/subscription-4"], "isController": false}, {"data": [1.0, 500, 1500, "https://vinfax-api.designitic.com/login-26"], "isController": false}, {"data": [1.0, 500, 1500, "https://vinfax-api.designitic.com/user/subscription-1"], "isController": false}, {"data": [0.5, 500, 1500, "https://vinfax-api.designitic.com/login-25"], "isController": false}, {"data": [1.0, 500, 1500, "https://vinfax-api.designitic.com/user/subscription-2"], "isController": false}, {"data": [0.5, 500, 1500, "https://vinfax-api.designitic.com/login-24"], "isController": false}, {"data": [0.5, 500, 1500, "https://vinfax-api.designitic.com/login-23"], "isController": false}, {"data": [0.5, 500, 1500, "https://vinfax-api.designitic.com/login-22"], "isController": false}, {"data": [0.0, 500, 1500, "https://vinfax-api.designitic.com/"], "isController": false}, {"data": [0.5, 500, 1500, "https://vinfax-api.designitic.com/login-21"], "isController": false}, {"data": [0.0, 500, 1500, "https://vinfax-api.designitic.com/user/download-history"], "isController": false}, {"data": [0.0, 500, 1500, "https://vinfax-api.designitic.com/login-20"], "isController": false}, {"data": [1.0, 500, 1500, "https://vinfax-api.designitic.com/login-5"], "isController": false}, {"data": [1.0, 500, 1500, "https://vinfax-api.designitic.com/login-6"], "isController": false}, {"data": [1.0, 500, 1500, "https://vinfax-api.designitic.com/login-7"], "isController": false}, {"data": [1.0, 500, 1500, "https://vinfax-api.designitic.com/user/subscription-20"], "isController": false}, {"data": [1.0, 500, 1500, "https://vinfax-api.designitic.com/login-8"], "isController": false}, {"data": [1.0, 500, 1500, "https://vinfax-api.designitic.com/login-9"], "isController": false}, {"data": [1.0, 500, 1500, "https://vinfax-api.designitic.com/user/subscription-22"], "isController": false}, {"data": [1.0, 500, 1500, "https://vinfax-api.designitic.com/user/subscription-21"], "isController": false}, {"data": [1.0, 500, 1500, "https://vinfax-api.designitic.com/user/subscription-24"], "isController": false}, {"data": [1.0, 500, 1500, "https://vinfax-api.designitic.com/user/subscription-23"], "isController": false}, {"data": [1.0, 500, 1500, "https://vinfax-api.designitic.com/user/subscription-26"], "isController": false}, {"data": [1.0, 500, 1500, "https://vinfax-api.designitic.com/user/subscription-25"], "isController": false}, {"data": [0.5, 500, 1500, "https://vinfax-api.designitic.com/login-0"], "isController": false}, {"data": [1.0, 500, 1500, "https://vinfax-api.designitic.com/user/subscription-27"], "isController": false}, {"data": [0.5, 500, 1500, "https://vinfax-api.designitic.com/login-1"], "isController": false}, {"data": [1.0, 500, 1500, "https://vinfax-api.designitic.com/login-2"], "isController": false}, {"data": [1.0, 500, 1500, "https://vinfax-api.designitic.com/login-3"], "isController": false}, {"data": [1.0, 500, 1500, "https://vinfax-api.designitic.com/login-4"], "isController": false}]}, function(index, item){
        switch(index){
            case 0:
                item = item.toFixed(3);
                break;
            case 1:
            case 2:
                item = formatDuration(item);
                break;
        }
        return item;
    }, [[0, 0]], 3);

    // Create statistics table
    createTable($("#statisticsTable"), {"supportsControllersDiscrimination": true, "overall": {"data": ["Total", 103, 0, 0.0, 541.4563106796116, 221, 3867, 420.0, 1216.2000000000003, 1674.3999999999994, 3828.919999999994, 4.920695585706095, 185.8402822980365, 11.571089943029811], "isController": false}, "titles": ["Label", "#Samples", "FAIL", "Error %", "Average", "Min", "Max", "Median", "90th pct", "95th pct", "99th pct", "Transactions/s", "Received", "Sent"], "items": [{"data": ["https://vinfax-api.designitic.com/user/download-history-6", 1, 0, 0.0, 425.0, 425, 425, 425.0, 425.0, 425.0, 425.0, 2.352941176470588, 0.9581801470588236, 3.083639705882353], "isController": false}, {"data": ["https://vinfax-api.designitic.com/user/download-history-5", 1, 0, 0.0, 419.0, 419, 419, 419.0, 419.0, 419.0, 419.0, 2.3866348448687353, 0.9719011038186158, 3.1464424224343674], "isController": false}, {"data": ["https://vinfax-api.designitic.com/-9", 1, 0, 0.0, 312.0, 312, 312, 312.0, 312.0, 312.0, 312.0, 3.205128205128205, 21.337264623397434, 3.9312900641025643], "isController": false}, {"data": ["https://vinfax-api.designitic.com/user/download-history-4", 1, 0, 0.0, 423.0, 423, 423, 423.0, 423.0, 423.0, 423.0, 2.3640661938534278, 0.9580932328605202, 3.1674793144208038], "isController": false}, {"data": ["https://vinfax-api.designitic.com/-8", 1, 0, 0.0, 228.0, 228, 228, 228.0, 228.0, 228.0, 228.0, 4.385964912280701, 26.962547971491226, 5.396792763157895], "isController": false}, {"data": ["https://vinfax-api.designitic.com/user/download-history-3", 1, 0, 0.0, 421.0, 421, 421, 421.0, 421.0, 421.0, 421.0, 2.375296912114014, 0.9649643705463183, 3.191805225653207], "isController": false}, {"data": ["https://vinfax-api.designitic.com/-7", 1, 0, 0.0, 668.0, 668, 668, 668.0, 668.0, 668.0, 668.0, 1.4970059880239521, 115.67441289296407, 1.8522525261976046], "isController": false}, {"data": ["https://vinfax-api.designitic.com/-6", 1, 0, 0.0, 983.0, 983, 983, 983.0, 983.0, 983.0, 983.0, 1.0172939979654119, 86.84452091810783, 1.2487681205493388], "isController": false}, {"data": ["https://vinfax-api.designitic.com/user/download-history-9", 1, 0, 0.0, 493.0, 493, 493, 493.0, 493.0, 493.0, 493.0, 2.028397565922921, 0.822055654158215, 2.656329234279919], "isController": false}, {"data": ["https://vinfax-api.designitic.com/-5", 1, 0, 0.0, 1715.0, 1715, 1715, 1715.0, 1715.0, 1715.0, 1715.0, 0.5830903790087464, 89.84773596938776, 1.0152833454810495], "isController": false}, {"data": ["https://vinfax-api.designitic.com/user/download-history-8", 1, 0, 0.0, 225.0, 225, 225, 225.0, 225.0, 225.0, 225.0, 4.444444444444445, 1.8098958333333333, 5.824652777777778], "isController": false}, {"data": ["https://vinfax-api.designitic.com/-4", 1, 0, 0.0, 497.0, 497, 497, 497.0, 497.0, 497.0, 497.0, 2.012072434607646, 6.067655935613682, 2.4797220824949697], "isController": false}, {"data": ["https://vinfax-api.designitic.com/user/download-history-7", 1, 0, 0.0, 228.0, 228, 228, 228.0, 228.0, 228.0, 228.0, 4.385964912280701, 1.777515076754386, 5.773711622807017], "isController": false}, {"data": ["https://vinfax-api.designitic.com/user/subscription-7", 1, 0, 0.0, 224.0, 224, 224, 224.0, 224.0, 224.0, 224.0, 4.464285714285714, 1.8092564174107142, 5.876813616071429], "isController": false}, {"data": ["https://vinfax-api.designitic.com/user/subscription-8", 1, 0, 0.0, 422.0, 422, 422, 422.0, 422.0, 422.0, 422.0, 2.3696682464454977, 0.9649918542654029, 3.1055613151658767], "isController": false}, {"data": ["https://vinfax-api.designitic.com/user/subscription-5", 1, 0, 0.0, 227.0, 227, 227, 227.0, 227.0, 227.0, 227.0, 4.405286343612335, 1.793949614537445, 5.807750550660793], "isController": false}, {"data": ["https://vinfax-api.designitic.com/user/subscription-6", 1, 0, 0.0, 419.0, 419, 419, 419.0, 419.0, 419.0, 419.0, 2.3866348448687353, 0.9719011038186158, 3.1277968377088308], "isController": false}, {"data": ["https://vinfax-api.designitic.com/user/subscription-9", 1, 0, 0.0, 225.0, 225, 225, 225.0, 225.0, 225.0, 225.0, 4.444444444444445, 1.8012152777777777, 5.8203125], "isController": false}, {"data": ["https://vinfax-api.designitic.com/-3", 1, 0, 0.0, 1342.0, 1342, 1342, 1342.0, 1342.0, 1342.0, 1342.0, 0.7451564828614009, 210.44194183122204, 0.9125256147540983], "isController": false}, {"data": ["https://vinfax-api.designitic.com/-2", 1, 0, 0.0, 1194.0, 1194, 1194, 1194.0, 1194.0, 1194.0, 1194.0, 0.8375209380234506, 127.78328491415411, 1.0321791247906198], "isController": false}, {"data": ["https://vinfax-api.designitic.com/-1", 2, 0, 0.0, 594.0, 567, 621, 594.0, 621.0, 621.0, 621.0, 1.1655011655011656, 15.513457896270397, 1.0175371503496504], "isController": false}, {"data": ["https://vinfax-api.designitic.com/-0", 2, 0, 0.0, 991.0, 874, 1108, 991.0, 1108.0, 1108.0, 1108.0, 0.9643201542912248, 75.07430162126326, 0.8282417731436837], "isController": false}, {"data": ["https://vinfax-api.designitic.com/user/download-history-2", 1, 0, 0.0, 224.0, 224, 224, 224.0, 224.0, 224.0, 224.0, 4.464285714285714, 1.8136160714285714, 5.990164620535714], "isController": false}, {"data": ["https://vinfax-api.designitic.com/user/download-history-1", 1, 0, 0.0, 223.0, 223, 223, 223.0, 223.0, 223.0, 223.0, 4.484304932735426, 1.7210271860986546, 5.8944086322869955], "isController": false}, {"data": ["https://vinfax-api.designitic.com/user/download-history-0", 1, 0, 0.0, 665.0, 665, 665, 665.0, 665.0, 665.0, 665.0, 1.5037593984962407, 102.21452067669172, 1.8429863721804511], "isController": false}, {"data": ["https://vinfax-api.designitic.com/user/subscription", 1, 0, 0.0, 1851.0, 1851, 1851, 1851.0, 1851.0, 1851.0, 1851.0, 0.5402485143165856, 21.441640498379254, 18.78735311993517], "isController": false}, {"data": ["https://vinfax-api.designitic.com/-10", 1, 0, 0.0, 228.0, 228, 228, 228.0, 228.0, 228.0, 228.0, 4.385964912280701, 22.323876096491226, 5.431058114035087], "isController": false}, {"data": ["https://vinfax-api.designitic.com/-11", 1, 0, 0.0, 230.0, 230, 230, 230.0, 230.0, 230.0, 230.0, 4.3478260869565215, 11.15828804347826, 5.307404891304348], "isController": false}, {"data": ["https://vinfax-api.designitic.com/login", 1, 0, 0.0, 3867.0, 3867, 3867, 3867.0, 3867.0, 3867.0, 3867.0, 0.2585983966899405, 244.56059485712439, 9.346665292862685], "isController": false}, {"data": ["https://vinfax-api.designitic.com/user/subscription-11", 1, 0, 0.0, 424.0, 424, 424, 424.0, 424.0, 424.0, 424.0, 2.3584905660377355, 0.9604400058962265, 3.0978220813679247], "isController": false}, {"data": ["https://vinfax-api.designitic.com/user/download-history-18", 1, 0, 0.0, 224.0, 224, 224, 224.0, 224.0, 224.0, 224.0, 4.464285714285714, 1.8179757254464286, 5.950927734375], "isController": false}, {"data": ["https://vinfax-api.designitic.com/user/subscription-10", 1, 0, 0.0, 224.0, 224, 224, 224.0, 224.0, 224.0, 224.0, 4.464285714285714, 1.708984375, 5.902971540178571], "isController": false}, {"data": ["https://vinfax-api.designitic.com/user/download-history-19", 1, 0, 0.0, 268.0, 268, 268, 268.0, 268.0, 268.0, 268.0, 3.7313432835820897, 1.9421933302238805, 2.2409923041044775], "isController": false}, {"data": ["https://vinfax-api.designitic.com/user/subscription-13", 1, 0, 0.0, 231.0, 231, 231, 231.0, 231.0, 231.0, 231.0, 4.329004329004329, 1.762885551948052, 5.728321158008658], "isController": false}, {"data": ["https://vinfax-api.designitic.com/user/download-history-16", 1, 0, 0.0, 421.0, 421, 421, 421.0, 421.0, 421.0, 421.0, 2.375296912114014, 0.9649643705463183, 3.1430930819477436], "isController": false}, {"data": ["https://vinfax-api.designitic.com/user/subscription-12", 1, 0, 0.0, 420.0, 420, 420, 420.0, 420.0, 420.0, 420.0, 2.3809523809523814, 0.964936755952381, 3.1156994047619047], "isController": false}, {"data": ["https://vinfax-api.designitic.com/user/download-history-17", 1, 0, 0.0, 420.0, 420, 420, 420.0, 420.0, 420.0, 420.0, 2.3809523809523814, 0.9695870535714286, 3.1459263392857144], "isController": false}, {"data": ["https://vinfax-api.designitic.com/user/subscription-15", 1, 0, 0.0, 225.0, 225, 225, 225.0, 225.0, 225.0, 225.0, 4.444444444444445, 1.8055555555555556, 5.828993055555555], "isController": false}, {"data": ["https://vinfax-api.designitic.com/user/download-history-14", 1, 0, 0.0, 422.0, 422, 422, 422.0, 422.0, 422.0, 422.0, 2.3696682464454977, 0.9626777251184835, 3.117131960900474], "isController": false}, {"data": ["https://vinfax-api.designitic.com/user/subscription-14", 1, 0, 0.0, 227.0, 227, 227, 227.0, 227.0, 227.0, 227.0, 4.405286343612335, 1.7896475770925109, 5.794844438325991], "isController": false}, {"data": ["https://vinfax-api.designitic.com/user/download-history-15", 1, 0, 0.0, 227.0, 227, 227, 227.0, 227.0, 227.0, 227.0, 4.405286343612335, 1.7896475770925109, 5.7776362885462555], "isController": false}, {"data": ["https://vinfax-api.designitic.com/user/subscription-17", 1, 0, 0.0, 424.0, 424, 424, 424.0, 424.0, 424.0, 424.0, 2.3584905660377355, 0.9604400058962265, 3.1162477889150946], "isController": false}, {"data": ["https://vinfax-api.designitic.com/user/download-history-12", 1, 0, 0.0, 420.0, 420, 420, 420.0, 420.0, 420.0, 420.0, 2.3809523809523814, 0.964936755952381, 3.1156994047619047], "isController": false}, {"data": ["https://vinfax-api.designitic.com/user/subscription-16", 1, 0, 0.0, 426.0, 426, 426, 426.0, 426.0, 426.0, 426.0, 2.347417840375587, 0.9536384976525821, 3.1062023180751175], "isController": false}, {"data": ["https://vinfax-api.designitic.com/user/download-history-13", 1, 0, 0.0, 223.0, 223, 223, 223.0, 223.0, 223.0, 223.0, 4.484304932735426, 1.8261280829596411, 5.933821468609866], "isController": false}, {"data": ["https://vinfax-api.designitic.com/user/subscription-19", 1, 0, 0.0, 272.0, 272, 272, 272.0, 272.0, 272.0, 272.0, 3.676470588235294, 1.9136316636029411, 2.2080365349264706], "isController": false}, {"data": ["https://vinfax-api.designitic.com/user/download-history-10", 1, 0, 0.0, 238.0, 238, 238, 238.0, 238.0, 238.0, 238.0, 4.201680672268908, 1.6084558823529413, 5.555737920168068], "isController": false}, {"data": ["https://vinfax-api.designitic.com/user/subscription-18", 1, 0, 0.0, 226.0, 226, 226, 226.0, 226.0, 226.0, 226.0, 4.424778761061947, 1.8018874446902655, 5.898264657079646], "isController": false}, {"data": ["https://vinfax-api.designitic.com/user/download-history-11", 1, 0, 0.0, 235.0, 235, 235, 235.0, 235.0, 235.0, 235.0, 4.25531914893617, 1.7328789893617023, 5.589261968085107], "isController": false}, {"data": ["https://vinfax-api.designitic.com/login-19", 1, 0, 0.0, 932.0, 932, 932, 932.0, 932.0, 932.0, 932.0, 1.0729613733905579, 432.7754073900214, 1.3894011534334763], "isController": false}, {"data": ["https://vinfax-api.designitic.com/login-18", 1, 0, 0.0, 1231.0, 1231, 1231, 1231.0, 1231.0, 1231.0, 1231.0, 0.8123476848090982, 117.07167699025182, 1.0424070877335498], "isController": false}, {"data": ["https://vinfax-api.designitic.com/login-17", 1, 0, 0.0, 424.0, 424, 424, 424.0, 424.0, 424.0, 424.0, 2.3584905660377355, 0.9581367924528302, 3.233711674528302], "isController": false}, {"data": ["https://vinfax-api.designitic.com/login-16", 1, 0, 0.0, 425.0, 425, 425, 425.0, 425.0, 425.0, 425.0, 2.352941176470588, 0.9558823529411765, 3.198529411764706], "isController": false}, {"data": ["https://vinfax-api.designitic.com/login-15", 1, 0, 0.0, 227.0, 227, 227, 227.0, 227.0, 227.0, 227.0, 4.405286343612335, 1.7896475770925109, 6.0056442731277535], "isController": false}, {"data": ["https://vinfax-api.designitic.com/login-14", 1, 0, 0.0, 423.0, 423, 423, 423.0, 423.0, 423.0, 423.0, 2.3640661938534278, 0.96271054964539, 3.2413563829787235], "isController": false}, {"data": ["https://vinfax-api.designitic.com/login-13", 1, 0, 0.0, 422.0, 422, 422, 422.0, 422.0, 422.0, 422.0, 2.3696682464454977, 2.1359412026066353, 3.015310278436019], "isController": false}, {"data": ["https://vinfax-api.designitic.com/login-12", 1, 0, 0.0, 422.0, 422, 422, 422.0, 422.0, 422.0, 422.0, 2.3696682464454977, 0.9649918542654029, 3.2258960308056874], "isController": false}, {"data": ["https://vinfax-api.designitic.com/login-11", 1, 0, 0.0, 223.0, 223, 223, 223.0, 223.0, 223.0, 223.0, 4.484304932735426, 3.8580787556053813, 5.767411715246637], "isController": false}, {"data": ["https://vinfax-api.designitic.com/login-10", 1, 0, 0.0, 226.0, 226, 226, 226.0, 226.0, 226.0, 226.0, 4.424778761061947, 4.09637721238938, 5.6346792035398225], "isController": false}, {"data": ["https://vinfax-api.designitic.com/user/download-history-27", 1, 0, 0.0, 427.0, 427, 427, 427.0, 427.0, 427.0, 427.0, 2.34192037470726, 0.9491181206088993, 3.0554742388758784], "isController": false}, {"data": ["https://vinfax-api.designitic.com/user/download-history-25", 1, 0, 0.0, 228.0, 228, 228, 228.0, 228.0, 228.0, 228.0, 4.385964912280701, 1.777515076754386, 5.885074013157895], "isController": false}, {"data": ["https://vinfax-api.designitic.com/user/download-history-26", 1, 0, 0.0, 231.0, 231, 231, 231.0, 231.0, 231.0, 231.0, 4.329004329004329, 1.7544304653679652, 5.745231331168831], "isController": false}, {"data": ["https://vinfax-api.designitic.com/user/download-history-23", 1, 0, 0.0, 231.0, 231, 231, 231.0, 231.0, 231.0, 231.0, 4.329004329004329, 1.762885551948052, 5.825554653679653], "isController": false}, {"data": ["https://vinfax-api.designitic.com/user/download-history-24", 1, 0, 0.0, 426.0, 426, 426, 426.0, 426.0, 426.0, 426.0, 2.347417840375587, 0.955930897887324, 3.145173122065728], "isController": false}, {"data": ["https://vinfax-api.designitic.com/user/download-history-21", 1, 0, 0.0, 847.0, 847, 847, 847.0, 847.0, 847.0, 847.0, 1.1806375442739079, 0.5361293536009445, 0.6894738783943329], "isController": false}, {"data": ["https://vinfax-api.designitic.com/user/download-history-22", 1, 0, 0.0, 232.0, 232, 232, 232.0, 232.0, 232.0, 232.0, 4.310344827586206, 1.755286907327586, 5.800444504310344], "isController": false}, {"data": ["https://vinfax-api.designitic.com/user/download-history-20", 1, 0, 0.0, 276.0, 276, 276, 276.0, 276.0, 276.0, 276.0, 3.6231884057971016, 1.7195991847826086, 2.1265002264492754], "isController": false}, {"data": ["https://vinfax-api.designitic.com/user/subscription-0", 1, 0, 0.0, 263.0, 263, 263, 263.0, 263.0, 263.0, 263.0, 3.802281368821293, 108.48755346958174, 4.645169914448669], "isController": false}, {"data": ["https://vinfax-api.designitic.com/login-28", 1, 0, 0.0, 231.0, 231, 231, 231.0, 231.0, 231.0, 231.0, 4.329004329004329, 1.7544304653679652, 5.855147456709957], "isController": false}, {"data": ["https://vinfax-api.designitic.com/user/subscription-3", 1, 0, 0.0, 229.0, 229, 229, 229.0, 229.0, 229.0, 229.0, 4.366812227074235, 1.7740174672489082, 5.867903930131004], "isController": false}, {"data": ["https://vinfax-api.designitic.com/login-27", 1, 0, 0.0, 228.0, 228, 228, 228.0, 228.0, 228.0, 228.0, 4.385964912280701, 18.713164747807017, 5.66234923245614], "isController": false}, {"data": ["https://vinfax-api.designitic.com/user/subscription-4", 1, 0, 0.0, 227.0, 227, 227, 227.0, 227.0, 227.0, 227.0, 4.405286343612335, 1.785345539647577, 5.902395374449339], "isController": false}, {"data": ["https://vinfax-api.designitic.com/login-26", 1, 0, 0.0, 226.0, 226, 226, 226.0, 226.0, 226.0, 226.0, 4.424778761061947, 11.048983683628318, 5.777274612831858], "isController": false}, {"data": ["https://vinfax-api.designitic.com/user/subscription-1", 1, 0, 0.0, 224.0, 224, 224, 224.0, 224.0, 224.0, 224.0, 4.464285714285714, 1.7133440290178572, 5.868094308035714], "isController": false}, {"data": ["https://vinfax-api.designitic.com/login-25", 1, 0, 0.0, 682.0, 682, 682, 682.0, 682.0, 682.0, 682.0, 1.466275659824047, 119.93390304252199, 1.9087357954545454], "isController": false}, {"data": ["https://vinfax-api.designitic.com/user/subscription-2", 1, 0, 0.0, 225.0, 225, 225, 225.0, 225.0, 225.0, 225.0, 4.444444444444445, 1.8055555555555556, 5.963541666666667], "isController": false}, {"data": ["https://vinfax-api.designitic.com/login-24", 1, 0, 0.0, 821.0, 821, 821, 821.0, 821.0, 821.0, 821.0, 1.2180267965895248, 133.88541032277712, 1.5927127740560294], "isController": false}, {"data": ["https://vinfax-api.designitic.com/login-23", 1, 0, 0.0, 822.0, 822, 822, 822.0, 822.0, 822.0, 822.0, 1.2165450121654502, 125.11523912712896, 1.5907751672749393], "isController": false}, {"data": ["https://vinfax-api.designitic.com/login-22", 1, 0, 0.0, 1373.0, 1373, 1373, 1373.0, 1373.0, 1373.0, 1373.0, 0.7283321194464676, 16.00339129643117, 0.40186293699927167], "isController": false}, {"data": ["https://vinfax-api.designitic.com/", 1, 0, 0.0, 2915.0, 2915, 2915, 2915.0, 2915.0, 2915.0, 2915.0, 0.34305317324185247, 275.6180987349914, 4.985996462264151], "isController": false}, {"data": ["https://vinfax-api.designitic.com/login-21", 1, 0, 0.0, 1268.0, 1268, 1268, 1268.0, 1268.0, 1268.0, 1268.0, 0.7886435331230284, 0.42743863367507884, 0.43976118888012616], "isController": false}, {"data": ["https://vinfax-api.designitic.com/user/download-history", 1, 0, 0.0, 2443.0, 2443, 2443, 2443.0, 2443.0, 2443.0, 2443.0, 0.4093327875562833, 32.3900557715923, 14.23630653909128], "isController": false}, {"data": ["https://vinfax-api.designitic.com/login-20", 1, 0, 0.0, 1512.0, 1512, 1512, 1512.0, 1512.0, 1512.0, 1512.0, 0.6613756613756614, 15.595935639880953, 0.37589905753968256], "isController": false}, {"data": ["https://vinfax-api.designitic.com/login-5", 1, 0, 0.0, 423.0, 423, 423, 423.0, 423.0, 423.0, 423.0, 2.3640661938534278, 7.6208813534278965, 3.0820589539007095], "isController": false}, {"data": ["https://vinfax-api.designitic.com/login-6", 1, 0, 0.0, 440.0, 440, 440, 440.0, 440.0, 440.0, 440.0, 2.2727272727272725, 0.9255149147727273, 3.1050248579545454], "isController": false}, {"data": ["https://vinfax-api.designitic.com/login-7", 1, 0, 0.0, 436.0, 436, 436, 436.0, 436.0, 436.0, 436.0, 2.293577981651376, 0.934005877293578, 3.115592746559633], "isController": false}, {"data": ["https://vinfax-api.designitic.com/user/subscription-20", 1, 0, 0.0, 258.0, 258, 258, 258.0, 258.0, 258.0, 258.0, 3.875968992248062, 1.8395712209302324, 2.274860707364341], "isController": false}, {"data": ["https://vinfax-api.designitic.com/login-8", 1, 0, 0.0, 226.0, 226, 226, 226.0, 226.0, 226.0, 226.0, 4.424778761061947, 1.7932452986725662, 6.036538993362831], "isController": false}, {"data": ["https://vinfax-api.designitic.com/login-9", 1, 0, 0.0, 226.0, 226, 226, 226.0, 226.0, 226.0, 226.0, 4.424778761061947, 1.8018874446902655, 6.010612555309734], "isController": false}, {"data": ["https://vinfax-api.designitic.com/user/subscription-22", 1, 0, 0.0, 232.0, 232, 232, 232.0, 232.0, 232.0, 232.0, 4.310344827586206, 1.755286907327586, 5.800444504310344], "isController": false}, {"data": ["https://vinfax-api.designitic.com/user/subscription-21", 1, 0, 0.0, 269.0, 269, 269, 269.0, 269.0, 269.0, 269.0, 3.717472118959108, 1.6881098977695166, 2.1709456319702602], "isController": false}, {"data": ["https://vinfax-api.designitic.com/user/subscription-24", 1, 0, 0.0, 424.0, 424, 424, 424.0, 424.0, 424.0, 424.0, 2.3584905660377355, 0.9604400058962265, 3.1600088443396226], "isController": false}, {"data": ["https://vinfax-api.designitic.com/user/subscription-23", 1, 0, 0.0, 221.0, 221, 221, 221.0, 221.0, 221.0, 221.0, 4.524886877828055, 1.842654128959276, 6.089154411764706], "isController": false}, {"data": ["https://vinfax-api.designitic.com/user/subscription-26", 1, 0, 0.0, 227.0, 227, 227, 227.0, 227.0, 227.0, 227.0, 4.405286343612335, 1.785345539647577, 5.846468887665198], "isController": false}, {"data": ["https://vinfax-api.designitic.com/user/subscription-25", 1, 0, 0.0, 431.0, 431, 431, 431.0, 431.0, 431.0, 431.0, 2.320185614849188, 0.9403095997679815, 3.113217807424594], "isController": false}, {"data": ["https://vinfax-api.designitic.com/login-0", 1, 0, 0.0, 523.0, 523, 523, 523.0, 523.0, 523.0, 523.0, 1.9120458891013383, 3.4151679015296366, 2.6234614005736137], "isController": false}, {"data": ["https://vinfax-api.designitic.com/user/subscription-27", 1, 0, 0.0, 433.0, 433, 433, 433.0, 433.0, 433.0, 433.0, 2.3094688221709005, 0.9359663683602771, 3.013135103926097], "isController": false}, {"data": ["https://vinfax-api.designitic.com/login-1", 1, 0, 0.0, 641.0, 641, 641, 641.0, 641.0, 641.0, 641.0, 1.5600624024960998, 41.55646694617785, 1.9759774765990639], "isController": false}, {"data": ["https://vinfax-api.designitic.com/login-2", 1, 0, 0.0, 424.0, 424, 424, 424.0, 424.0, 424.0, 424.0, 2.3584905660377355, 0.905162883254717, 3.212982753537736], "isController": false}, {"data": ["https://vinfax-api.designitic.com/login-3", 1, 0, 0.0, 225.0, 225, 225, 225.0, 225.0, 225.0, 225.0, 4.444444444444445, 30.60763888888889, 5.798611111111111], "isController": false}, {"data": ["https://vinfax-api.designitic.com/login-4", 1, 0, 0.0, 424.0, 424, 424, 424.0, 424.0, 424.0, 424.0, 2.3584905660377355, 12.179392688679245, 3.081699587264151], "isController": false}]}, function(index, item){
        switch(index){
            // Errors pct
            case 3:
                item = item.toFixed(2) + '%';
                break;
            // Mean
            case 4:
            // Mean
            case 7:
            // Median
            case 8:
            // Percentile 1
            case 9:
            // Percentile 2
            case 10:
            // Percentile 3
            case 11:
            // Throughput
            case 12:
            // Kbytes/s
            case 13:
            // Sent Kbytes/s
                item = item.toFixed(2);
                break;
        }
        return item;
    }, [[0, 0]], 0, summaryTableHeader);

    // Create error table
    createTable($("#errorsTable"), {"supportsControllersDiscrimination": false, "titles": ["Type of error", "Number of errors", "% in errors", "% in all samples"], "items": []}, function(index, item){
        switch(index){
            case 2:
            case 3:
                item = item.toFixed(2) + '%';
                break;
        }
        return item;
    }, [[1, 1]]);

        // Create top5 errors by sampler
    createTable($("#top5ErrorsBySamplerTable"), {"supportsControllersDiscrimination": false, "overall": {"data": ["Total", 103, 0, "", "", "", "", "", "", "", "", "", ""], "isController": false}, "titles": ["Sample", "#Samples", "#Errors", "Error", "#Errors", "Error", "#Errors", "Error", "#Errors", "Error", "#Errors", "Error", "#Errors"], "items": [{"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}]}, function(index, item){
        return item;
    }, [[0, 0]], 0);

});
