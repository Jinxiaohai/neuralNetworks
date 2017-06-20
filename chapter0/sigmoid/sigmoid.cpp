int sigmoid()
{
  double x;
  TF1 *red = new TF1("red", "1./(1.+exp(-0.5*x))", -10, 10);
  TF1 *blue = new TF1("blue", "1./(1.+exp(-x))", -10, 10);
  TF1 *black = new TF1("black", "1./(1.+exp(-2.*x))", -10, 10);

  red->SetLineColor(2);
  red->SetLineWidth(1);
  red->Draw();

  blue->SetLineColor(4);
  blue->SetLineWidth(1);
  blue->Draw("same");

  black->SetLineColor(1);
  black->SetLineWidth(1);
  black->Draw("same");

  red->SetTitle("");
  return 0;
}
