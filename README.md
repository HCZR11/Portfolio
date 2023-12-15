
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!--========== FAVICON ===========-->
    <link rel="icon" type="image/x-icon" href="/images/portofolio.png">
    <title>Horoiu Portofolio</title>

    <!--=============== REMIXICONS ===============-->
    <link
            href="https://cdn.jsdelivr.net/npm/remixicon@3.0.0/fonts/remixicon.css"
            rel="stylesheet"
    />
    <!--=============== CSS ===============-->
    <link rel="stylesheet" href="/css/styles.css"/>

</head>
<body>
<!--========== HEADER ===========-->

<header class="header" id="header">
    <nav class="nav container">
        <a href="#" class="nav__logo"> <span></span></a>
        <div class="nav__menu" id="nav-menu">
            <ul class="nav__list">
                <li class="nav__item">
                    <a href="#home" class="nav__link active-link"
                    >Home</a
                    >
                </li>
                <li class="nav__item">
                    <a href="#about" class="nav__link">About</a>
                </li>
                <li class="nav__item">
                    <a href="#skills" class="nav__link">Skills</a>
                </li>
                <li class="nav__item">
                    <a href="#services" class="nav__link">Services</a>
                </li>
                <li class="nav__item">
                    <a href="#projects" class="nav__link">Projects</a>
                </li>
                <li class="nav__item">
                    <a href="#contact" class="nav__link">Contact</a>
                </li>
            </ul>
            <!-- Close Button -->
            <div class="nav__close" id="nav-close">
                <i class="ri-close-line"></i>
            </div>
        </div>
        <!-- Toggle button -->
        <div class="nav__toggle" id="nav-toggle">
            <i class="ri-menu-fold-line"></i>
        </div>
    </nav>
</header>
<!--==================== MAIN ====================-->
<main class="main">
    <!--==================== HOME ====================-->
    <section class="home section" id="home">
        <div class="home__container container grid">
            <div class="home__content">
                <div class="home__data">
                    <h3 class="home__subtitle">
                        Hello, <span>I'm</span>
                    </h3>
                    <h1 class="home__title">Horoiu Cezar</h1>
                    <h3 class="home__education">Junior Python Developer || Web Development || DevOps ||
                    </h3>
                    <p class="home__description">
                        Ladies and gentlemen, prepare to enter a world
                        of relentless determination and lethal
                        precision. I am the shadow that strikes fear
                        into the hearts of criminals, the embodiment of
                        vengeance and justice. I am John Wick.
                    </p>
                    <a href="#contact" class="button">Chat</a>
                </div>
                <div class="home__social">
                    <a
                            href="https://github.com/HCZR11"
                            target="_blank"
                            class="home__social-link"
                    >
                        <i class="ri-github-line"></i>
                    </a>
                    <!--                    <a-->
                    <!--                            href="#"-->
                    <!--                            target="_blank"-->
                    <!--                            class="home__social-link"-->
                    <!--                    >-->
                    <!--                        <i class="ri-dribbble-line"></i>-->
                    <!--                    </a>-->
                    <a
                            href="https://www.linkedin.com/in/horoiucezarcvwriting/"
                            target="_blank"
                            class="home__social-link"
                    >
                        <i class="ri-linkedin-fill"></i>
                    </a>
                </div>
            </div>
            <div class="home__image">
                <svg
                        class="home__blob"
                        viewBox="0 0 550 591"
                        xmlns="http://www.w3.org/2000/svg"
                >
                    <mask id="maskBlob" mask-type="alpha">
                          <path
                                                    d="M285 51.6423L499.157 175.286C505.345 178.859 509.157 185.461 509.157
                                                       192.606V439.894C509.157 447.039 505.345 453.641 499.157 457.214L285
                                                       580.858C278.812 584.43 271.188 584.43 265 580.858L50.843 457.214C44.655 453.641
                                                       40.843 447.039 40.843 439.894V192.606C40.843 185.461 44.655 178.859 50.843
                                                       175.286L265 51.6423C271.188 48.0697 278.812 48.0696 285 51.6423Z"
                                                    stroke="black"
                                                    stroke-width="10"
                                            />
                    </mask>
                    <g mask="url(#maskBlob)">
                        <path
                                d="M263 47.1782C270.426 42.891 279.574 42.891 287 47.1782L501.157
                               170.822C508.583 175.109 513.157 183.032 513.157 191.606V438.894C513.157
                               447.468 508.583 455.391 501.157 459.678L287 583.322C279.574 587.609 270.426
                               587.609 263 583.322L48.843 459.678C41.4174 455.391 36.843 447.468 36.843
                               438.894V191.606C36.843 183.032 41.4174 175.109 48.843 170.822L263 47.1782Z"
                        />

                        <rect
                                x="37"
                                width="476"
                                height="630"
                                fill="url(#pattern0)"
                        />
                    </g>

                    <rect
                            x="37"
                            width="476"
                            height="300"
                            fill="url(#pattern1)"
                    />

                    <defs>
                        <pattern
                                id="pattern0"
                                patternContentUnits="objectBoundingBox"
                                width="1"
                                height="1"
                        >
                            <use
                                    href="#imageBlob"
                                    transform="matrix(0.00143057 0 0 0.00108108 0.0404062 0)"
                            />
                        </pattern>

                        <pattern
                                id="pattern1"
                                patternContentUnits="objectBoundingBox"
                                width="1"
                                height="1"
                        >
                            <use
                                    href="#imageBlob"
                                    transform="matrix(0.00143057 0 0 0.00226984 0.0404062 0)"
                            />
                        </pattern>

                        <!-- Insert your profile (recommended size: 640 x 940) -->
                        <image
                                class="home__img"
                                id="imageBlob"
                                width="740"
                                height="1225"
                                href="images/hc.png"
                        />
                    </defs>
                </svg>
            </div>
        </div>
    </section>

    <!--==================== ABOUT ====================-->
    <section class="about section" id="about">
        <div class="about__container container grid">
            <div class="about__data" >
                <h3 class="section__subtitle">My <span>Intro</span></h3>
                <h2 class="section__title">About Me</h2>
                <p class="about__description" content="center">
                    I am a dedicated and enthusiastic person who continuously explores and learns about Python, HTML,
                    CSS, JavaScript and other current web development frameworks. I see this journey as an opportunity
                    to build a solid place for myself in this dynamic industry.
                    <br/>
                    <br/>
                    I aim to not only learn the syntax of programming languages, but to gain a deep understanding of how
                    they interact and are applied in developing applications and websites. In the near future, I want to
                    become an expert in using these technologies to create interactive and functional solutions.
                </p>
                <a href="#" class="button">Contact Me</a>
            </div>
            <div class="about__image">
                <svg
                        class="about__blob"
                        viewBox="0 0 550 592"
                        fill="none"
                        xmlns="http://www.w3.org/2000/svg"
                >
                    <mask id="maskBorder" mask-type="alpha">
                        <path
                                d="M263 48.1782C270.426 43.891 279.574 43.891 287 48.1782L501.157
                                   171.822C508.583 176.109 513.157 184.032 513.157 192.606V439.894C513.157
                                   448.468 508.583 456.391 501.157 460.678L287 584.322C279.574 588.609
                                   270.426 588.609 263 584.322L48.843 460.678C41.4174 456.391 36.843 448.468 36.843
                                   439.894V192.606C36.843 184.032 41.4174 176.109 48.843 171.822L263 48.1782Z"
                                fill="black"
                        />
                    </mask>
                                        <g mask="url(#maskBorder)">
                                            <rect
                                                    x="37"
                                                    width="476"
                                                    height="630"
                                                    fill="url(#pattern2)"
                                            />

<!--                                            <path-->
<!--                                                    d="M285 51.6423L499.157 175.286C505.345 178.859 509.157 185.461 509.157-->
<!--                                                       192.606V439.894C509.157 447.039 505.345 453.641 499.157 457.214L285-->
<!--                                                       580.858C278.812 584.43 271.188 584.43 265 580.858L50.843 457.214C44.655 453.641-->
<!--                                                       40.843 447.039 40.843 439.894V192.606C40.843 185.461 44.655 178.859 50.843-->
<!--                                                       175.286L265 51.6423C271.188 48.0697 278.812 48.0696 285 51.6423Z"-->
<!--                                                    stroke="black"-->
<!--                                                    stroke-width="10"-->
<!--                                            />-->
                    </g>

<!--                    <rect-->
<!--                            x="37"-->
<!--                            width="476"-->
<!--                            height="300"-->
<!--                            fill="url(#pattern3)"-->
<!--                    />-->

<!--                    <defs>-->
<!--                        <pattern-->
<!--                                id="pattern2"-->
<!--                                patternContentUnits="objectBoundingBox"-->
<!--                                width="1"-->
<!--                                height="1"-->
<!--                        >-->
<!--                            <use-->
<!--                                    href="#imageBorder"-->
<!--                                    transform="matrix(0.00143057 0 0 0.00108108 0.0404062 0)"-->
<!--                            />-->
<!--                        </pattern>-->

<!--                        <pattern-->
<!--                                id="pattern3"-->
<!--                                patternContentUnits="objectBoundingBox"-->
<!--                                width="1"-->
<!--                                height="1"-->
<!--                        >-->
<!--                            <use-->
<!--                                    href="#imageBorder"-->
<!--                                    transform="matrix(0.00143057 0 0 0.00226984 0.0404062 0)"-->
<!--                            />-->
<!--                        </pattern>-->

                         Insert your profile (recommended size: 640 x 940)
<!--                                                <image-->
<!--                                                        class="about__img"-->
<!--                                                        id="imageBorder"-->
<!--                                                        width="640"-->
<!--                                                        height="940"-->
<!--                                                        href="#"-->
<!--                                                />-->
                    </defs>
                </svg>
            </div>
        </div>
    </section>

    <!--==================== SKILLS ====================-->
    <section class="skills section" id="skills">
        <div class="skills__container container grid">
            <div class="skills__data">
                <h3 class="section__subtitle">
                    <span></span>
                </h3>
                <h2 class="section__title">My knowledge</h2>
                <p class="skills__description">
                    Lorem ipsum, dolor sit amet consectetur adipisicing
                    elit. Eaque animi voluptatem perspiciatis ratione
                    autem et distinctio aliquam repellat pariatur
                    adipisci.
                </p>
                <a href="https://github.com/HCZR11" class="button">See Projects</a>
            </div>
            <div class="skills__content">
                <ol class="skills__group">
                    <li class="skills__item">Python</li>
                    <li class="skills__item">HTML&CSS</li>
                    <li class="skills__item">Javascript</li>
                    <li class="skills__item">Django</li>
                    <li class="skills__item">Flask</li>
                </ol>
                <ol class="skills__group" start="6">
                    <li class="skills__item">Git&Github</li>
                    <li class="skills__item">Jeckins</li>
                    <li class="skills__item">Docker</li>
                    <li class="skills__item">CI/CD</li>
                    <li class="skills__item">SQL</li>
                    <li class="skills__item">MongoDB</li>
                </ol>
            </div>
        </div>
    </section>

    <!--==================== SERVICES ====================-->
    <section class="services section" id="services">
        <h3 class="section__subtitle">My <span>Services</span></h3>
        <h2 class="section__title">Major work that i do</h2>
        <div class="services__container container grid">
            <article class="services__card">
                <i class="ri-layout-3-line services__icon"></i>
                <h2 class="services__title">Python developer</h2>
                <p class="services__description">
                    I am a passionate Python Developer specializing in the creation and implementation of innovative
                    technology solutions. With solid experience in web application development, data analysis, and
                    implementation of machine learning algorithms, I bring a unique perspective and hands-on approach to
                    solving complex technical problems.
                </p>
            </article>
            <article class="services__card">
                <i class="ri-pantone-line services__icon"></i>
                <h2 class="services__title">Python Trading</h2>
                <p class="services__description">
                    With remarkable versatility and undeniable computational power, Python has established itself as the
                    language of choice in the field of financial transactions. From analyzing data to implementing
                    automated trading strategies, Python is redefining the way traders interact with the financial
                    markets.
                </p>
            </article>
            <article class="services__card">
                <i class="ri-pen-nib-line services__icon"></i>
                <h2 class="services__title">Graphics Design</h2>
                <p class="services__description">

                    I am a passionate Graphic Designer with a creative approach and a broad artistic vision of the
                    digital world. With a wealth of experience in the design industry, I bring concepts and ideas to
                    life through my image and creativity.
                </p>
            </article>
            <article class="services__card">
                <i class="ri-flutter-fill services__icon"></i>
                <h2 class="services__title">Web Development</h2>
                <p class="services__description">
                    I am an enthusiastic Web Developer, passionate about the art of building and bringing the online
                    environment to life. With a strong background in web application development and a passion for
                    technology, I create engaging and functional digital experiences.
                </p>
            </article>

        </div>
    </section>

    <!--==================== PROJECTS ====================-->
    <section class="projects section" id="projects">
        <h3 class="section__subtitle"><span></span></h3>
        <h2 class="section__title">My Projects</h2>

        <div class="projects__container container grid">
            <article class="projects__card">
                <img
                        src="images/project-1.jpg"
                        alt="First project"
                        class="projects__img"
                />
                <div class="projects__modal">
                    <span class="projects__subtitle"></span>
                    <h2 class="projects__title">Ticket Site</h2>
                    <a href="https://github.com/HCZR11/Ticket-Site" class="projects__button">
                        View demo <i class="ri-external-link-line"></i>
                    </a>
                </div>
            </article>
            <article class="projects__card">
                <img
                        src="images/project-2.jpg"
                        alt="First project"
                        class="projects__img"
                />
                <div class="projects__modal">
                    <span class="projects__subtitle"></span>
                    <h2 class="projects__title">Stock Trading</h2>
                    <a href="https://github.com/HCZR11/ML-Data-Visualization" class="projects__button">
                        View demo <i class="ri-external-link-line"></i>
                    </a>
                </div>
            </article>
            <article class="projects__card">
                <img
                        src="images/project-3.jpg"
                        alt="First project"
                        class="projects__img"
                />
                <div class="projects__modal">
                    <span class="projects__subtitle"></span>
                    <h2 class="projects__title">Woodzech</h2>
                    <a href="https://github.com/HCZR11/woodzech" class="projects__button">
                        View demo <i class="ri-external-link-line"></i>
                    </a>
                </div>
            </article>
            <article class="projects__card">
                <img
                        src="images/project-4.jpg"
                        alt="First project"
                        class="projects__img"
                />
                <div class="projects__modal">
                    <span class="projects__subtitle"></span>
                    <h2 class="projects__title">QR Code</h2>
                    <a href="https://github.com/HCZR11/QR_Code_Scanner" class="projects__button">
                        View demo <i class="ri-external-link-line"></i>
                    </a>
                </div>
            </article>
            <article class="projects__card">
                <img
                        src="images/project-5.jpg"
                        alt="First project"
                        class="projects__img"
                />
                <div class="projects__modal">
                    <span class="projects__subtitle"></span>
                    <h2 class="projects__title">Mini Games</h2>
                    <a href="https://github.com/HCZR11/Mini-Games" class="projects__button">
                        View demo <i class="ri-external-link-line"></i>
                    </a>
                </div>
            </article>
            <article class="projects__card">
                <img
                        src="images/project-6.jpg"
                        alt="First project"
                        class="projects__img"
                />
                <div class="projects__modal">
                    <span class="projects__subtitle">Web</span>
                    <h2 class="projects__title">Modern website</h2>
                    <a href="#" class="projects__button">
                        View demo <i class="ri-external-link-line"></i>
                    </a>
                </div>
            </article>
        </div>
    </section>

    <!--==================== CONTACT ====================-->
    <section class="contact section" id="contact">
        <h3 class="section__subtitle">Get in <span>Touch</span></h3>
        <h2 class="section__title">Contact Me</h2>

        <div class="contact__container container grid">
            <form action="" class="contact__form" id="contact-form">
                <div class="contact__group">
                    <input
                            type="text"
                            required
                            autocomplete="off"
                            placeholder="Enter your name"
                            name="user_name"
                            class="contact__input"
                    />
                    <input
                            type="email"
                            required
                            autocomplete="off"
                            placeholder="Enter your email"
                            name="user_email"
                            class="contact__input"
                    />
                </div>

                <textarea
                        name="user_project"
                        autocomplete="off"
                        required
                        placeholder="Enter your message"
                        class="contact__input"
                ></textarea>

                <p class="contact__message" id="contact-message"></p>

                <button type="submit" class="button contact__button">
                    Send Message
                </button>
            </form>
        </div>
    </section>
</main>

<!--==================== FOOTER ====================-->
<footer class="footer">
    <div class="footer__container container grid">
        <div>
            <h1 class="footer__title">Horoiu<span>Cezar</span></h1>
            <h2 class="footer__education">Junior Python Developer || Web Development || DevOps ||</h2>
        </div>
        <div class="footer__social">
            <a href="#" target="_blank" class="footer__social-link">
                <i class="ri-facebook-circle-line"></i>
            </a>
            <a href="https://www.instagram.com/horoiucezar/" target="_blank" class="footer__social-link">
                <i class="ri-instagram-line"></i>
            </a>
            <a href="https://github.com/HCZR11" target="_blank" class="footer__social-link">
                <i class="ri-twitter-line"></i>
            </a>
            <a href="https://www.linkedin.com/in/horoiucezarcvwriting/" target="_blank" class="footer__social-link">
                <i class="ri-linkedin-line"></i>
            </a>
        </div>
        <span class="footer__copy">
                    &copy; Copyright @.HZCR11 All rights reserved
                </span>
    </div>
</footer>

<!--========== SCROLL UP ==========-->
<a href="#" class="scrollup" id="scroll-up">
    <i class="ri-arrow-up-line"></i>
</a>
<!--=============== SCROLLREVEAL ===============-->
<script src="/js/scrollreveal.min.js"></script>

<!--=============== EMAIL JS ===============-->
<script
        type="text/javascript"
        src="https://cdn.jsdelivr.net/npm/@emailjs/browser@3/dist/email.min.js"
></script>
<!--=============== MAIN JS ===============-->
<script src="/js/main.js"></script>
</body>
</html>