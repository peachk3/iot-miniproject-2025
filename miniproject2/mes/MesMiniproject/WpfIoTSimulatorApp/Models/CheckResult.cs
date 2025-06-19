using MahApps.Metro.Converters;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace WpfIoTSimulatorApp.Models
{
    // JSON 전송용 객체
    public class CheckResult
    {
        public string ClientId { get; set; } // IoT 장비 번호
        public string Timestamp { get; set; } // 검사 시간
        public string Result { get; set; } // 검사 결과
    }
}
