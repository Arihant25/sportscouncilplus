import adapter from "@sveltejs/adapter-node";

/** @type {import('@sveltejs/kit').Config} */
const config = {
  kit: {
    adapter: adapter({
      out: "build", // Directory to output the build files
    }),
    // Other configuration options...
  },
};

export default config;
