using CommunityToolkit.Mvvm.ComponentModel;
using CommunityToolkit.Mvvm.Input;
using MahApps.Metro.Controls.Dialogs;
using Org.BouncyCastle.Asn1.BC;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace WpfMrpSimulatorApp.ViewModels
{
    public partial class MonitoringViewModel : ObservableObject
    {
        // readonly 생성자에서 할당하고 나면 그 이후에 값 변경 불가
        private readonly IDialogCoordinator dialogCoordinator;

        public MonitoringViewModel(IDialogCoordinator coordinator)
        {
            this.dialogCoordinator = coordinator; // 파라미터값으로 초기화
        }
        [RelayCommand]
        public async Task SearchProcess()
        {
            await this.dialogCoordinator.ShowMessageAsync(this, "공정조회", "공정조회를 시작합니다.");
        }
        [RelayCommand]
        public async Task StartProcess()
        {
            await this.dialogCoordinator.ShowMessageAsync(this, "공정시작", "공정을 시작합니다.");

        }

    }
}
