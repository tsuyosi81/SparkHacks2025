document.addEventListener("DOMContentLoaded", () => {
  // Initialize the setup process
  const setup = new SetupProcess();
  setup.init();
});

class SetupProcess {
  constructor() {
      this.progressBar = document.querySelector(".progress");
      this.steps = document.querySelectorAll(".step-container");
      this.prevButton = document.getElementById("btn-prev");
      this.nextButton = document.getElementById("btn-next");
      this.currentStep = this.getCurrentStep(); // Get the current step based on the page
  }

  init() {
      // Initialize progress bar and event listeners
      this.updateProgressBar();
      this.addEventListeners();
  }

  // Get the current step based on the page URL
  getCurrentStep() {
      const page = window.location.pathname.split("/").pop(); // Get the current page filename
      switch (page) {
          case "SetUpName.html":
              return 0; // Step 1
          case "SetUpCategory.html":
              return 1; // Step 2
          case "done.html":
              return 2; // Step 3
          default:
              return 0; // Default to Step 1
      }
  }

  // Update the progress bar and step active states
  updateProgressBar() {
      const progressWidth = ((this.currentStep + 1) / this.steps.length) * 100;
      this.progressBar.style.width = `${progressWidth}%`;

      // Update step active states
      this.steps.forEach((step, index) => {
          if (index <= this.currentStep) {
              step.querySelector(".step").classList.add("active");
          } else {
              step.querySelector(".step").classList.remove("active");
          }
      });
  }

  // Go to the next step
  nextStep() {
      if (this.currentStep < this.steps.length - 1) {
          this.currentStep++;
          this.updateProgressBar();
      }
  }

  // Go to the previous step
  previousStep() {
      if (this.currentStep > 0) {
          this.currentStep--;
          this.updateProgressBar();
      }
  }

  // Add event listeners for buttons
  addEventListeners() {
      if (this.nextButton) {
          this.nextButton.addEventListener("click", (e) => {
              this.nextStep(); // Update progress bar
              // Allow navigation after updating the progress bar
              const href = e.currentTarget.closest("a").getAttribute("href");
              if (href) {
                  window.location.href = href; // Navigate to the next page
              }
          });
      }

      if (this.prevButton) {
          this.prevButton.addEventListener("click", (e) => {
              this.previousStep(); // Update progress bar
              // Allow navigation after updating the progress bar
              const href = e.currentTarget.closest("a").getAttribute("href");
              if (href) {
                  window.location.href = href; // Navigate to the previous page
              }
          });
      }
  }
}