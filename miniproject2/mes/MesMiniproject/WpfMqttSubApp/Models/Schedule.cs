using System;
using System.Collections.Generic;

namespace WpfMqttSubApp.Models;

public partial class Schedule
{
    /// <summary>
    /// 공정계획 순번(자동 증가)
    /// </summary>
    public int SchIdx { get; set; }

    /// <summary>
    /// 공장 코드
    /// </summary>
    public string PlantCode { get; set; } = null!;

    public DateTime SchDate { get; set; }

    public int LoadTime { get; set; }

    /// <summary>
    /// 계획된 시작 시간
    /// </summary>
    public TimeOnly? SchStartTime { get; set; }

    /// <summary>
    /// 계획된 종료 시간
    /// </summary>
    public TimeOnly? SchEndTime { get; set; }

    /// <summary>
    /// 생산설비 ID
    /// </summary>
    public string? SchFacilityId { get; set; }

    /// <summary>
    /// 계획목표 수량
    /// </summary>
    public int? SchAmount { get; set; }

    public DateTime? RegDt { get; set; }

    public DateTime? ModDt { get; set; }

    public virtual ICollection<Process> Processes { get; set; } = new List<Process>();
}
