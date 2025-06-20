using MahApps.Metro.Controls;

namespace WpfMrpSimulatorApp.Views
{
    /// <summary>
    /// MainView.xaml에 대한 상호 작용 논리
    /// </summary>
    public partial class MainView : MetroWindow
    {
        public MainView()
        {
            InitializeComponent();
        }

        private void MetroWindow_Closing(object sender, System.ComponentModel.CancelEventArgs e)
        {
            e.Cancel = true; // x 버튼을 눌러도, Alt+F4를 눌러도 종료되지 않도록 함
        }
    }
}
