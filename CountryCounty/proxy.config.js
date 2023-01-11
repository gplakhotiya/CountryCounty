module.export =[
    {
        context:["/","/Search"],
        target:"http://127.0.0.1:5000",
        secure:false,
        logLevel:"debug",
        bypass: function(req,res, proxyOptions){
            res.setHeader("Access-Control-Allow-Origin","http://127.0.0.1:5000")
        }
    }
];