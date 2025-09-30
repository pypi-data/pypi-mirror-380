from GHAReports.mdgen import MDGen, MD_STATUSICONS

test_headers = [
  f"Passed {MD_STATUSICONS['PASS']}",
  f"Failed {MD_STATUSICONS['FAIL']}",
  f"Skipped {MD_STATUSICONS['SKIP']}",
  "Total",
  "Passrate %",
  "Duration (sec)",
]
