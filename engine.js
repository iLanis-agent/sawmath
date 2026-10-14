// Saw math - chainsaw honesty.
// "50:1" is ounces of oil per gallon of gas, not capfuls. The file size lives
// in the pitch stamped on the drive link, not on the shelf tag.
// Verdicts judge the unrounded figure; rounding is for display only.
var SawMath = (function () {
  function pos(x) { return typeof x === "number" && isFinite(x) && x > 0; }
  function r2(x) { return Math.round(x * 100) / 100; }

  function mixPlan(gasGal, ratio) {
    if (!pos(gasGal) || !pos(ratio)) return { error: "gas and ratio must both be above zero" };
    return { oilOz: r2(gasGal * 128 / ratio) };
  }

  function renderMix(r, gasGal, ratio) {
    return "Your " + gasGal + (gasGal === 1 ? " gallon" : " gallons") + " of gas at " + ratio
      + ":1 takes " + r.oilOz + " oz of oil - measure the cap lines, not capfuls.";
  }

  // Labeled norms: round file size by chain pitch (the pitch is stamped on
  // the drive link; the manual outranks any chart).
  var FILES = { "1/4": "5/32", ".325": "3/16", "3/8": "7/32", ".404": "7/32" };

  function filePlan(pitch) {
    if (!FILES[pitch]) return { error: "pick a chain pitch" };
    return { file: FILES[pitch], pitch: pitch };
  }

  function renderFile(r) {
    return "Your " + r.pitch + " pitch chain files with a " + r.file
      + " in round file - a labeled norm; the pitch is stamped on the drive link.";
  }

  // Labeled norm: a bar cuts its own length minus a couple inches in one pass,
  // and about twice that with a pass from each side.
  function logPlan(barIn, logIn) {
    if (!pos(barIn) || !pos(logIn)) return { error: "bar and log must both be above zero" };
    var verdict;
    if (logIn <= barIn - 2) verdict = "one pass";
    else if (logIn <= barIn * 2 - 4) verdict = "two passes, one from each side";
    else verdict = "beyond the bar - a bigger saw or a different plan";
    return { verdict: verdict };
  }

  function renderLog(r, barIn, logIn) {
    var lead = r.verdict.indexOf("beyond") === 0 ? " is " : " goes in ";
    return "Your " + barIn + " in bar against a " + logIn + " in log" + lead + r.verdict + ".";
  }

  return {
    mixPlan: mixPlan, renderMix: renderMix,
    filePlan: filePlan, renderFile: renderFile,
    logPlan: logPlan, renderLog: renderLog
  };
})();
if (typeof module !== "undefined") module.exports = SawMath;
