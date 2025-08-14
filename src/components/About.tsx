
const About = () => {
  const stats = [
    { number: "3+", label: "Years Experience" },
    { number: "25+", label: "Projects Completed" },
    { number: "10+", label: "Technologies" },
    { number: "100%", label: "Client Satisfaction" },
  ];

  return (
    <section id="about" className="section-alternate">
      <div className="section-container">
        <div className="text-center mb-16">
          <h2 className="heading-section animate-fade-up">About Me</h2>
          <div className="w-24 h-1 bg-gradient-to-r from-primary to-green-600 mx-auto mb-8"></div>
        </div>

        <div className="grid lg:grid-cols-2 gap-12 items-center">
          <div className="animate-slide-in">
            <h3 className="text-2xl font-semibold mb-6">Professional Summary</h3>
            <div className="space-y-4 text-muted-foreground leading-relaxed">
              <p>
                I'm a passionate Full Stack Developer with over 3 years of experience creating
                innovative web applications and digital solutions. My expertise spans across
                modern frontend frameworks, robust backend systems, and cloud technologies.
              </p>
              <p>
                I believe in writing clean, maintainable code and creating user-centric
                applications that solve real-world problems. My approach combines technical
                excellence with creative problem-solving to deliver exceptional results.
              </p>
              <p>
                When I'm not coding, you'll find me exploring new technologies, contributing
                to open-source projects, or sharing knowledge with the developer community.
              </p>
            </div>
          </div>

          <div className="grid grid-cols-2 gap-6 animate-fade-up">
            {stats.map((stat, index) => (
              <div
                key={index}
                className="card-elevated p-6 text-center hover-lift"
              >
                <div className="text-3xl font-bold text-green-600 mb-2">
                  {stat.number}
                </div>
                <div className="text-sm text-muted-foreground font-medium">
                  {stat.label}
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </section>
  );
};

export default About;
