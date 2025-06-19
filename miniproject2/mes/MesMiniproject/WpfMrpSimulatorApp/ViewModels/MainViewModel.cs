using CommunityToolkit.Mvvm.ComponentModel;

namespace WpfMrpSimulatorApp.ViewModels
{
    public partial class MainViewModel : ObservableObject
    {
        private string _greeting;

        public MainViewModel()
        {
            Greeting = "MRP 공정관리!";
        }

        public string Greeting
        {
            get => _greeting;
            set => SetProperty(ref _greeting, value);
        }
    }
}
