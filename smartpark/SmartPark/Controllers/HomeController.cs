using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;

namespace SmartPark.Controllers
{
    public class HomeController : Controller
    {
        public ActionResult Index()
        {
            return View();
        }

        public ActionResult About()
        {
            ViewBag.Message = "Development Team";
             
            return View();
        }

        public ActionResult Contact()
        {
            ViewBag.Message = "How It Works";

            return View();
        }

        public ActionResult Students()
        {
            ViewBag.Message = "Students";

            return View();
        }

        public ActionResult RealTimeData()
        {
            return PartialView("_spots");
        }
    }
}