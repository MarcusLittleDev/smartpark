using Microsoft.Owin;
using Owin;
using System.Net.WebSockets;

[assembly: OwinStartupAttribute(typeof(SmartPark.Startup))]
namespace SmartPark
{
    public partial class Startup
    {


        public void Configuration(IAppBuilder app)
        {
            ConfigureAuth(app);
        }


    }
}
