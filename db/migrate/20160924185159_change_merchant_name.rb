class ChangeMerchantName < ActiveRecord::Migration
  def change
    rename_column :charities, :co_merchant_id, :merchant_id
  end
end
