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

    var data = {"OkPercent": 99.64636542239685, "KoPercent": 0.35363457760314343};
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
    createTable($("#apdexTable"), {"supportsControllersDiscrimination": true, "overall": {"data": [0.6265212046711739, 500, 1500, "Total"], "isController": false}, "titles": ["Apdex", "T (Toleration threshold)", "F (Frustration threshold)", "Label"], "items": [{"data": [0.9351851851851852, 500, 1500, "subscription-0"], "isController": false}, {"data": [0.9259259259259259, 500, 1500, "subscription-1"], "isController": false}, {"data": [0.661, 500, 1500, "documentation"], "isController": false}, {"data": [0.47674418604651164, 500, 1500, "login-1"], "isController": false}, {"data": [0.5607822410147991, 500, 1500, "login-0"], "isController": false}, {"data": [0.7275, 500, 1500, "subscription"], "isController": false}, {"data": [0.708, 500, 1500, "contact us"], "isController": false}, {"data": [0.217, 500, 1500, "login"], "isController": false}, {"data": [0.9985, 500, 1500, "documentation-0"], "isController": false}, {"data": [0.7935, 500, 1500, "documentation-1"], "isController": false}, {"data": [0.144, 500, 1500, "home"], "isController": false}, {"data": [0.9351851851851852, 500, 1500, "documentation-2"], "isController": false}, {"data": [0.9885, 500, 1500, "downlaod history-0"], "isController": false}, {"data": [0.4845, 500, 1500, "downlaod history"], "isController": false}, {"data": [0.9907407407407407, 500, 1500, "transaction-1"], "isController": false}, {"data": [0.9975, 500, 1500, "contact us-0"], "isController": false}, {"data": [0.0, 500, 1500, "Test"], "isController": true}, {"data": [0.9629629629629629, 500, 1500, "transaction-0"], "isController": false}, {"data": [0.9259259259259259, 500, 1500, "downlaod history-2"], "isController": false}, {"data": [0.827, 500, 1500, "contact us-1"], "isController": false}, {"data": [0.5215, 500, 1500, "downlaod history-1"], "isController": false}, {"data": [0.9074074074074074, 500, 1500, "contact us-2"], "isController": false}, {"data": [0.788, 500, 1500, "transaction"], "isController": false}]}, function(index, item){
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
    createTable($("#statisticsTable"), {"supportsControllersDiscrimination": true, "overall": {"data": ["Total", 15270, 54, 0.35363457760314343, 3167.6379829731527, 19, 69536, 508.0, 11972.8, 24034.24999999997, 32061.619999999926, 74.83533286285581, 1727.8257166742017, 115.14728994525798], "isController": false}, "titles": ["Label", "#Samples", "FAIL", "Error %", "Average", "Min", "Max", "Median", "90th pct", "95th pct", "99th pct", "Transactions/s", "Received", "Sent"], "items": [{"data": ["subscription-0", 54, 0, 0.0, 884.7407407407408, 232, 30432, 283.0, 512.5, 1317.0, 30432.0, 0.3963564565732783, 0.683560060848056, 0.48422063200504983], "isController": false}, {"data": ["subscription-1", 54, 0, 0.0, 1385.0555555555552, 231, 30111, 248.5, 518.0, 8925.75, 30111.0, 0.3995826581126379, 3.4201691427842036, 0.4815283204208938], "isController": false}, {"data": ["documentation", 1000, 0, 0.0, 642.846000000001, 455, 31117, 520.0, 753.4999999999999, 856.0, 1527.99, 6.618878364872288, 180.97964855203762, 16.61594434019711], "isController": false}, {"data": ["login-1", 946, 0, 0.0, 6666.331923890061, 245, 31456, 626.5, 30653.0, 30691.3, 30755.12, 6.250165173498243, 166.45255406747998, 7.916468974635958], "isController": false}, {"data": ["login-0", 946, 0, 0.0, 5143.050739957716, 309, 30684, 539.0, 18769.600000000006, 28945.25, 29902.929999999997, 6.116880261745574, 10.925560545637358, 8.392789812258332], "isController": false}, {"data": ["subscription", 1000, 0, 0.0, 1535.3639999999991, 267, 30815, 498.0, 774.0, 1829.8999999999808, 30690.89, 6.304097032661527, 173.79099608476173, 8.111821482156254], "isController": false}, {"data": ["contact us", 1000, 0, 0.0, 657.4410000000005, 455, 29801, 513.0, 767.6999999999999, 882.8499999999998, 1531.960000000001, 6.4400623398034496, 156.7931790079728, 16.091577485220057], "isController": false}, {"data": ["login", 1000, 54, 5.4, 12352.868999999997, 40, 48475, 4974.0, 31132.4, 34384.84999999999, 46402.84, 6.446912895759866, 173.77764516836112, 16.57034156147454], "isController": false}, {"data": ["documentation-0", 1000, 0, 0.0, 37.81499999999994, 19, 1062, 24.0, 35.0, 51.94999999999993, 277.98, 6.6467264872050515, 3.849129694250582, 8.126661681621801], "isController": false}, {"data": ["documentation-1", 1000, 0, 0.0, 587.6120000000009, 232, 30838, 490.0, 642.9, 786.5499999999994, 1493.800000000002, 6.62001760924684, 174.11709781944896, 8.094005905055708], "isController": false}, {"data": ["home", 1000, 0, 0.0, 17600.292000000005, 234, 69536, 13785.0, 30549.7, 59121.299999999996, 60447.8, 6.441514271174868, 55.123887429706976, 3.5038314932074233], "isController": false}, {"data": ["documentation-2", 54, 0, 0.0, 319.3333333333333, 232, 684, 248.0, 584.0, 647.5, 684.0, 0.4504579655983584, 3.8559221406346453, 0.5428370405745842], "isController": false}, {"data": ["downlaod history-0", 1000, 0, 0.0, 73.81900000000006, 20, 2126, 45.0, 57.0, 270.7999999999997, 1054.0, 6.5444597875668356, 3.80908011073226, 8.020797884176151], "isController": false}, {"data": ["downlaod history", 1000, 0, 0.0, 1019.6869999999999, 491, 31427, 767.5, 1005.3999999999999, 1155.9499999999998, 4208.430000000012, 6.516865648297795, 426.41958462720265, 16.398037731022885], "isController": false}, {"data": ["transaction-1", 54, 0, 0.0, 261.6851851851853, 232, 602, 239.5, 309.5, 350.75, 602.0, 0.4344013707776589, 3.7184697633518087, 0.523487589394171], "isController": false}, {"data": ["contact us-0", 1000, 0, 0.0, 41.013000000000034, 19, 1050, 24.0, 41.89999999999998, 264.89999999999986, 286.98, 6.468514505643779, 3.708025405090721, 7.87086823635952], "isController": false}, {"data": ["Test", 1000, 54, 5.4, 34667.31200000003, 3761, 113114, 32866.5, 57137.0, 63316.799999999996, 76388.20000000003, 6.2510548655085545, 1296.7356576383202, 82.58926652857043], "isController": true}, {"data": ["transaction-0", 54, 0, 0.0, 1381.740740740741, 230, 30588, 241.5, 299.0, 7988.25, 30588.0, 0.41465737015081244, 0.7151219879749362, 0.5061735475473784], "isController": false}, {"data": ["downlaod history-2", 54, 0, 0.0, 1420.3333333333333, 232, 30853, 251.0, 607.0, 8182.5, 30853.0, 0.43470210830522527, 3.721366388470734, 0.5238500016100078], "isController": false}, {"data": ["contact us-1", 1000, 0, 0.0, 598.2309999999999, 232, 29772, 479.0, 637.5999999999999, 795.8499999999998, 1359.91, 6.441265322159885, 150.1529272128967, 7.8377115150500165], "isController": false}, {"data": ["downlaod history-1", 1000, 0, 0.0, 869.029999999999, 231, 31024, 715.0, 882.6999999999999, 982.8499999999998, 1477.0600000000018, 6.518522381346596, 419.720628352965, 7.989009363857401], "isController": false}, {"data": ["contact us-2", 54, 0, 0.0, 334.5925925925925, 231, 1094, 256.5, 560.5, 674.25, 1094.0, 0.4452506596306069, 3.810993285166557, 0.5365618300626649], "isController": false}, {"data": ["transaction", 1000, 0, 0.0, 858.8129999999998, 336, 60405, 482.5, 674.8, 823.7999999999997, 21629.05000000004, 6.284407129031448, 171.18264735756392, 8.080348305409618], "isController": false}]}, function(index, item){
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
    createTable($("#errorsTable"), {"supportsControllersDiscrimination": false, "titles": ["Type of error", "Number of errors", "% in errors", "% in all samples"], "items": [{"data": ["502/Bad Gateway", 15, 27.77777777777778, 0.09823182711198428], "isController": false}, {"data": ["504/Gateway Time-out", 39, 72.22222222222223, 0.2554027504911591], "isController": false}]}, function(index, item){
        switch(index){
            case 2:
            case 3:
                item = item.toFixed(2) + '%';
                break;
        }
        return item;
    }, [[1, 1]]);

        // Create top5 errors by sampler
    createTable($("#top5ErrorsBySamplerTable"), {"supportsControllersDiscrimination": false, "overall": {"data": ["Total", 15270, 54, "504/Gateway Time-out", 39, "502/Bad Gateway", 15, "", "", "", "", "", ""], "isController": false}, "titles": ["Sample", "#Samples", "#Errors", "Error", "#Errors", "Error", "#Errors", "Error", "#Errors", "Error", "#Errors", "Error", "#Errors"], "items": [{"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": ["login", 1000, 54, "504/Gateway Time-out", 39, "502/Bad Gateway", 15, "", "", "", "", "", ""], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}]}, function(index, item){
        return item;
    }, [[0, 0]], 0);

});
