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
$(document).ready(function() {

    $(".click-title").mouseenter( function(    e){
        e.preventDefault();
        this.style.cursor="pointer";
    });
    $(".click-title").mousedown( function(event){
        event.preventDefault();
    });

    // Ugly code while this script is shared among several pages
    try{
        refreshHitsPerSecond(true);
    } catch(e){}
    try{
        refreshResponseTimeOverTime(true);
    } catch(e){}
    try{
        refreshResponseTimePercentiles();
    } catch(e){}
});


var responseTimePercentilesInfos = {
        getOptions: function() {
            return {
                series: {
                    points: { show: false }
                },
                legend: {
                    noColumns: 2,
                    show: true,
                    container: '#legendResponseTimePercentiles'
                },
                xaxis: {
                    tickDecimals: 1,
                    axisLabel: "Percentiles",
                    axisLabelUseCanvas: true,
                    axisLabelFontSizePixels: 12,
                    axisLabelFontFamily: 'Verdana, Arial',
                    axisLabelPadding: 20,
                },
                yaxis: {
                    axisLabel: "Percentile value in ms",
                    axisLabelUseCanvas: true,
                    axisLabelFontSizePixels: 12,
                    axisLabelFontFamily: 'Verdana, Arial',
                    axisLabelPadding: 20
                },
                grid: {
                    hoverable: true // IMPORTANT! this is needed for tooltip to
                                    // work
                },
                tooltip: true,
                tooltipOpts: {
                    content: "%s : %x.2 percentile was %y ms"
                },
                selection: { mode: "xy" },
            };
        },
        createGraph: function() {
            var data = this.data;
            var dataset = prepareData(data.result.series, $("#choicesResponseTimePercentiles"));
            var options = this.getOptions();
            prepareOptions(options, data);
            $.plot($("#flotResponseTimesPercentiles"), dataset, options);
            // setup overview
            $.plot($("#overviewResponseTimesPercentiles"), dataset, prepareOverviewOptions(options));
        }
};

/**
 * @param elementId Id of element where we display message
 */
function setEmptyGraph(elementId) {
    $(function() {
        $(elementId).text("No graph series with filter="+seriesFilter);
    });
}

// Response times percentiles
function refreshResponseTimePercentiles() {
    var infos = responseTimePercentilesInfos;
    prepareSeries(infos.data);
    if(infos.data.result.series.length == 0) {
        setEmptyGraph("#bodyResponseTimePercentiles");
        return;
    }
    if (isGraph($("#flotResponseTimesPercentiles"))){
        infos.createGraph();
    } else {
        var choiceContainer = $("#choicesResponseTimePercentiles");
        createLegend(choiceContainer, infos);
        infos.createGraph();
        setGraphZoomable("#flotResponseTimesPercentiles", "#overviewResponseTimesPercentiles");
        $('#bodyResponseTimePercentiles .legendColorBox > div').each(function(i){
            $(this).clone().prependTo(choiceContainer.find("li").eq(i));
        });
    }
}

var responseTimeDistributionInfos = {
        data: {"result": {"minY": 1.0, "minX": 200.0, "maxY": 1.0, "series": [{"data": [[400.0, 1.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-6", "isController": false}, {"data": [[400.0, 1.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-5", "isController": false}, {"data": [[300.0, 1.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/-9", "isController": false}, {"data": [[400.0, 1.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-4", "isController": false}, {"data": [[200.0, 1.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/-8", "isController": false}, {"data": [[400.0, 1.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-3", "isController": false}, {"data": [[600.0, 1.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/-7", "isController": false}, {"data": [[900.0, 1.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/-6", "isController": false}, {"data": [[400.0, 1.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-9", "isController": false}, {"data": [[1700.0, 1.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/-5", "isController": false}, {"data": [[200.0, 1.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-8", "isController": false}, {"data": [[400.0, 1.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/-4", "isController": false}, {"data": [[200.0, 1.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-7", "isController": false}, {"data": [[200.0, 1.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-7", "isController": false}, {"data": [[400.0, 1.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-8", "isController": false}, {"data": [[200.0, 1.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-5", "isController": false}, {"data": [[400.0, 1.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-6", "isController": false}, {"data": [[200.0, 1.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-9", "isController": false}, {"data": [[1300.0, 1.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/-3", "isController": false}, {"data": [[1100.0, 1.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/-2", "isController": false}, {"data": [[600.0, 1.0], [500.0, 1.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/-1", "isController": false}, {"data": [[1100.0, 1.0], [800.0, 1.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/-0", "isController": false}, {"data": [[200.0, 1.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-2", "isController": false}, {"data": [[200.0, 1.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-1", "isController": false}, {"data": [[600.0, 1.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-0", "isController": false}, {"data": [[1800.0, 1.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription", "isController": false}, {"data": [[200.0, 1.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/-10", "isController": false}, {"data": [[200.0, 1.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/-11", "isController": false}, {"data": [[3800.0, 1.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login", "isController": false}, {"data": [[400.0, 1.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-11", "isController": false}, {"data": [[200.0, 1.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-18", "isController": false}, {"data": [[200.0, 1.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-10", "isController": false}, {"data": [[200.0, 1.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-19", "isController": false}, {"data": [[200.0, 1.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-13", "isController": false}, {"data": [[400.0, 1.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-16", "isController": false}, {"data": [[400.0, 1.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-12", "isController": false}, {"data": [[400.0, 1.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-17", "isController": false}, {"data": [[200.0, 1.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-15", "isController": false}, {"data": [[400.0, 1.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-14", "isController": false}, {"data": [[200.0, 1.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-14", "isController": false}, {"data": [[200.0, 1.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-15", "isController": false}, {"data": [[400.0, 1.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-17", "isController": false}, {"data": [[400.0, 1.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-12", "isController": false}, {"data": [[400.0, 1.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-16", "isController": false}, {"data": [[200.0, 1.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-13", "isController": false}, {"data": [[200.0, 1.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-19", "isController": false}, {"data": [[200.0, 1.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-10", "isController": false}, {"data": [[200.0, 1.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-18", "isController": false}, {"data": [[200.0, 1.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-11", "isController": false}, {"data": [[900.0, 1.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-19", "isController": false}, {"data": [[1200.0, 1.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-18", "isController": false}, {"data": [[400.0, 1.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-17", "isController": false}, {"data": [[400.0, 1.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-16", "isController": false}, {"data": [[200.0, 1.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-15", "isController": false}, {"data": [[400.0, 1.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-14", "isController": false}, {"data": [[400.0, 1.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-13", "isController": false}, {"data": [[400.0, 1.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-12", "isController": false}, {"data": [[200.0, 1.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-11", "isController": false}, {"data": [[200.0, 1.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-10", "isController": false}, {"data": [[400.0, 1.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-27", "isController": false}, {"data": [[200.0, 1.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-25", "isController": false}, {"data": [[200.0, 1.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-26", "isController": false}, {"data": [[200.0, 1.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-23", "isController": false}, {"data": [[400.0, 1.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-24", "isController": false}, {"data": [[800.0, 1.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-21", "isController": false}, {"data": [[200.0, 1.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-22", "isController": false}, {"data": [[200.0, 1.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-20", "isController": false}, {"data": [[200.0, 1.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-0", "isController": false}, {"data": [[200.0, 1.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-28", "isController": false}, {"data": [[200.0, 1.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-3", "isController": false}, {"data": [[200.0, 1.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-27", "isController": false}, {"data": [[200.0, 1.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-4", "isController": false}, {"data": [[200.0, 1.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-26", "isController": false}, {"data": [[200.0, 1.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-1", "isController": false}, {"data": [[600.0, 1.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-25", "isController": false}, {"data": [[200.0, 1.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-2", "isController": false}, {"data": [[800.0, 1.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-24", "isController": false}, {"data": [[800.0, 1.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-23", "isController": false}, {"data": [[1300.0, 1.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-22", "isController": false}, {"data": [[2900.0, 1.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/", "isController": false}, {"data": [[1200.0, 1.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-21", "isController": false}, {"data": [[2400.0, 1.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history", "isController": false}, {"data": [[1500.0, 1.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-20", "isController": false}, {"data": [[400.0, 1.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-5", "isController": false}, {"data": [[400.0, 1.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-6", "isController": false}, {"data": [[400.0, 1.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-7", "isController": false}, {"data": [[200.0, 1.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-20", "isController": false}, {"data": [[200.0, 1.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-8", "isController": false}, {"data": [[200.0, 1.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-9", "isController": false}, {"data": [[200.0, 1.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-22", "isController": false}, {"data": [[200.0, 1.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-21", "isController": false}, {"data": [[400.0, 1.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-24", "isController": false}, {"data": [[200.0, 1.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-23", "isController": false}, {"data": [[200.0, 1.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-26", "isController": false}, {"data": [[400.0, 1.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-25", "isController": false}, {"data": [[500.0, 1.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-0", "isController": false}, {"data": [[400.0, 1.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-27", "isController": false}, {"data": [[600.0, 1.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-1", "isController": false}, {"data": [[400.0, 1.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-2", "isController": false}, {"data": [[200.0, 1.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-3", "isController": false}, {"data": [[400.0, 1.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-4", "isController": false}], "supportsControllersDiscrimination": true, "granularity": 100, "maxX": 3800.0, "title": "Response Time Distribution"}},
        getOptions: function() {
            var granularity = this.data.result.granularity;
            return {
                legend: {
                    noColumns: 2,
                    show: true,
                    container: '#legendResponseTimeDistribution'
                },
                xaxis:{
                    axisLabel: "Response times in ms",
                    axisLabelUseCanvas: true,
                    axisLabelFontSizePixels: 12,
                    axisLabelFontFamily: 'Verdana, Arial',
                    axisLabelPadding: 20,
                },
                yaxis: {
                    axisLabel: "Number of responses",
                    axisLabelUseCanvas: true,
                    axisLabelFontSizePixels: 12,
                    axisLabelFontFamily: 'Verdana, Arial',
                    axisLabelPadding: 20,
                },
                bars : {
                    show: true,
                    barWidth: this.data.result.granularity
                },
                grid: {
                    hoverable: true // IMPORTANT! this is needed for tooltip to
                                    // work
                },
                tooltip: true,
                tooltipOpts: {
                    content: function(label, xval, yval, flotItem){
                        return yval + " responses for " + label + " were between " + xval + " and " + (xval + granularity) + " ms";
                    }
                }
            };
        },
        createGraph: function() {
            var data = this.data;
            var options = this.getOptions();
            prepareOptions(options, data);
            $.plot($("#flotResponseTimeDistribution"), prepareData(data.result.series, $("#choicesResponseTimeDistribution")), options);
        }

};

// Response time distribution
function refreshResponseTimeDistribution() {
    var infos = responseTimeDistributionInfos;
    prepareSeries(infos.data);
    if(infos.data.result.series.length == 0) {
        setEmptyGraph("#bodyResponseTimeDistribution");
        return;
    }
    if (isGraph($("#flotResponseTimeDistribution"))){
        infos.createGraph();
    }else{
        var choiceContainer = $("#choicesResponseTimeDistribution");
        createLegend(choiceContainer, infos);
        infos.createGraph();
        $('#footerResponseTimeDistribution .legendColorBox > div').each(function(i){
            $(this).clone().prependTo(choiceContainer.find("li").eq(i));
        });
    }
};


var syntheticResponseTimeDistributionInfos = {
        data: {"result": {"minY": 6.0, "minX": 0.0, "ticks": [[0, "Requests having \nresponse time <= 500ms"], [1, "Requests having \nresponse time > 500ms and <= 1,500ms"], [2, "Requests having \nresponse time > 1,500ms"], [3, "Requests in error"]], "maxY": 78.0, "series": [{"data": [[0.0, 78.0]], "color": "#9ACD32", "isOverall": false, "label": "Requests having \nresponse time <= 500ms", "isController": false}, {"data": [[1.0, 19.0]], "color": "yellow", "isOverall": false, "label": "Requests having \nresponse time > 500ms and <= 1,500ms", "isController": false}, {"data": [[2.0, 6.0]], "color": "orange", "isOverall": false, "label": "Requests having \nresponse time > 1,500ms", "isController": false}, {"data": [], "color": "#FF6347", "isOverall": false, "label": "Requests in error", "isController": false}], "supportsControllersDiscrimination": false, "maxX": 2.0, "title": "Synthetic Response Times Distribution"}},
        getOptions: function() {
            return {
                legend: {
                    noColumns: 2,
                    show: true,
                    container: '#legendSyntheticResponseTimeDistribution'
                },
                xaxis:{
                    axisLabel: "Response times ranges",
                    axisLabelUseCanvas: true,
                    axisLabelFontSizePixels: 12,
                    axisLabelFontFamily: 'Verdana, Arial',
                    axisLabelPadding: 20,
                    tickLength:0,
                    min:-0.5,
                    max:3.5
                },
                yaxis: {
                    axisLabel: "Number of responses",
                    axisLabelUseCanvas: true,
                    axisLabelFontSizePixels: 12,
                    axisLabelFontFamily: 'Verdana, Arial',
                    axisLabelPadding: 20,
                },
                bars : {
                    show: true,
                    align: "center",
                    barWidth: 0.25,
                    fill:.75
                },
                grid: {
                    hoverable: true // IMPORTANT! this is needed for tooltip to
                                    // work
                },
                tooltip: true,
                tooltipOpts: {
                    content: function(label, xval, yval, flotItem){
                        return yval + " " + label;
                    }
                }
            };
        },
        createGraph: function() {
            var data = this.data;
            var options = this.getOptions();
            prepareOptions(options, data);
            options.xaxis.ticks = data.result.ticks;
            $.plot($("#flotSyntheticResponseTimeDistribution"), prepareData(data.result.series, $("#choicesSyntheticResponseTimeDistribution")), options);
        }

};

// Response time distribution
function refreshSyntheticResponseTimeDistribution() {
    var infos = syntheticResponseTimeDistributionInfos;
    prepareSeries(infos.data, true);
    if (isGraph($("#flotSyntheticResponseTimeDistribution"))){
        infos.createGraph();
    }else{
        var choiceContainer = $("#choicesSyntheticResponseTimeDistribution");
        createLegend(choiceContainer, infos);
        infos.createGraph();
        $('#footerSyntheticResponseTimeDistribution .legendColorBox > div').each(function(i){
            $(this).clone().prependTo(choiceContainer.find("li").eq(i));
        });
    }
};

var activeThreadsOverTimeInfos = {
        data: {"result": {"minY": 0.0, "minX": 1.68914544E12, "maxY": 1.0, "series": [{"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "ResDownload-Thread-6", "isController": false}, {"data": [[1.68914544E12, 1.0]], "isOverall": false, "label": "Thread Group", "isController": false}], "supportsControllersDiscrimination": false, "granularity": 60000, "maxX": 1.68914544E12, "title": "Active Threads Over Time"}},
        getOptions: function() {
            return {
                series: {
                    stack: true,
                    lines: {
                        show: true,
                        fill: true
                    },
                    points: {
                        show: true
                    }
                },
                xaxis: {
                    mode: "time",
                    timeformat: getTimeFormat(this.data.result.granularity),
                    axisLabel: getElapsedTimeLabel(this.data.result.granularity),
                    axisLabelUseCanvas: true,
                    axisLabelFontSizePixels: 12,
                    axisLabelFontFamily: 'Verdana, Arial',
                    axisLabelPadding: 20,
                },
                yaxis: {
                    axisLabel: "Number of active threads",
                    axisLabelUseCanvas: true,
                    axisLabelFontSizePixels: 12,
                    axisLabelFontFamily: 'Verdana, Arial',
                    axisLabelPadding: 20
                },
                legend: {
                    noColumns: 6,
                    show: true,
                    container: '#legendActiveThreadsOverTime'
                },
                grid: {
                    hoverable: true // IMPORTANT! this is needed for tooltip to
                                    // work
                },
                selection: {
                    mode: 'xy'
                },
                tooltip: true,
                tooltipOpts: {
                    content: "%s : At %x there were %y active threads"
                }
            };
        },
        createGraph: function() {
            var data = this.data;
            var dataset = prepareData(data.result.series, $("#choicesActiveThreadsOverTime"));
            var options = this.getOptions();
            prepareOptions(options, data);
            $.plot($("#flotActiveThreadsOverTime"), dataset, options);
            // setup overview
            $.plot($("#overviewActiveThreadsOverTime"), dataset, prepareOverviewOptions(options));
        }
};

// Active Threads Over Time
function refreshActiveThreadsOverTime(fixTimestamps) {
    var infos = activeThreadsOverTimeInfos;
    prepareSeries(infos.data);
    if(fixTimestamps) {
        fixTimeStamps(infos.data.result.series, 18000000);
    }
    if(isGraph($("#flotActiveThreadsOverTime"))) {
        infos.createGraph();
    }else{
        var choiceContainer = $("#choicesActiveThreadsOverTime");
        createLegend(choiceContainer, infos);
        infos.createGraph();
        setGraphZoomable("#flotActiveThreadsOverTime", "#overviewActiveThreadsOverTime");
        $('#footerActiveThreadsOverTime .legendColorBox > div').each(function(i){
            $(this).clone().prependTo(choiceContainer.find("li").eq(i));
        });
    }
};

var timeVsThreadsInfos = {
        data: {"result": {"minY": 221.0, "minX": 0.0, "maxY": 3867.0, "series": [{"data": [[1.0, 425.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-6", "isController": false}, {"data": [[1.0, 425.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-6-Aggregated", "isController": false}, {"data": [[1.0, 419.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-5", "isController": false}, {"data": [[1.0, 419.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-5-Aggregated", "isController": false}, {"data": [[1.0, 312.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/-9", "isController": false}, {"data": [[1.0, 312.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/-9-Aggregated", "isController": false}, {"data": [[1.0, 423.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-4", "isController": false}, {"data": [[1.0, 423.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-4-Aggregated", "isController": false}, {"data": [[1.0, 228.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/-8", "isController": false}, {"data": [[1.0, 228.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/-8-Aggregated", "isController": false}, {"data": [[1.0, 421.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-3", "isController": false}, {"data": [[1.0, 421.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-3-Aggregated", "isController": false}, {"data": [[1.0, 668.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/-7", "isController": false}, {"data": [[1.0, 668.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/-7-Aggregated", "isController": false}, {"data": [[1.0, 983.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/-6", "isController": false}, {"data": [[1.0, 983.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/-6-Aggregated", "isController": false}, {"data": [[1.0, 493.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-9", "isController": false}, {"data": [[1.0, 493.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-9-Aggregated", "isController": false}, {"data": [[1.0, 1715.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/-5", "isController": false}, {"data": [[1.0, 1715.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/-5-Aggregated", "isController": false}, {"data": [[1.0, 225.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-8", "isController": false}, {"data": [[1.0, 225.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-8-Aggregated", "isController": false}, {"data": [[1.0, 497.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/-4", "isController": false}, {"data": [[1.0, 497.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/-4-Aggregated", "isController": false}, {"data": [[1.0, 228.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-7", "isController": false}, {"data": [[1.0, 228.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-7-Aggregated", "isController": false}, {"data": [[1.0, 224.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-7", "isController": false}, {"data": [[1.0, 224.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-7-Aggregated", "isController": false}, {"data": [[1.0, 422.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-8", "isController": false}, {"data": [[1.0, 422.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-8-Aggregated", "isController": false}, {"data": [[1.0, 227.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-5", "isController": false}, {"data": [[1.0, 227.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-5-Aggregated", "isController": false}, {"data": [[1.0, 419.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-6", "isController": false}, {"data": [[1.0, 419.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-6-Aggregated", "isController": false}, {"data": [[1.0, 225.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-9", "isController": false}, {"data": [[1.0, 225.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-9-Aggregated", "isController": false}, {"data": [[1.0, 1342.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/-3", "isController": false}, {"data": [[1.0, 1342.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/-3-Aggregated", "isController": false}, {"data": [[1.0, 1194.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/-2", "isController": false}, {"data": [[1.0, 1194.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/-2-Aggregated", "isController": false}, {"data": [[1.0, 621.0], [0.0, 567.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/-1", "isController": false}, {"data": [[0.5, 594.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/-1-Aggregated", "isController": false}, {"data": [[1.0, 1108.0], [0.0, 874.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/-0", "isController": false}, {"data": [[0.5, 991.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/-0-Aggregated", "isController": false}, {"data": [[1.0, 224.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-2", "isController": false}, {"data": [[1.0, 224.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-2-Aggregated", "isController": false}, {"data": [[1.0, 223.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-1", "isController": false}, {"data": [[1.0, 223.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-1-Aggregated", "isController": false}, {"data": [[1.0, 665.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-0", "isController": false}, {"data": [[1.0, 665.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-0-Aggregated", "isController": false}, {"data": [[1.0, 1851.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription", "isController": false}, {"data": [[1.0, 1851.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-Aggregated", "isController": false}, {"data": [[1.0, 228.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/-10", "isController": false}, {"data": [[1.0, 228.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/-10-Aggregated", "isController": false}, {"data": [[1.0, 230.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/-11", "isController": false}, {"data": [[1.0, 230.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/-11-Aggregated", "isController": false}, {"data": [[1.0, 3867.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login", "isController": false}, {"data": [[1.0, 3867.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-Aggregated", "isController": false}, {"data": [[1.0, 424.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-11", "isController": false}, {"data": [[1.0, 424.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-11-Aggregated", "isController": false}, {"data": [[1.0, 224.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-18", "isController": false}, {"data": [[1.0, 224.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-18-Aggregated", "isController": false}, {"data": [[1.0, 224.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-10", "isController": false}, {"data": [[1.0, 224.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-10-Aggregated", "isController": false}, {"data": [[1.0, 268.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-19", "isController": false}, {"data": [[1.0, 268.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-19-Aggregated", "isController": false}, {"data": [[1.0, 231.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-13", "isController": false}, {"data": [[1.0, 231.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-13-Aggregated", "isController": false}, {"data": [[1.0, 421.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-16", "isController": false}, {"data": [[1.0, 421.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-16-Aggregated", "isController": false}, {"data": [[1.0, 420.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-12", "isController": false}, {"data": [[1.0, 420.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-12-Aggregated", "isController": false}, {"data": [[1.0, 420.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-17", "isController": false}, {"data": [[1.0, 420.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-17-Aggregated", "isController": false}, {"data": [[1.0, 225.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-15", "isController": false}, {"data": [[1.0, 225.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-15-Aggregated", "isController": false}, {"data": [[1.0, 422.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-14", "isController": false}, {"data": [[1.0, 422.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-14-Aggregated", "isController": false}, {"data": [[1.0, 227.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-14", "isController": false}, {"data": [[1.0, 227.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-14-Aggregated", "isController": false}, {"data": [[1.0, 227.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-15", "isController": false}, {"data": [[1.0, 227.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-15-Aggregated", "isController": false}, {"data": [[1.0, 424.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-17", "isController": false}, {"data": [[1.0, 424.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-17-Aggregated", "isController": false}, {"data": [[1.0, 420.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-12", "isController": false}, {"data": [[1.0, 420.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-12-Aggregated", "isController": false}, {"data": [[1.0, 426.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-16", "isController": false}, {"data": [[1.0, 426.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-16-Aggregated", "isController": false}, {"data": [[1.0, 223.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-13", "isController": false}, {"data": [[1.0, 223.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-13-Aggregated", "isController": false}, {"data": [[1.0, 272.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-19", "isController": false}, {"data": [[1.0, 272.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-19-Aggregated", "isController": false}, {"data": [[1.0, 238.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-10", "isController": false}, {"data": [[1.0, 238.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-10-Aggregated", "isController": false}, {"data": [[1.0, 226.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-18", "isController": false}, {"data": [[1.0, 226.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-18-Aggregated", "isController": false}, {"data": [[1.0, 235.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-11", "isController": false}, {"data": [[1.0, 235.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-11-Aggregated", "isController": false}, {"data": [[1.0, 932.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-19", "isController": false}, {"data": [[1.0, 932.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-19-Aggregated", "isController": false}, {"data": [[1.0, 1231.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-18", "isController": false}, {"data": [[1.0, 1231.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-18-Aggregated", "isController": false}, {"data": [[1.0, 424.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-17", "isController": false}, {"data": [[1.0, 424.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-17-Aggregated", "isController": false}, {"data": [[1.0, 425.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-16", "isController": false}, {"data": [[1.0, 425.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-16-Aggregated", "isController": false}, {"data": [[1.0, 227.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-15", "isController": false}, {"data": [[1.0, 227.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-15-Aggregated", "isController": false}, {"data": [[1.0, 423.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-14", "isController": false}, {"data": [[1.0, 423.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-14-Aggregated", "isController": false}, {"data": [[1.0, 422.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-13", "isController": false}, {"data": [[1.0, 422.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-13-Aggregated", "isController": false}, {"data": [[1.0, 422.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-12", "isController": false}, {"data": [[1.0, 422.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-12-Aggregated", "isController": false}, {"data": [[1.0, 223.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-11", "isController": false}, {"data": [[1.0, 223.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-11-Aggregated", "isController": false}, {"data": [[1.0, 226.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-10", "isController": false}, {"data": [[1.0, 226.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-10-Aggregated", "isController": false}, {"data": [[1.0, 427.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-27", "isController": false}, {"data": [[1.0, 427.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-27-Aggregated", "isController": false}, {"data": [[1.0, 228.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-25", "isController": false}, {"data": [[1.0, 228.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-25-Aggregated", "isController": false}, {"data": [[1.0, 231.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-26", "isController": false}, {"data": [[1.0, 231.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-26-Aggregated", "isController": false}, {"data": [[1.0, 231.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-23", "isController": false}, {"data": [[1.0, 231.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-23-Aggregated", "isController": false}, {"data": [[1.0, 426.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-24", "isController": false}, {"data": [[1.0, 426.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-24-Aggregated", "isController": false}, {"data": [[1.0, 847.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-21", "isController": false}, {"data": [[1.0, 847.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-21-Aggregated", "isController": false}, {"data": [[1.0, 232.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-22", "isController": false}, {"data": [[1.0, 232.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-22-Aggregated", "isController": false}, {"data": [[1.0, 276.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-20", "isController": false}, {"data": [[1.0, 276.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-20-Aggregated", "isController": false}, {"data": [[1.0, 263.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-0", "isController": false}, {"data": [[1.0, 263.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-0-Aggregated", "isController": false}, {"data": [[1.0, 231.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-28", "isController": false}, {"data": [[1.0, 231.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-28-Aggregated", "isController": false}, {"data": [[1.0, 229.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-3", "isController": false}, {"data": [[1.0, 229.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-3-Aggregated", "isController": false}, {"data": [[1.0, 228.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-27", "isController": false}, {"data": [[1.0, 228.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-27-Aggregated", "isController": false}, {"data": [[1.0, 227.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-4", "isController": false}, {"data": [[1.0, 227.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-4-Aggregated", "isController": false}, {"data": [[1.0, 226.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-26", "isController": false}, {"data": [[1.0, 226.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-26-Aggregated", "isController": false}, {"data": [[1.0, 224.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-1", "isController": false}, {"data": [[1.0, 224.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-1-Aggregated", "isController": false}, {"data": [[1.0, 682.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-25", "isController": false}, {"data": [[1.0, 682.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-25-Aggregated", "isController": false}, {"data": [[1.0, 225.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-2", "isController": false}, {"data": [[1.0, 225.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-2-Aggregated", "isController": false}, {"data": [[1.0, 821.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-24", "isController": false}, {"data": [[1.0, 821.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-24-Aggregated", "isController": false}, {"data": [[1.0, 822.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-23", "isController": false}, {"data": [[1.0, 822.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-23-Aggregated", "isController": false}, {"data": [[1.0, 1373.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-22", "isController": false}, {"data": [[1.0, 1373.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-22-Aggregated", "isController": false}, {"data": [[1.0, 2915.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/", "isController": false}, {"data": [[1.0, 2915.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/-Aggregated", "isController": false}, {"data": [[1.0, 1268.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-21", "isController": false}, {"data": [[1.0, 1268.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-21-Aggregated", "isController": false}, {"data": [[1.0, 2443.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history", "isController": false}, {"data": [[1.0, 2443.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-Aggregated", "isController": false}, {"data": [[1.0, 1512.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-20", "isController": false}, {"data": [[1.0, 1512.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-20-Aggregated", "isController": false}, {"data": [[1.0, 423.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-5", "isController": false}, {"data": [[1.0, 423.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-5-Aggregated", "isController": false}, {"data": [[1.0, 440.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-6", "isController": false}, {"data": [[1.0, 440.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-6-Aggregated", "isController": false}, {"data": [[1.0, 436.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-7", "isController": false}, {"data": [[1.0, 436.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-7-Aggregated", "isController": false}, {"data": [[1.0, 258.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-20", "isController": false}, {"data": [[1.0, 258.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-20-Aggregated", "isController": false}, {"data": [[1.0, 226.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-8", "isController": false}, {"data": [[1.0, 226.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-8-Aggregated", "isController": false}, {"data": [[1.0, 226.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-9", "isController": false}, {"data": [[1.0, 226.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-9-Aggregated", "isController": false}, {"data": [[1.0, 232.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-22", "isController": false}, {"data": [[1.0, 232.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-22-Aggregated", "isController": false}, {"data": [[1.0, 269.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-21", "isController": false}, {"data": [[1.0, 269.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-21-Aggregated", "isController": false}, {"data": [[1.0, 424.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-24", "isController": false}, {"data": [[1.0, 424.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-24-Aggregated", "isController": false}, {"data": [[1.0, 221.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-23", "isController": false}, {"data": [[1.0, 221.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-23-Aggregated", "isController": false}, {"data": [[1.0, 227.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-26", "isController": false}, {"data": [[1.0, 227.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-26-Aggregated", "isController": false}, {"data": [[1.0, 431.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-25", "isController": false}, {"data": [[1.0, 431.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-25-Aggregated", "isController": false}, {"data": [[1.0, 523.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-0", "isController": false}, {"data": [[1.0, 523.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-0-Aggregated", "isController": false}, {"data": [[1.0, 433.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-27", "isController": false}, {"data": [[1.0, 433.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-27-Aggregated", "isController": false}, {"data": [[1.0, 641.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-1", "isController": false}, {"data": [[1.0, 641.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-1-Aggregated", "isController": false}, {"data": [[1.0, 424.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-2", "isController": false}, {"data": [[1.0, 424.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-2-Aggregated", "isController": false}, {"data": [[1.0, 225.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-3", "isController": false}, {"data": [[1.0, 225.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-3-Aggregated", "isController": false}, {"data": [[1.0, 424.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-4", "isController": false}, {"data": [[1.0, 424.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-4-Aggregated", "isController": false}], "supportsControllersDiscrimination": true, "maxX": 1.0, "title": "Time VS Threads"}},
        getOptions: function() {
            return {
                series: {
                    lines: {
                        show: true
                    },
                    points: {
                        show: true
                    }
                },
                xaxis: {
                    axisLabel: "Number of active threads",
                    axisLabelUseCanvas: true,
                    axisLabelFontSizePixels: 12,
                    axisLabelFontFamily: 'Verdana, Arial',
                    axisLabelPadding: 20,
                },
                yaxis: {
                    axisLabel: "Average response times in ms",
                    axisLabelUseCanvas: true,
                    axisLabelFontSizePixels: 12,
                    axisLabelFontFamily: 'Verdana, Arial',
                    axisLabelPadding: 20
                },
                legend: { noColumns: 2,show: true, container: '#legendTimeVsThreads' },
                selection: {
                    mode: 'xy'
                },
                grid: {
                    hoverable: true // IMPORTANT! this is needed for tooltip to work
                },
                tooltip: true,
                tooltipOpts: {
                    content: "%s: At %x.2 active threads, Average response time was %y.2 ms"
                }
            };
        },
        createGraph: function() {
            var data = this.data;
            var dataset = prepareData(data.result.series, $("#choicesTimeVsThreads"));
            var options = this.getOptions();
            prepareOptions(options, data);
            $.plot($("#flotTimesVsThreads"), dataset, options);
            // setup overview
            $.plot($("#overviewTimesVsThreads"), dataset, prepareOverviewOptions(options));
        }
};

// Time vs threads
function refreshTimeVsThreads(){
    var infos = timeVsThreadsInfos;
    prepareSeries(infos.data);
    if(infos.data.result.series.length == 0) {
        setEmptyGraph("#bodyTimeVsThreads");
        return;
    }
    if(isGraph($("#flotTimesVsThreads"))){
        infos.createGraph();
    }else{
        var choiceContainer = $("#choicesTimeVsThreads");
        createLegend(choiceContainer, infos);
        infos.createGraph();
        setGraphZoomable("#flotTimesVsThreads", "#overviewTimesVsThreads");
        $('#footerTimeVsThreads .legendColorBox > div').each(function(i){
            $(this).clone().prependTo(choiceContainer.find("li").eq(i));
        });
    }
};

var bytesThroughputOverTimeInfos = {
        data : {"result": {"minY": 4133.65, "minX": 1.68914544E12, "maxY": 66389.48333333334, "series": [{"data": [[1.68914544E12, 66389.48333333334]], "isOverall": false, "label": "Bytes received per second", "isController": false}, {"data": [[1.68914544E12, 4133.65]], "isOverall": false, "label": "Bytes sent per second", "isController": false}], "supportsControllersDiscrimination": false, "granularity": 60000, "maxX": 1.68914544E12, "title": "Bytes Throughput Over Time"}},
        getOptions : function(){
            return {
                series: {
                    lines: {
                        show: true
                    },
                    points: {
                        show: true
                    }
                },
                xaxis: {
                    mode: "time",
                    timeformat: getTimeFormat(this.data.result.granularity),
                    axisLabel: getElapsedTimeLabel(this.data.result.granularity) ,
                    axisLabelUseCanvas: true,
                    axisLabelFontSizePixels: 12,
                    axisLabelFontFamily: 'Verdana, Arial',
                    axisLabelPadding: 20,
                },
                yaxis: {
                    axisLabel: "Bytes / sec",
                    axisLabelUseCanvas: true,
                    axisLabelFontSizePixels: 12,
                    axisLabelFontFamily: 'Verdana, Arial',
                    axisLabelPadding: 20,
                },
                legend: {
                    noColumns: 2,
                    show: true,
                    container: '#legendBytesThroughputOverTime'
                },
                selection: {
                    mode: "xy"
                },
                grid: {
                    hoverable: true // IMPORTANT! this is needed for tooltip to
                                    // work
                },
                tooltip: true,
                tooltipOpts: {
                    content: "%s at %x was %y"
                }
            };
        },
        createGraph : function() {
            var data = this.data;
            var dataset = prepareData(data.result.series, $("#choicesBytesThroughputOverTime"));
            var options = this.getOptions();
            prepareOptions(options, data);
            $.plot($("#flotBytesThroughputOverTime"), dataset, options);
            // setup overview
            $.plot($("#overviewBytesThroughputOverTime"), dataset, prepareOverviewOptions(options));
        }
};

// Bytes throughput Over Time
function refreshBytesThroughputOverTime(fixTimestamps) {
    var infos = bytesThroughputOverTimeInfos;
    prepareSeries(infos.data);
    if(fixTimestamps) {
        fixTimeStamps(infos.data.result.series, 18000000);
    }
    if(isGraph($("#flotBytesThroughputOverTime"))){
        infos.createGraph();
    }else{
        var choiceContainer = $("#choicesBytesThroughputOverTime");
        createLegend(choiceContainer, infos);
        infos.createGraph();
        setGraphZoomable("#flotBytesThroughputOverTime", "#overviewBytesThroughputOverTime");
        $('#footerBytesThroughputOverTime .legendColorBox > div').each(function(i){
            $(this).clone().prependTo(choiceContainer.find("li").eq(i));
        });
    }
}

var responseTimesOverTimeInfos = {
        data: {"result": {"minY": 221.0, "minX": 1.68914544E12, "maxY": 3867.0, "series": [{"data": [[1.68914544E12, 425.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-6", "isController": false}, {"data": [[1.68914544E12, 419.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-5", "isController": false}, {"data": [[1.68914544E12, 312.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/-9", "isController": false}, {"data": [[1.68914544E12, 423.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-4", "isController": false}, {"data": [[1.68914544E12, 228.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/-8", "isController": false}, {"data": [[1.68914544E12, 421.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-3", "isController": false}, {"data": [[1.68914544E12, 668.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/-7", "isController": false}, {"data": [[1.68914544E12, 983.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/-6", "isController": false}, {"data": [[1.68914544E12, 493.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-9", "isController": false}, {"data": [[1.68914544E12, 1715.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/-5", "isController": false}, {"data": [[1.68914544E12, 225.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-8", "isController": false}, {"data": [[1.68914544E12, 497.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/-4", "isController": false}, {"data": [[1.68914544E12, 228.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-7", "isController": false}, {"data": [[1.68914544E12, 224.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-7", "isController": false}, {"data": [[1.68914544E12, 422.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-8", "isController": false}, {"data": [[1.68914544E12, 227.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-5", "isController": false}, {"data": [[1.68914544E12, 419.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-6", "isController": false}, {"data": [[1.68914544E12, 225.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-9", "isController": false}, {"data": [[1.68914544E12, 1342.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/-3", "isController": false}, {"data": [[1.68914544E12, 1194.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/-2", "isController": false}, {"data": [[1.68914544E12, 594.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/-1", "isController": false}, {"data": [[1.68914544E12, 991.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/-0", "isController": false}, {"data": [[1.68914544E12, 224.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-2", "isController": false}, {"data": [[1.68914544E12, 223.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-1", "isController": false}, {"data": [[1.68914544E12, 665.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-0", "isController": false}, {"data": [[1.68914544E12, 1851.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription", "isController": false}, {"data": [[1.68914544E12, 228.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/-10", "isController": false}, {"data": [[1.68914544E12, 230.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/-11", "isController": false}, {"data": [[1.68914544E12, 3867.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login", "isController": false}, {"data": [[1.68914544E12, 424.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-11", "isController": false}, {"data": [[1.68914544E12, 224.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-18", "isController": false}, {"data": [[1.68914544E12, 224.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-10", "isController": false}, {"data": [[1.68914544E12, 268.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-19", "isController": false}, {"data": [[1.68914544E12, 231.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-13", "isController": false}, {"data": [[1.68914544E12, 421.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-16", "isController": false}, {"data": [[1.68914544E12, 420.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-12", "isController": false}, {"data": [[1.68914544E12, 420.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-17", "isController": false}, {"data": [[1.68914544E12, 225.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-15", "isController": false}, {"data": [[1.68914544E12, 422.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-14", "isController": false}, {"data": [[1.68914544E12, 227.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-14", "isController": false}, {"data": [[1.68914544E12, 227.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-15", "isController": false}, {"data": [[1.68914544E12, 424.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-17", "isController": false}, {"data": [[1.68914544E12, 420.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-12", "isController": false}, {"data": [[1.68914544E12, 426.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-16", "isController": false}, {"data": [[1.68914544E12, 223.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-13", "isController": false}, {"data": [[1.68914544E12, 272.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-19", "isController": false}, {"data": [[1.68914544E12, 238.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-10", "isController": false}, {"data": [[1.68914544E12, 226.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-18", "isController": false}, {"data": [[1.68914544E12, 235.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-11", "isController": false}, {"data": [[1.68914544E12, 932.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-19", "isController": false}, {"data": [[1.68914544E12, 1231.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-18", "isController": false}, {"data": [[1.68914544E12, 424.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-17", "isController": false}, {"data": [[1.68914544E12, 425.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-16", "isController": false}, {"data": [[1.68914544E12, 227.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-15", "isController": false}, {"data": [[1.68914544E12, 423.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-14", "isController": false}, {"data": [[1.68914544E12, 422.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-13", "isController": false}, {"data": [[1.68914544E12, 422.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-12", "isController": false}, {"data": [[1.68914544E12, 223.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-11", "isController": false}, {"data": [[1.68914544E12, 226.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-10", "isController": false}, {"data": [[1.68914544E12, 427.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-27", "isController": false}, {"data": [[1.68914544E12, 228.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-25", "isController": false}, {"data": [[1.68914544E12, 231.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-26", "isController": false}, {"data": [[1.68914544E12, 231.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-23", "isController": false}, {"data": [[1.68914544E12, 426.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-24", "isController": false}, {"data": [[1.68914544E12, 847.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-21", "isController": false}, {"data": [[1.68914544E12, 232.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-22", "isController": false}, {"data": [[1.68914544E12, 276.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-20", "isController": false}, {"data": [[1.68914544E12, 263.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-0", "isController": false}, {"data": [[1.68914544E12, 231.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-28", "isController": false}, {"data": [[1.68914544E12, 229.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-3", "isController": false}, {"data": [[1.68914544E12, 228.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-27", "isController": false}, {"data": [[1.68914544E12, 227.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-4", "isController": false}, {"data": [[1.68914544E12, 226.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-26", "isController": false}, {"data": [[1.68914544E12, 224.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-1", "isController": false}, {"data": [[1.68914544E12, 682.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-25", "isController": false}, {"data": [[1.68914544E12, 225.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-2", "isController": false}, {"data": [[1.68914544E12, 821.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-24", "isController": false}, {"data": [[1.68914544E12, 822.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-23", "isController": false}, {"data": [[1.68914544E12, 1373.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-22", "isController": false}, {"data": [[1.68914544E12, 2915.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/", "isController": false}, {"data": [[1.68914544E12, 1268.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-21", "isController": false}, {"data": [[1.68914544E12, 2443.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history", "isController": false}, {"data": [[1.68914544E12, 1512.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-20", "isController": false}, {"data": [[1.68914544E12, 423.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-5", "isController": false}, {"data": [[1.68914544E12, 440.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-6", "isController": false}, {"data": [[1.68914544E12, 436.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-7", "isController": false}, {"data": [[1.68914544E12, 258.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-20", "isController": false}, {"data": [[1.68914544E12, 226.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-8", "isController": false}, {"data": [[1.68914544E12, 226.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-9", "isController": false}, {"data": [[1.68914544E12, 232.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-22", "isController": false}, {"data": [[1.68914544E12, 269.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-21", "isController": false}, {"data": [[1.68914544E12, 424.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-24", "isController": false}, {"data": [[1.68914544E12, 221.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-23", "isController": false}, {"data": [[1.68914544E12, 227.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-26", "isController": false}, {"data": [[1.68914544E12, 431.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-25", "isController": false}, {"data": [[1.68914544E12, 523.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-0", "isController": false}, {"data": [[1.68914544E12, 433.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-27", "isController": false}, {"data": [[1.68914544E12, 641.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-1", "isController": false}, {"data": [[1.68914544E12, 424.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-2", "isController": false}, {"data": [[1.68914544E12, 225.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-3", "isController": false}, {"data": [[1.68914544E12, 424.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-4", "isController": false}], "supportsControllersDiscrimination": true, "granularity": 60000, "maxX": 1.68914544E12, "title": "Response Time Over Time"}},
        getOptions: function(){
            return {
                series: {
                    lines: {
                        show: true
                    },
                    points: {
                        show: true
                    }
                },
                xaxis: {
                    mode: "time",
                    timeformat: getTimeFormat(this.data.result.granularity),
                    axisLabel: getElapsedTimeLabel(this.data.result.granularity),
                    axisLabelUseCanvas: true,
                    axisLabelFontSizePixels: 12,
                    axisLabelFontFamily: 'Verdana, Arial',
                    axisLabelPadding: 20,
                },
                yaxis: {
                    axisLabel: "Average response time in ms",
                    axisLabelUseCanvas: true,
                    axisLabelFontSizePixels: 12,
                    axisLabelFontFamily: 'Verdana, Arial',
                    axisLabelPadding: 20,
                },
                legend: {
                    noColumns: 2,
                    show: true,
                    container: '#legendResponseTimesOverTime'
                },
                selection: {
                    mode: 'xy'
                },
                grid: {
                    hoverable: true // IMPORTANT! this is needed for tooltip to
                                    // work
                },
                tooltip: true,
                tooltipOpts: {
                    content: "%s : at %x Average response time was %y ms"
                }
            };
        },
        createGraph: function() {
            var data = this.data;
            var dataset = prepareData(data.result.series, $("#choicesResponseTimesOverTime"));
            var options = this.getOptions();
            prepareOptions(options, data);
            $.plot($("#flotResponseTimesOverTime"), dataset, options);
            // setup overview
            $.plot($("#overviewResponseTimesOverTime"), dataset, prepareOverviewOptions(options));
        }
};

// Response Times Over Time
function refreshResponseTimeOverTime(fixTimestamps) {
    var infos = responseTimesOverTimeInfos;
    prepareSeries(infos.data);
    if(infos.data.result.series.length == 0) {
        setEmptyGraph("#bodyResponseTimeOverTime");
        return;
    }
    if(fixTimestamps) {
        fixTimeStamps(infos.data.result.series, 18000000);
    }
    if(isGraph($("#flotResponseTimesOverTime"))){
        infos.createGraph();
    }else{
        var choiceContainer = $("#choicesResponseTimesOverTime");
        createLegend(choiceContainer, infos);
        infos.createGraph();
        setGraphZoomable("#flotResponseTimesOverTime", "#overviewResponseTimesOverTime");
        $('#footerResponseTimesOverTime .legendColorBox > div').each(function(i){
            $(this).clone().prependTo(choiceContainer.find("li").eq(i));
        });
    }
};

var latenciesOverTimeInfos = {
        data: {"result": {"minY": 0.0, "minX": 1.68914544E12, "maxY": 1373.0, "series": [{"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-6", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-5", "isController": false}, {"data": [[1.68914544E12, 312.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/-9", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-4", "isController": false}, {"data": [[1.68914544E12, 228.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/-8", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-3", "isController": false}, {"data": [[1.68914544E12, 227.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/-7", "isController": false}, {"data": [[1.68914544E12, 503.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/-6", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-9", "isController": false}, {"data": [[1.68914544E12, 288.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/-5", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-8", "isController": false}, {"data": [[1.68914544E12, 497.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/-4", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-7", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-7", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-8", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-5", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-6", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-9", "isController": false}, {"data": [[1.68914544E12, 497.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/-3", "isController": false}, {"data": [[1.68914544E12, 512.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/-2", "isController": false}, {"data": [[1.68914544E12, 495.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/-1", "isController": false}, {"data": [[1.68914544E12, 651.5]], "isOverall": false, "label": "https://vinfax-api.designitic.com/-0", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-2", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-1", "isController": false}, {"data": [[1.68914544E12, 248.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-0", "isController": false}, {"data": [[1.68914544E12, 253.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription", "isController": false}, {"data": [[1.68914544E12, 228.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/-10", "isController": false}, {"data": [[1.68914544E12, 229.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/-11", "isController": false}, {"data": [[1.68914544E12, 523.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-11", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-18", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-10", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-19", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-13", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-16", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-12", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-17", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-15", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-14", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-14", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-15", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-17", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-12", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-16", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-13", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-19", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-10", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-18", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-11", "isController": false}, {"data": [[1.68914544E12, 232.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-19", "isController": false}, {"data": [[1.68914544E12, 234.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-18", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-17", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-16", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-15", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-14", "isController": false}, {"data": [[1.68914544E12, 422.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-13", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-12", "isController": false}, {"data": [[1.68914544E12, 223.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-11", "isController": false}, {"data": [[1.68914544E12, 226.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-10", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-27", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-25", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-26", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-23", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-24", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-21", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-22", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-20", "isController": false}, {"data": [[1.68914544E12, 253.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-0", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-28", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-3", "isController": false}, {"data": [[1.68914544E12, 227.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-27", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-4", "isController": false}, {"data": [[1.68914544E12, 226.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-26", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-1", "isController": false}, {"data": [[1.68914544E12, 228.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-25", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-2", "isController": false}, {"data": [[1.68914544E12, 229.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-24", "isController": false}, {"data": [[1.68914544E12, 231.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-23", "isController": false}, {"data": [[1.68914544E12, 1373.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-22", "isController": false}, {"data": [[1.68914544E12, 1015.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/", "isController": false}, {"data": [[1.68914544E12, 1268.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-21", "isController": false}, {"data": [[1.68914544E12, 248.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history", "isController": false}, {"data": [[1.68914544E12, 1255.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-20", "isController": false}, {"data": [[1.68914544E12, 423.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-5", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-6", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-7", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-20", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-8", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-9", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-22", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-21", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-24", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-23", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-26", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-25", "isController": false}, {"data": [[1.68914544E12, 523.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-0", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-27", "isController": false}, {"data": [[1.68914544E12, 445.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-1", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-2", "isController": false}, {"data": [[1.68914544E12, 225.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-3", "isController": false}, {"data": [[1.68914544E12, 424.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-4", "isController": false}], "supportsControllersDiscrimination": true, "granularity": 60000, "maxX": 1.68914544E12, "title": "Latencies Over Time"}},
        getOptions: function() {
            return {
                series: {
                    lines: {
                        show: true
                    },
                    points: {
                        show: true
                    }
                },
                xaxis: {
                    mode: "time",
                    timeformat: getTimeFormat(this.data.result.granularity),
                    axisLabel: getElapsedTimeLabel(this.data.result.granularity),
                    axisLabelUseCanvas: true,
                    axisLabelFontSizePixels: 12,
                    axisLabelFontFamily: 'Verdana, Arial',
                    axisLabelPadding: 20,
                },
                yaxis: {
                    axisLabel: "Average response latencies in ms",
                    axisLabelUseCanvas: true,
                    axisLabelFontSizePixels: 12,
                    axisLabelFontFamily: 'Verdana, Arial',
                    axisLabelPadding: 20,
                },
                legend: {
                    noColumns: 2,
                    show: true,
                    container: '#legendLatenciesOverTime'
                },
                selection: {
                    mode: 'xy'
                },
                grid: {
                    hoverable: true // IMPORTANT! this is needed for tooltip to
                                    // work
                },
                tooltip: true,
                tooltipOpts: {
                    content: "%s : at %x Average latency was %y ms"
                }
            };
        },
        createGraph: function () {
            var data = this.data;
            var dataset = prepareData(data.result.series, $("#choicesLatenciesOverTime"));
            var options = this.getOptions();
            prepareOptions(options, data);
            $.plot($("#flotLatenciesOverTime"), dataset, options);
            // setup overview
            $.plot($("#overviewLatenciesOverTime"), dataset, prepareOverviewOptions(options));
        }
};

// Latencies Over Time
function refreshLatenciesOverTime(fixTimestamps) {
    var infos = latenciesOverTimeInfos;
    prepareSeries(infos.data);
    if(infos.data.result.series.length == 0) {
        setEmptyGraph("#bodyLatenciesOverTime");
        return;
    }
    if(fixTimestamps) {
        fixTimeStamps(infos.data.result.series, 18000000);
    }
    if(isGraph($("#flotLatenciesOverTime"))) {
        infos.createGraph();
    }else {
        var choiceContainer = $("#choicesLatenciesOverTime");
        createLegend(choiceContainer, infos);
        infos.createGraph();
        setGraphZoomable("#flotLatenciesOverTime", "#overviewLatenciesOverTime");
        $('#footerLatenciesOverTime .legendColorBox > div').each(function(i){
            $(this).clone().prependTo(choiceContainer.find("li").eq(i));
        });
    }
};

var connectTimeOverTimeInfos = {
        data: {"result": {"minY": 0.0, "minX": 1.68914544E12, "maxY": 998.0, "series": [{"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-6", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-5", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/-9", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-4", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/-8", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-3", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/-7", "isController": false}, {"data": [[1.68914544E12, 81.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/-6", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-9", "isController": false}, {"data": [[1.68914544E12, 57.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/-5", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-8", "isController": false}, {"data": [[1.68914544E12, 75.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/-4", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-7", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-7", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-8", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-5", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-6", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-9", "isController": false}, {"data": [[1.68914544E12, 76.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/-3", "isController": false}, {"data": [[1.68914544E12, 85.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/-2", "isController": false}, {"data": [[1.68914544E12, 208.5]], "isOverall": false, "label": "https://vinfax-api.designitic.com/-1", "isController": false}, {"data": [[1.68914544E12, 294.5]], "isOverall": false, "label": "https://vinfax-api.designitic.com/-0", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-2", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-1", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-0", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/-10", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/-11", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-11", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-18", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-10", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-19", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-13", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-16", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-12", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-17", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-15", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-14", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-14", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-15", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-17", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-12", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-16", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-13", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-19", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-10", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-18", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-11", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-19", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-18", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-17", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-16", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-15", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-14", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-13", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-12", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-11", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-10", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-27", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-25", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-26", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-23", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-24", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-21", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-22", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-20", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-0", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-28", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-3", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-27", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-4", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-26", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-1", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-25", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-2", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-24", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-23", "isController": false}, {"data": [[1.68914544E12, 828.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-22", "isController": false}, {"data": [[1.68914544E12, 532.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/", "isController": false}, {"data": [[1.68914544E12, 998.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-21", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history", "isController": false}, {"data": [[1.68914544E12, 993.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-20", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-5", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-6", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-7", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-20", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-8", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-9", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-22", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-21", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-24", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-23", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-26", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-25", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-0", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-27", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-1", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-2", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-3", "isController": false}, {"data": [[1.68914544E12, 0.0]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-4", "isController": false}], "supportsControllersDiscrimination": true, "granularity": 60000, "maxX": 1.68914544E12, "title": "Connect Time Over Time"}},
        getOptions: function() {
            return {
                series: {
                    lines: {
                        show: true
                    },
                    points: {
                        show: true
                    }
                },
                xaxis: {
                    mode: "time",
                    timeformat: getTimeFormat(this.data.result.granularity),
                    axisLabel: getConnectTimeLabel(this.data.result.granularity),
                    axisLabelUseCanvas: true,
                    axisLabelFontSizePixels: 12,
                    axisLabelFontFamily: 'Verdana, Arial',
                    axisLabelPadding: 20,
                },
                yaxis: {
                    axisLabel: "Average Connect Time in ms",
                    axisLabelUseCanvas: true,
                    axisLabelFontSizePixels: 12,
                    axisLabelFontFamily: 'Verdana, Arial',
                    axisLabelPadding: 20,
                },
                legend: {
                    noColumns: 2,
                    show: true,
                    container: '#legendConnectTimeOverTime'
                },
                selection: {
                    mode: 'xy'
                },
                grid: {
                    hoverable: true // IMPORTANT! this is needed for tooltip to
                                    // work
                },
                tooltip: true,
                tooltipOpts: {
                    content: "%s : at %x Average connect time was %y ms"
                }
            };
        },
        createGraph: function () {
            var data = this.data;
            var dataset = prepareData(data.result.series, $("#choicesConnectTimeOverTime"));
            var options = this.getOptions();
            prepareOptions(options, data);
            $.plot($("#flotConnectTimeOverTime"), dataset, options);
            // setup overview
            $.plot($("#overviewConnectTimeOverTime"), dataset, prepareOverviewOptions(options));
        }
};

// Connect Time Over Time
function refreshConnectTimeOverTime(fixTimestamps) {
    var infos = connectTimeOverTimeInfos;
    prepareSeries(infos.data);
    if(infos.data.result.series.length == 0) {
        setEmptyGraph("#bodyConnectTimeOverTime");
        return;
    }
    if(fixTimestamps) {
        fixTimeStamps(infos.data.result.series, 18000000);
    }
    if(isGraph($("#flotConnectTimeOverTime"))) {
        infos.createGraph();
    }else {
        var choiceContainer = $("#choicesConnectTimeOverTime");
        createLegend(choiceContainer, infos);
        infos.createGraph();
        setGraphZoomable("#flotConnectTimeOverTime", "#overviewConnectTimeOverTime");
        $('#footerConnectTimeOverTime .legendColorBox > div').each(function(i){
            $(this).clone().prependTo(choiceContainer.find("li").eq(i));
        });
    }
};

var responseTimePercentilesOverTimeInfos = {
        data: {"result": {"minY": 221.0, "minX": 1.68914544E12, "maxY": 3867.0, "series": [{"data": [[1.68914544E12, 3867.0]], "isOverall": false, "label": "Max", "isController": false}, {"data": [[1.68914544E12, 221.0]], "isOverall": false, "label": "Min", "isController": false}, {"data": [[1.68914544E12, 1216.2000000000003]], "isOverall": false, "label": "90th percentile", "isController": false}, {"data": [[1.68914544E12, 3828.919999999994]], "isOverall": false, "label": "99th percentile", "isController": false}, {"data": [[1.68914544E12, 420.0]], "isOverall": false, "label": "Median", "isController": false}, {"data": [[1.68914544E12, 1674.3999999999994]], "isOverall": false, "label": "95th percentile", "isController": false}], "supportsControllersDiscrimination": false, "granularity": 60000, "maxX": 1.68914544E12, "title": "Response Time Percentiles Over Time (successful requests only)"}},
        getOptions: function() {
            return {
                series: {
                    lines: {
                        show: true,
                        fill: true
                    },
                    points: {
                        show: true
                    }
                },
                xaxis: {
                    mode: "time",
                    timeformat: getTimeFormat(this.data.result.granularity),
                    axisLabel: getElapsedTimeLabel(this.data.result.granularity),
                    axisLabelUseCanvas: true,
                    axisLabelFontSizePixels: 12,
                    axisLabelFontFamily: 'Verdana, Arial',
                    axisLabelPadding: 20,
                },
                yaxis: {
                    axisLabel: "Response Time in ms",
                    axisLabelUseCanvas: true,
                    axisLabelFontSizePixels: 12,
                    axisLabelFontFamily: 'Verdana, Arial',
                    axisLabelPadding: 20,
                },
                legend: {
                    noColumns: 2,
                    show: true,
                    container: '#legendResponseTimePercentilesOverTime'
                },
                selection: {
                    mode: 'xy'
                },
                grid: {
                    hoverable: true // IMPORTANT! this is needed for tooltip to
                                    // work
                },
                tooltip: true,
                tooltipOpts: {
                    content: "%s : at %x Response time was %y ms"
                }
            };
        },
        createGraph: function () {
            var data = this.data;
            var dataset = prepareData(data.result.series, $("#choicesResponseTimePercentilesOverTime"));
            var options = this.getOptions();
            prepareOptions(options, data);
            $.plot($("#flotResponseTimePercentilesOverTime"), dataset, options);
            // setup overview
            $.plot($("#overviewResponseTimePercentilesOverTime"), dataset, prepareOverviewOptions(options));
        }
};

// Response Time Percentiles Over Time
function refreshResponseTimePercentilesOverTime(fixTimestamps) {
    var infos = responseTimePercentilesOverTimeInfos;
    prepareSeries(infos.data);
    if(fixTimestamps) {
        fixTimeStamps(infos.data.result.series, 18000000);
    }
    if(isGraph($("#flotResponseTimePercentilesOverTime"))) {
        infos.createGraph();
    }else {
        var choiceContainer = $("#choicesResponseTimePercentilesOverTime");
        createLegend(choiceContainer, infos);
        infos.createGraph();
        setGraphZoomable("#flotResponseTimePercentilesOverTime", "#overviewResponseTimePercentilesOverTime");
        $('#footerResponseTimePercentilesOverTime .legendColorBox > div').each(function(i){
            $(this).clone().prependTo(choiceContainer.find("li").eq(i));
        });
    }
};


var responseTimeVsRequestInfos = {
    data: {"result": {"minY": 227.0, "minX": 2.0, "maxY": 1026.0, "series": [{"data": [[2.0, 582.0], [4.0, 623.5], [16.0, 227.0], [17.0, 238.0], [9.0, 420.0], [10.0, 1026.0], [3.0, 847.0], [13.0, 272.0], [14.0, 422.0]], "isOverall": false, "label": "Successes", "isController": false}], "supportsControllersDiscrimination": false, "granularity": 1000, "maxX": 17.0, "title": "Response Time Vs Request"}},
    getOptions: function() {
        return {
            series: {
                lines: {
                    show: false
                },
                points: {
                    show: true
                }
            },
            xaxis: {
                axisLabel: "Global number of requests per second",
                axisLabelUseCanvas: true,
                axisLabelFontSizePixels: 12,
                axisLabelFontFamily: 'Verdana, Arial',
                axisLabelPadding: 20,
            },
            yaxis: {
                axisLabel: "Median Response Time in ms",
                axisLabelUseCanvas: true,
                axisLabelFontSizePixels: 12,
                axisLabelFontFamily: 'Verdana, Arial',
                axisLabelPadding: 20,
            },
            legend: {
                noColumns: 2,
                show: true,
                container: '#legendResponseTimeVsRequest'
            },
            selection: {
                mode: 'xy'
            },
            grid: {
                hoverable: true // IMPORTANT! this is needed for tooltip to work
            },
            tooltip: true,
            tooltipOpts: {
                content: "%s : Median response time at %x req/s was %y ms"
            },
            colors: ["#9ACD32", "#FF6347"]
        };
    },
    createGraph: function () {
        var data = this.data;
        var dataset = prepareData(data.result.series, $("#choicesResponseTimeVsRequest"));
        var options = this.getOptions();
        prepareOptions(options, data);
        $.plot($("#flotResponseTimeVsRequest"), dataset, options);
        // setup overview
        $.plot($("#overviewResponseTimeVsRequest"), dataset, prepareOverviewOptions(options));

    }
};

// Response Time vs Request
function refreshResponseTimeVsRequest() {
    var infos = responseTimeVsRequestInfos;
    prepareSeries(infos.data);
    if (isGraph($("#flotResponseTimeVsRequest"))){
        infos.createGraph();
    }else{
        var choiceContainer = $("#choicesResponseTimeVsRequest");
        createLegend(choiceContainer, infos);
        infos.createGraph();
        setGraphZoomable("#flotResponseTimeVsRequest", "#overviewResponseTimeVsRequest");
        $('#footerResponseRimeVsRequest .legendColorBox > div').each(function(i){
            $(this).clone().prependTo(choiceContainer.find("li").eq(i));
        });
    }
};


var latenciesVsRequestInfos = {
    data: {"result": {"minY": 0.0, "minX": 2.0, "maxY": 484.0, "series": [{"data": [[2.0, 484.0], [4.0, 115.5], [16.0, 0.0], [17.0, 0.0], [9.0, 227.5], [10.0, 231.5], [3.0, 427.0], [13.0, 0.0], [14.0, 0.0]], "isOverall": false, "label": "Successes", "isController": false}], "supportsControllersDiscrimination": false, "granularity": 1000, "maxX": 17.0, "title": "Latencies Vs Request"}},
    getOptions: function() {
        return{
            series: {
                lines: {
                    show: false
                },
                points: {
                    show: true
                }
            },
            xaxis: {
                axisLabel: "Global number of requests per second",
                axisLabelUseCanvas: true,
                axisLabelFontSizePixels: 12,
                axisLabelFontFamily: 'Verdana, Arial',
                axisLabelPadding: 20,
            },
            yaxis: {
                axisLabel: "Median Latency in ms",
                axisLabelUseCanvas: true,
                axisLabelFontSizePixels: 12,
                axisLabelFontFamily: 'Verdana, Arial',
                axisLabelPadding: 20,
            },
            legend: { noColumns: 2,show: true, container: '#legendLatencyVsRequest' },
            selection: {
                mode: 'xy'
            },
            grid: {
                hoverable: true // IMPORTANT! this is needed for tooltip to work
            },
            tooltip: true,
            tooltipOpts: {
                content: "%s : Median Latency time at %x req/s was %y ms"
            },
            colors: ["#9ACD32", "#FF6347"]
        };
    },
    createGraph: function () {
        var data = this.data;
        var dataset = prepareData(data.result.series, $("#choicesLatencyVsRequest"));
        var options = this.getOptions();
        prepareOptions(options, data);
        $.plot($("#flotLatenciesVsRequest"), dataset, options);
        // setup overview
        $.plot($("#overviewLatenciesVsRequest"), dataset, prepareOverviewOptions(options));
    }
};

// Latencies vs Request
function refreshLatenciesVsRequest() {
        var infos = latenciesVsRequestInfos;
        prepareSeries(infos.data);
        if(isGraph($("#flotLatenciesVsRequest"))){
            infos.createGraph();
        }else{
            var choiceContainer = $("#choicesLatencyVsRequest");
            createLegend(choiceContainer, infos);
            infos.createGraph();
            setGraphZoomable("#flotLatenciesVsRequest", "#overviewLatenciesVsRequest");
            $('#footerLatenciesVsRequest .legendColorBox > div').each(function(i){
                $(this).clone().prependTo(choiceContainer.find("li").eq(i));
            });
        }
};

var hitsPerSecondInfos = {
        data: {"result": {"minY": 1.7166666666666666, "minX": 1.68914544E12, "maxY": 1.7166666666666666, "series": [{"data": [[1.68914544E12, 1.7166666666666666]], "isOverall": false, "label": "hitsPerSecond", "isController": false}], "supportsControllersDiscrimination": false, "granularity": 60000, "maxX": 1.68914544E12, "title": "Hits Per Second"}},
        getOptions: function() {
            return {
                series: {
                    lines: {
                        show: true
                    },
                    points: {
                        show: true
                    }
                },
                xaxis: {
                    mode: "time",
                    timeformat: getTimeFormat(this.data.result.granularity),
                    axisLabel: getElapsedTimeLabel(this.data.result.granularity),
                    axisLabelUseCanvas: true,
                    axisLabelFontSizePixels: 12,
                    axisLabelFontFamily: 'Verdana, Arial',
                    axisLabelPadding: 20,
                },
                yaxis: {
                    axisLabel: "Number of hits / sec",
                    axisLabelUseCanvas: true,
                    axisLabelFontSizePixels: 12,
                    axisLabelFontFamily: 'Verdana, Arial',
                    axisLabelPadding: 20
                },
                legend: {
                    noColumns: 2,
                    show: true,
                    container: "#legendHitsPerSecond"
                },
                selection: {
                    mode : 'xy'
                },
                grid: {
                    hoverable: true // IMPORTANT! this is needed for tooltip to
                                    // work
                },
                tooltip: true,
                tooltipOpts: {
                    content: "%s at %x was %y.2 hits/sec"
                }
            };
        },
        createGraph: function createGraph() {
            var data = this.data;
            var dataset = prepareData(data.result.series, $("#choicesHitsPerSecond"));
            var options = this.getOptions();
            prepareOptions(options, data);
            $.plot($("#flotHitsPerSecond"), dataset, options);
            // setup overview
            $.plot($("#overviewHitsPerSecond"), dataset, prepareOverviewOptions(options));
        }
};

// Hits per second
function refreshHitsPerSecond(fixTimestamps) {
    var infos = hitsPerSecondInfos;
    prepareSeries(infos.data);
    if(fixTimestamps) {
        fixTimeStamps(infos.data.result.series, 18000000);
    }
    if (isGraph($("#flotHitsPerSecond"))){
        infos.createGraph();
    }else{
        var choiceContainer = $("#choicesHitsPerSecond");
        createLegend(choiceContainer, infos);
        infos.createGraph();
        setGraphZoomable("#flotHitsPerSecond", "#overviewHitsPerSecond");
        $('#footerHitsPerSecond .legendColorBox > div').each(function(i){
            $(this).clone().prependTo(choiceContainer.find("li").eq(i));
        });
    }
}

var codesPerSecondInfos = {
        data: {"result": {"minY": 0.016666666666666666, "minX": 1.68914544E12, "maxY": 1.0833333333333333, "series": [{"data": [[1.68914544E12, 0.6166666666666667]], "isOverall": false, "label": "200", "isController": false}, {"data": [[1.68914544E12, 0.016666666666666666]], "isOverall": false, "label": "302", "isController": false}, {"data": [[1.68914544E12, 1.0833333333333333]], "isOverall": false, "label": "304", "isController": false}], "supportsControllersDiscrimination": false, "granularity": 60000, "maxX": 1.68914544E12, "title": "Codes Per Second"}},
        getOptions: function(){
            return {
                series: {
                    lines: {
                        show: true
                    },
                    points: {
                        show: true
                    }
                },
                xaxis: {
                    mode: "time",
                    timeformat: getTimeFormat(this.data.result.granularity),
                    axisLabel: getElapsedTimeLabel(this.data.result.granularity),
                    axisLabelUseCanvas: true,
                    axisLabelFontSizePixels: 12,
                    axisLabelFontFamily: 'Verdana, Arial',
                    axisLabelPadding: 20,
                },
                yaxis: {
                    axisLabel: "Number of responses / sec",
                    axisLabelUseCanvas: true,
                    axisLabelFontSizePixels: 12,
                    axisLabelFontFamily: 'Verdana, Arial',
                    axisLabelPadding: 20,
                },
                legend: {
                    noColumns: 2,
                    show: true,
                    container: "#legendCodesPerSecond"
                },
                selection: {
                    mode: 'xy'
                },
                grid: {
                    hoverable: true // IMPORTANT! this is needed for tooltip to
                                    // work
                },
                tooltip: true,
                tooltipOpts: {
                    content: "Number of Response Codes %s at %x was %y.2 responses / sec"
                }
            };
        },
    createGraph: function() {
        var data = this.data;
        var dataset = prepareData(data.result.series, $("#choicesCodesPerSecond"));
        var options = this.getOptions();
        prepareOptions(options, data);
        $.plot($("#flotCodesPerSecond"), dataset, options);
        // setup overview
        $.plot($("#overviewCodesPerSecond"), dataset, prepareOverviewOptions(options));
    }
};

// Codes per second
function refreshCodesPerSecond(fixTimestamps) {
    var infos = codesPerSecondInfos;
    prepareSeries(infos.data);
    if(fixTimestamps) {
        fixTimeStamps(infos.data.result.series, 18000000);
    }
    if(isGraph($("#flotCodesPerSecond"))){
        infos.createGraph();
    }else{
        var choiceContainer = $("#choicesCodesPerSecond");
        createLegend(choiceContainer, infos);
        infos.createGraph();
        setGraphZoomable("#flotCodesPerSecond", "#overviewCodesPerSecond");
        $('#footerCodesPerSecond .legendColorBox > div').each(function(i){
            $(this).clone().prependTo(choiceContainer.find("li").eq(i));
        });
    }
};

var transactionsPerSecondInfos = {
        data: {"result": {"minY": 0.016666666666666666, "minX": 1.68914544E12, "maxY": 0.03333333333333333, "series": [{"data": [[1.68914544E12, 0.016666666666666666]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-23-success", "isController": false}, {"data": [[1.68914544E12, 0.016666666666666666]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-8-success", "isController": false}, {"data": [[1.68914544E12, 0.016666666666666666]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-18-success", "isController": false}, {"data": [[1.68914544E12, 0.016666666666666666]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-success", "isController": false}, {"data": [[1.68914544E12, 0.016666666666666666]], "isOverall": false, "label": "https://vinfax-api.designitic.com/-success", "isController": false}, {"data": [[1.68914544E12, 0.016666666666666666]], "isOverall": false, "label": "https://vinfax-api.designitic.com/-8-success", "isController": false}, {"data": [[1.68914544E12, 0.016666666666666666]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-9-success", "isController": false}, {"data": [[1.68914544E12, 0.016666666666666666]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-22-success", "isController": false}, {"data": [[1.68914544E12, 0.016666666666666666]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-1-success", "isController": false}, {"data": [[1.68914544E12, 0.016666666666666666]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-16-success", "isController": false}, {"data": [[1.68914544E12, 0.016666666666666666]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-20-success", "isController": false}, {"data": [[1.68914544E12, 0.016666666666666666]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-7-success", "isController": false}, {"data": [[1.68914544E12, 0.016666666666666666]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-4-success", "isController": false}, {"data": [[1.68914544E12, 0.016666666666666666]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-17-success", "isController": false}, {"data": [[1.68914544E12, 0.016666666666666666]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-24-success", "isController": false}, {"data": [[1.68914544E12, 0.03333333333333333]], "isOverall": false, "label": "https://vinfax-api.designitic.com/-1-success", "isController": false}, {"data": [[1.68914544E12, 0.016666666666666666]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-26-success", "isController": false}, {"data": [[1.68914544E12, 0.016666666666666666]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-0-success", "isController": false}, {"data": [[1.68914544E12, 0.016666666666666666]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-18-success", "isController": false}, {"data": [[1.68914544E12, 0.016666666666666666]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-10-success", "isController": false}, {"data": [[1.68914544E12, 0.016666666666666666]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-13-success", "isController": false}, {"data": [[1.68914544E12, 0.016666666666666666]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-27-success", "isController": false}, {"data": [[1.68914544E12, 0.016666666666666666]], "isOverall": false, "label": "https://vinfax-api.designitic.com/-5-success", "isController": false}, {"data": [[1.68914544E12, 0.016666666666666666]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-3-success", "isController": false}, {"data": [[1.68914544E12, 0.016666666666666666]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-14-success", "isController": false}, {"data": [[1.68914544E12, 0.016666666666666666]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-28-success", "isController": false}, {"data": [[1.68914544E12, 0.016666666666666666]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-12-success", "isController": false}, {"data": [[1.68914544E12, 0.016666666666666666]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-17-success", "isController": false}, {"data": [[1.68914544E12, 0.016666666666666666]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-19-success", "isController": false}, {"data": [[1.68914544E12, 0.016666666666666666]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-6-success", "isController": false}, {"data": [[1.68914544E12, 0.016666666666666666]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-24-success", "isController": false}, {"data": [[1.68914544E12, 0.016666666666666666]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-9-success", "isController": false}, {"data": [[1.68914544E12, 0.016666666666666666]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-2-success", "isController": false}, {"data": [[1.68914544E12, 0.016666666666666666]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-8-success", "isController": false}, {"data": [[1.68914544E12, 0.016666666666666666]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-success", "isController": false}, {"data": [[1.68914544E12, 0.016666666666666666]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-21-success", "isController": false}, {"data": [[1.68914544E12, 0.016666666666666666]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-20-success", "isController": false}, {"data": [[1.68914544E12, 0.016666666666666666]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-5-success", "isController": false}, {"data": [[1.68914544E12, 0.03333333333333333]], "isOverall": false, "label": "https://vinfax-api.designitic.com/-0-success", "isController": false}, {"data": [[1.68914544E12, 0.016666666666666666]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-16-success", "isController": false}, {"data": [[1.68914544E12, 0.016666666666666666]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-27-success", "isController": false}, {"data": [[1.68914544E12, 0.016666666666666666]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-11-success", "isController": false}, {"data": [[1.68914544E12, 0.016666666666666666]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-25-success", "isController": false}, {"data": [[1.68914544E12, 0.016666666666666666]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-23-success", "isController": false}, {"data": [[1.68914544E12, 0.016666666666666666]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-19-success", "isController": false}, {"data": [[1.68914544E12, 0.016666666666666666]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-1-success", "isController": false}, {"data": [[1.68914544E12, 0.016666666666666666]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-15-success", "isController": false}, {"data": [[1.68914544E12, 0.016666666666666666]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-13-success", "isController": false}, {"data": [[1.68914544E12, 0.016666666666666666]], "isOverall": false, "label": "https://vinfax-api.designitic.com/-4-success", "isController": false}, {"data": [[1.68914544E12, 0.016666666666666666]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-12-success", "isController": false}, {"data": [[1.68914544E12, 0.016666666666666666]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-5-success", "isController": false}, {"data": [[1.68914544E12, 0.016666666666666666]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-2-success", "isController": false}, {"data": [[1.68914544E12, 0.016666666666666666]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-6-success", "isController": false}, {"data": [[1.68914544E12, 0.016666666666666666]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-7-success", "isController": false}, {"data": [[1.68914544E12, 0.016666666666666666]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-21-success", "isController": false}, {"data": [[1.68914544E12, 0.016666666666666666]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-3-success", "isController": false}, {"data": [[1.68914544E12, 0.016666666666666666]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-16-success", "isController": false}, {"data": [[1.68914544E12, 0.016666666666666666]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-5-success", "isController": false}, {"data": [[1.68914544E12, 0.016666666666666666]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-2-success", "isController": false}, {"data": [[1.68914544E12, 0.016666666666666666]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-9-success", "isController": false}, {"data": [[1.68914544E12, 0.016666666666666666]], "isOverall": false, "label": "https://vinfax-api.designitic.com/-11-success", "isController": false}, {"data": [[1.68914544E12, 0.016666666666666666]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-20-success", "isController": false}, {"data": [[1.68914544E12, 0.016666666666666666]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-22-success", "isController": false}, {"data": [[1.68914544E12, 0.016666666666666666]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-18-success", "isController": false}, {"data": [[1.68914544E12, 0.016666666666666666]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-success", "isController": false}, {"data": [[1.68914544E12, 0.016666666666666666]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-10-success", "isController": false}, {"data": [[1.68914544E12, 0.016666666666666666]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-15-success", "isController": false}, {"data": [[1.68914544E12, 0.016666666666666666]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-26-success", "isController": false}, {"data": [[1.68914544E12, 0.016666666666666666]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-24-success", "isController": false}, {"data": [[1.68914544E12, 0.016666666666666666]], "isOverall": false, "label": "https://vinfax-api.designitic.com/-3-success", "isController": false}, {"data": [[1.68914544E12, 0.016666666666666666]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-1-success", "isController": false}, {"data": [[1.68914544E12, 0.016666666666666666]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-11-success", "isController": false}, {"data": [[1.68914544E12, 0.016666666666666666]], "isOverall": false, "label": "https://vinfax-api.designitic.com/-7-success", "isController": false}, {"data": [[1.68914544E12, 0.016666666666666666]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-14-success", "isController": false}, {"data": [[1.68914544E12, 0.016666666666666666]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-12-success", "isController": false}, {"data": [[1.68914544E12, 0.016666666666666666]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-6-success", "isController": false}, {"data": [[1.68914544E12, 0.016666666666666666]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-25-success", "isController": false}, {"data": [[1.68914544E12, 0.016666666666666666]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-4-success", "isController": false}, {"data": [[1.68914544E12, 0.016666666666666666]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-4-success", "isController": false}, {"data": [[1.68914544E12, 0.016666666666666666]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-15-success", "isController": false}, {"data": [[1.68914544E12, 0.016666666666666666]], "isOverall": false, "label": "https://vinfax-api.designitic.com/-9-success", "isController": false}, {"data": [[1.68914544E12, 0.016666666666666666]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-7-success", "isController": false}, {"data": [[1.68914544E12, 0.016666666666666666]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-22-success", "isController": false}, {"data": [[1.68914544E12, 0.016666666666666666]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-3-success", "isController": false}, {"data": [[1.68914544E12, 0.016666666666666666]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-0-success", "isController": false}, {"data": [[1.68914544E12, 0.016666666666666666]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-19-success", "isController": false}, {"data": [[1.68914544E12, 0.016666666666666666]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-17-success", "isController": false}, {"data": [[1.68914544E12, 0.016666666666666666]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-21-success", "isController": false}, {"data": [[1.68914544E12, 0.016666666666666666]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-8-success", "isController": false}, {"data": [[1.68914544E12, 0.016666666666666666]], "isOverall": false, "label": "https://vinfax-api.designitic.com/-2-success", "isController": false}, {"data": [[1.68914544E12, 0.016666666666666666]], "isOverall": false, "label": "https://vinfax-api.designitic.com/-10-success", "isController": false}, {"data": [[1.68914544E12, 0.016666666666666666]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-23-success", "isController": false}, {"data": [[1.68914544E12, 0.016666666666666666]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-25-success", "isController": false}, {"data": [[1.68914544E12, 0.016666666666666666]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-14-success", "isController": false}, {"data": [[1.68914544E12, 0.016666666666666666]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-11-success", "isController": false}, {"data": [[1.68914544E12, 0.016666666666666666]], "isOverall": false, "label": "https://vinfax-api.designitic.com/-6-success", "isController": false}, {"data": [[1.68914544E12, 0.016666666666666666]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-0-success", "isController": false}, {"data": [[1.68914544E12, 0.016666666666666666]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-26-success", "isController": false}, {"data": [[1.68914544E12, 0.016666666666666666]], "isOverall": false, "label": "https://vinfax-api.designitic.com/login-27-success", "isController": false}, {"data": [[1.68914544E12, 0.016666666666666666]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/subscription-13-success", "isController": false}, {"data": [[1.68914544E12, 0.016666666666666666]], "isOverall": false, "label": "https://vinfax-api.designitic.com/user/download-history-10-success", "isController": false}], "supportsControllersDiscrimination": true, "granularity": 60000, "maxX": 1.68914544E12, "title": "Transactions Per Second"}},
        getOptions: function(){
            return {
                series: {
                    lines: {
                        show: true
                    },
                    points: {
                        show: true
                    }
                },
                xaxis: {
                    mode: "time",
                    timeformat: getTimeFormat(this.data.result.granularity),
                    axisLabel: getElapsedTimeLabel(this.data.result.granularity),
                    axisLabelUseCanvas: true,
                    axisLabelFontSizePixels: 12,
                    axisLabelFontFamily: 'Verdana, Arial',
                    axisLabelPadding: 20,
                },
                yaxis: {
                    axisLabel: "Number of transactions / sec",
                    axisLabelUseCanvas: true,
                    axisLabelFontSizePixels: 12,
                    axisLabelFontFamily: 'Verdana, Arial',
                    axisLabelPadding: 20
                },
                legend: {
                    noColumns: 2,
                    show: true,
                    container: "#legendTransactionsPerSecond"
                },
                selection: {
                    mode: 'xy'
                },
                grid: {
                    hoverable: true // IMPORTANT! this is needed for tooltip to
                                    // work
                },
                tooltip: true,
                tooltipOpts: {
                    content: "%s at %x was %y transactions / sec"
                }
            };
        },
    createGraph: function () {
        var data = this.data;
        var dataset = prepareData(data.result.series, $("#choicesTransactionsPerSecond"));
        var options = this.getOptions();
        prepareOptions(options, data);
        $.plot($("#flotTransactionsPerSecond"), dataset, options);
        // setup overview
        $.plot($("#overviewTransactionsPerSecond"), dataset, prepareOverviewOptions(options));
    }
};

// Transactions per second
function refreshTransactionsPerSecond(fixTimestamps) {
    var infos = transactionsPerSecondInfos;
    prepareSeries(infos.data);
    if(infos.data.result.series.length == 0) {
        setEmptyGraph("#bodyTransactionsPerSecond");
        return;
    }
    if(fixTimestamps) {
        fixTimeStamps(infos.data.result.series, 18000000);
    }
    if(isGraph($("#flotTransactionsPerSecond"))){
        infos.createGraph();
    }else{
        var choiceContainer = $("#choicesTransactionsPerSecond");
        createLegend(choiceContainer, infos);
        infos.createGraph();
        setGraphZoomable("#flotTransactionsPerSecond", "#overviewTransactionsPerSecond");
        $('#footerTransactionsPerSecond .legendColorBox > div').each(function(i){
            $(this).clone().prependTo(choiceContainer.find("li").eq(i));
        });
    }
};

var totalTPSInfos = {
        data: {"result": {"minY": 1.7166666666666666, "minX": 1.68914544E12, "maxY": 1.7166666666666666, "series": [{"data": [[1.68914544E12, 1.7166666666666666]], "isOverall": false, "label": "Transaction-success", "isController": false}, {"data": [], "isOverall": false, "label": "Transaction-failure", "isController": false}], "supportsControllersDiscrimination": true, "granularity": 60000, "maxX": 1.68914544E12, "title": "Total Transactions Per Second"}},
        getOptions: function(){
            return {
                series: {
                    lines: {
                        show: true
                    },
                    points: {
                        show: true
                    }
                },
                xaxis: {
                    mode: "time",
                    timeformat: getTimeFormat(this.data.result.granularity),
                    axisLabel: getElapsedTimeLabel(this.data.result.granularity),
                    axisLabelUseCanvas: true,
                    axisLabelFontSizePixels: 12,
                    axisLabelFontFamily: 'Verdana, Arial',
                    axisLabelPadding: 20,
                },
                yaxis: {
                    axisLabel: "Number of transactions / sec",
                    axisLabelUseCanvas: true,
                    axisLabelFontSizePixels: 12,
                    axisLabelFontFamily: 'Verdana, Arial',
                    axisLabelPadding: 20
                },
                legend: {
                    noColumns: 2,
                    show: true,
                    container: "#legendTotalTPS"
                },
                selection: {
                    mode: 'xy'
                },
                grid: {
                    hoverable: true // IMPORTANT! this is needed for tooltip to
                                    // work
                },
                tooltip: true,
                tooltipOpts: {
                    content: "%s at %x was %y transactions / sec"
                },
                colors: ["#9ACD32", "#FF6347"]
            };
        },
    createGraph: function () {
        var data = this.data;
        var dataset = prepareData(data.result.series, $("#choicesTotalTPS"));
        var options = this.getOptions();
        prepareOptions(options, data);
        $.plot($("#flotTotalTPS"), dataset, options);
        // setup overview
        $.plot($("#overviewTotalTPS"), dataset, prepareOverviewOptions(options));
    }
};

// Total Transactions per second
function refreshTotalTPS(fixTimestamps) {
    var infos = totalTPSInfos;
    // We want to ignore seriesFilter
    prepareSeries(infos.data, false, true);
    if(fixTimestamps) {
        fixTimeStamps(infos.data.result.series, 18000000);
    }
    if(isGraph($("#flotTotalTPS"))){
        infos.createGraph();
    }else{
        var choiceContainer = $("#choicesTotalTPS");
        createLegend(choiceContainer, infos);
        infos.createGraph();
        setGraphZoomable("#flotTotalTPS", "#overviewTotalTPS");
        $('#footerTotalTPS .legendColorBox > div').each(function(i){
            $(this).clone().prependTo(choiceContainer.find("li").eq(i));
        });
    }
};

// Collapse the graph matching the specified DOM element depending the collapsed
// status
function collapse(elem, collapsed){
    if(collapsed){
        $(elem).parent().find(".fa-chevron-up").removeClass("fa-chevron-up").addClass("fa-chevron-down");
    } else {
        $(elem).parent().find(".fa-chevron-down").removeClass("fa-chevron-down").addClass("fa-chevron-up");
        if (elem.id == "bodyBytesThroughputOverTime") {
            if (isGraph($(elem).find('.flot-chart-content')) == false) {
                refreshBytesThroughputOverTime(true);
            }
            document.location.href="#bytesThroughputOverTime";
        } else if (elem.id == "bodyLatenciesOverTime") {
            if (isGraph($(elem).find('.flot-chart-content')) == false) {
                refreshLatenciesOverTime(true);
            }
            document.location.href="#latenciesOverTime";
        } else if (elem.id == "bodyCustomGraph") {
            if (isGraph($(elem).find('.flot-chart-content')) == false) {
                refreshCustomGraph(true);
            }
            document.location.href="#responseCustomGraph";
        } else if (elem.id == "bodyConnectTimeOverTime") {
            if (isGraph($(elem).find('.flot-chart-content')) == false) {
                refreshConnectTimeOverTime(true);
            }
            document.location.href="#connectTimeOverTime";
        } else if (elem.id == "bodyResponseTimePercentilesOverTime") {
            if (isGraph($(elem).find('.flot-chart-content')) == false) {
                refreshResponseTimePercentilesOverTime(true);
            }
            document.location.href="#responseTimePercentilesOverTime";
        } else if (elem.id == "bodyResponseTimeDistribution") {
            if (isGraph($(elem).find('.flot-chart-content')) == false) {
                refreshResponseTimeDistribution();
            }
            document.location.href="#responseTimeDistribution" ;
        } else if (elem.id == "bodySyntheticResponseTimeDistribution") {
            if (isGraph($(elem).find('.flot-chart-content')) == false) {
                refreshSyntheticResponseTimeDistribution();
            }
            document.location.href="#syntheticResponseTimeDistribution" ;
        } else if (elem.id == "bodyActiveThreadsOverTime") {
            if (isGraph($(elem).find('.flot-chart-content')) == false) {
                refreshActiveThreadsOverTime(true);
            }
            document.location.href="#activeThreadsOverTime";
        } else if (elem.id == "bodyTimeVsThreads") {
            if (isGraph($(elem).find('.flot-chart-content')) == false) {
                refreshTimeVsThreads();
            }
            document.location.href="#timeVsThreads" ;
        } else if (elem.id == "bodyCodesPerSecond") {
            if (isGraph($(elem).find('.flot-chart-content')) == false) {
                refreshCodesPerSecond(true);
            }
            document.location.href="#codesPerSecond";
        } else if (elem.id == "bodyTransactionsPerSecond") {
            if (isGraph($(elem).find('.flot-chart-content')) == false) {
                refreshTransactionsPerSecond(true);
            }
            document.location.href="#transactionsPerSecond";
        } else if (elem.id == "bodyTotalTPS") {
            if (isGraph($(elem).find('.flot-chart-content')) == false) {
                refreshTotalTPS(true);
            }
            document.location.href="#totalTPS";
        } else if (elem.id == "bodyResponseTimeVsRequest") {
            if (isGraph($(elem).find('.flot-chart-content')) == false) {
                refreshResponseTimeVsRequest();
            }
            document.location.href="#responseTimeVsRequest";
        } else if (elem.id == "bodyLatenciesVsRequest") {
            if (isGraph($(elem).find('.flot-chart-content')) == false) {
                refreshLatenciesVsRequest();
            }
            document.location.href="#latencyVsRequest";
        }
    }
}

/*
 * Activates or deactivates all series of the specified graph (represented by id parameter)
 * depending on checked argument.
 */
function toggleAll(id, checked){
    var placeholder = document.getElementById(id);

    var cases = $(placeholder).find(':checkbox');
    cases.prop('checked', checked);
    $(cases).parent().children().children().toggleClass("legend-disabled", !checked);

    var choiceContainer;
    if ( id == "choicesBytesThroughputOverTime"){
        choiceContainer = $("#choicesBytesThroughputOverTime");
        refreshBytesThroughputOverTime(false);
    } else if(id == "choicesResponseTimesOverTime"){
        choiceContainer = $("#choicesResponseTimesOverTime");
        refreshResponseTimeOverTime(false);
    }else if(id == "choicesResponseCustomGraph"){
        choiceContainer = $("#choicesResponseCustomGraph");
        refreshCustomGraph(false);
    } else if ( id == "choicesLatenciesOverTime"){
        choiceContainer = $("#choicesLatenciesOverTime");
        refreshLatenciesOverTime(false);
    } else if ( id == "choicesConnectTimeOverTime"){
        choiceContainer = $("#choicesConnectTimeOverTime");
        refreshConnectTimeOverTime(false);
    } else if ( id == "choicesResponseTimePercentilesOverTime"){
        choiceContainer = $("#choicesResponseTimePercentilesOverTime");
        refreshResponseTimePercentilesOverTime(false);
    } else if ( id == "choicesResponseTimePercentiles"){
        choiceContainer = $("#choicesResponseTimePercentiles");
        refreshResponseTimePercentiles();
    } else if(id == "choicesActiveThreadsOverTime"){
        choiceContainer = $("#choicesActiveThreadsOverTime");
        refreshActiveThreadsOverTime(false);
    } else if ( id == "choicesTimeVsThreads"){
        choiceContainer = $("#choicesTimeVsThreads");
        refreshTimeVsThreads();
    } else if ( id == "choicesSyntheticResponseTimeDistribution"){
        choiceContainer = $("#choicesSyntheticResponseTimeDistribution");
        refreshSyntheticResponseTimeDistribution();
    } else if ( id == "choicesResponseTimeDistribution"){
        choiceContainer = $("#choicesResponseTimeDistribution");
        refreshResponseTimeDistribution();
    } else if ( id == "choicesHitsPerSecond"){
        choiceContainer = $("#choicesHitsPerSecond");
        refreshHitsPerSecond(false);
    } else if(id == "choicesCodesPerSecond"){
        choiceContainer = $("#choicesCodesPerSecond");
        refreshCodesPerSecond(false);
    } else if ( id == "choicesTransactionsPerSecond"){
        choiceContainer = $("#choicesTransactionsPerSecond");
        refreshTransactionsPerSecond(false);
    } else if ( id == "choicesTotalTPS"){
        choiceContainer = $("#choicesTotalTPS");
        refreshTotalTPS(false);
    } else if ( id == "choicesResponseTimeVsRequest"){
        choiceContainer = $("#choicesResponseTimeVsRequest");
        refreshResponseTimeVsRequest();
    } else if ( id == "choicesLatencyVsRequest"){
        choiceContainer = $("#choicesLatencyVsRequest");
        refreshLatenciesVsRequest();
    }
    var color = checked ? "black" : "#818181";
    if(choiceContainer != null) {
        choiceContainer.find("label").each(function(){
            this.style.color = color;
        });
    }
}
