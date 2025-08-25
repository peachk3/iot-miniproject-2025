namespace ASPWebApp
{
    public class Program
    {
        public static void Main(string[] args)
        {
            var builder = WebApplication.CreateBuilder(args);

            // HttpClient ���
            builder.Services.AddHttpClient("PythonAiServer", client =>
            {
                client.BaseAddress = new Uri("http://localhost:8000"); 
            });

            // CORS ���(�����׽�Ʈ��) -> ���� ��ô� ��Ȯ�ϰ� �����Ұ�
            builder.Services.AddCors(options => {
                options.AddDefaultPolicy(policy => {
                    policy.AllowAnyOrigin().AllowAnyMethod().AllowAnyHeader();
                });
            });

            builder.Services.AddControllers();
            var app = builder.Build();

            app.UseCors();
            app.UseDefaultFiles();      // index.html ó��
            app.UseStaticFiles();       // wwwroot ���� �Ʒ� ���� ��뼳��
            app.MapControllers();       // MVC�� Controller ����
            //app.MapGet("/", () => "Hello World!");

            app.MapGet("/ai", async context =>
            {
                context.Response.Redirect("/ai.html");
            });

            app.Run();
        }
    }
}
