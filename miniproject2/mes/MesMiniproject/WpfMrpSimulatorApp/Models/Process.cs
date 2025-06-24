using System;
using System.Collections.Generic;

namespace WpfMrpSimulatorApp.Models;

public partial class Process
{
    /// <summary>
    /// 공정처리 순번(자동 증가)
    /// </summary>
    public int PrcIdx { get; set; }

    public int SchIdx { get; set; }

    /// <summary>
    /// 공정처리ID(UK)
    /// yyyyMMdd-NewGuid(36)
    /// </summary>
    public string PrcCd { get; set; } = null!;

    public DateOnly PrcDate { get; set; }

    public int PrcLoadTime { get; set; }

    public TimeOnly? PrcStartTime { get; set; }

    public TimeOnly? PrcEndTime { get; set; }

    public string? PrcFacilityId { get; set; }

    /// <summary>
    /// 공정처리 여부(1성공, 0실패)
    /// </summary>
    public sbyte? PrcResult { get; set; }

    /// <summary>
    /// 등록일
    /// </summary>
    public DateTime? RegDt { get; set; }

    /// <summary>
    /// 수정일
    /// </summary>
    public DateTime? ModDt { get; set; }

    public virtual Schedule SchIdxNavigation { get; set; } = null!;
}
