namespace TestWebApp
{
    public class Program
    {
        public static void Main(string[] args)
        {
            var builder = WebApplication.CreateBuilder(args);

            // HttpClient ���
            builder.Services.AddHttpClient("MyWebClient", client =>
            {
                client.BaseAddress = new Uri("http://localhost:8000");  // Python Uvcorn ���� URL
            });

            // CORS ���
            builder.Services.AddCors(options => {
                // �׽�Ʈ �ÿ��� ���. ����� ���� ������, ���� ����ϴ� �޼��常 �������� ��
                options.AddDefaultPolicy(policy =>
                {
                    policy.AllowAnyOrigin().AllowAnyMethod().AllowAnyHeader();
                });
            });

            builder.Services.AddControllers();   // ��Ʈ�ѷ� ��� ���
            var app = builder.Build();

            //app.MapGet("/", () => "Hello World!");
            app.UseCors();              // ������ ������ CORS�� ����ϰڴ�
            app.UseDefaultFiles();      // index.html�� �ڵ�ó�� �ϰڴ�
            app.UseStaticFiles();       // wwwroot ������� ����ϰڴ�
            app.MapControllers();       // Controller ��� ����(���)�ϰڴ�

            app.Run();
        }
    }
}
