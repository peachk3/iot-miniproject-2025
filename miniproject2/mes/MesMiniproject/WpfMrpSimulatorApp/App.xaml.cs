using MahApps.Metro.Controls.Dialogs;
using System.Windows;
using WpfMrpSimulatorApp.Helpers;
using WpfMrpSimulatorApp.ViewModels;
using WpfMrpSimulatorApp.Views;

namespace WpfMrpSimulatorApp
{
    /// <summary>
    /// Interaction logic for App.xaml
    /// </summary>
    public partial class App : Application
    {
        private void Application_Startup(object sender, StartupEventArgs e)
        {
            Common.DIALOGVCOORDINATOR = DialogCoordinator.Instance;

            var viewModel = new MainViewModel(Common.DIALOGVCOORDINATOR);
            var view = new MainView
            {
                DataContext = viewModel,
            };
            view.ShowDialog();
        }
    }

}
